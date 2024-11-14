"""
This script is used to extract the normalizing latency of the model.

Author: Sathvik Udupa 2024
"""

import os
import re
import json
import time
import argparse
from pathlib import Path
import torch, torchaudio


parser = argparse.ArgumentParser(description='Script to extract normalizing latency')
parser.add_argument("--test_set_generated_audios_path", required=True, type=str, help="Path to the synthesized audio files for challenge-track evaluation")
parser.add_argument("--json_path", required=True, type=str, help="Path to the test set metadata json file") 
parser.add_argument("--team_name", required=True, type=str, help="Your team name")
parser.add_argument("--save_path", required=True, type=str, help="Path to the directory where the extracted latency will be saved")
parser.add_argument("--device", default="cuda", type=str, help="Use the same GPU hardware that was used for test set synthesis")

NUM_TEST_AUDIOS = 96
TEST_AUDIO_EXTN = ".wav"
LATENCY_NORMALISER_SAVE_NAME = "latency_normaliser.json"
ALLOWED_JSON_NAMES = ["track1", "track2", "track3"]

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.audio_layer = torch.nn.LSTM(input_size=1, hidden_size=20, num_layers=2, batch_first=True)
        self.text_layer = torch.nn.LSTM(input_size=20, hidden_size=20, num_layers=2, batch_first=True)
        self.embedding = torch.nn.Embedding(2, 20)
    
    def encode_text(self, x):
        x = self.embedding(x.long())
        x = self.text_layer(x)
        return x
    
    def generate_one_frame(self, x):
        x = x.unsqueeze(0)
        x = x.transpose(1, 2)
        x = self.audio_layer(x)
        return x

def eval_():
    test_audio_files = os.listdir(args.test_set_generated_audios_path)
    test_audio_files = [f for f in test_audio_files if f.endswith(TEST_AUDIO_EXTN)]
    assert Path(args.json_path).stem in ALLOWED_JSON_NAMES, f"Invalid json file name. Allowed names are {ALLOWED_JSON_NAMES}"
    assert os.path.exists(args.json_path), "Path to the test set metadata json file is invalid"
    assert bool(re.fullmatch(r'[a-zA-Z0-9]+', args.team_name)), f"Invalid team name {args.team_name}. Team name should contain only alphabets and numbers"
    with open(args.json_path, "r") as f:
        metadata = json.load(f)
    save_names = [m["save_file_name"] for m in metadata]
    metadata = {m["save_file_name"]: m for m in metadata}
    assert len(set(save_names)) == len(set(test_audio_files)) == NUM_TEST_AUDIOS, f"{len(set(save_names))} == {len(set(test_audio_files))} == {NUM_TEST_AUDIOS} Test set metadata and test audios do not match"
    
    for file_name in test_audio_files:
        file_name = file_name.replace(TEST_AUDIO_EXTN, "")
        assert file_name in save_names, f"{file_name} not found in test set metadata"
    
    assert args.device != "cpu", "Please use a GPU device for evaluation"
    
    model = Model()
    model.to(args.device)
    model.eval()
    _ = model.encode_text(torch.ones((1, 1)).to(args.device))
    _ = model.generate_one_frame(torch.ones((1, 1)).to(args.device))
    
    results = {}
    
    for audio_file in test_audio_files:
        audio_path = os.path.join(args.test_set_generated_audios_path, audio_file)
        audio, sr = torchaudio.load(audio_path)
        audio = audio.squeeze()
        assert audio.dim() == 1, "Audio should be single channel"
        
        frame_rate = sr // 100
        duration = audio.size(0) / sr
        num_frames = int(duration * frame_rate)
        
        save_name = audio_file.replace(TEST_AUDIO_EXTN, "")
        text = metadata[save_name]["text"]
        text_len = len(text)
        time_to_first_frame = time.time()  
        
        ############## time to first frame ##############
        _ = model.encode_text(torch.ones((1, text_len)).to(args.device))
        _ = model.generate_one_frame(torch.ones((1, 1)).to(args.device))
        #################################################
        
        time_to_first_frame = time.time() - time_to_first_frame ##store time to first frame
        
        time_to_last_frame = time.time()
        
        ############## time to last frame ##############
        for i in range(num_frames - 1):
            _ = model.generate_one_frame(torch.ones((1, 1)).to(args.device))
        ################################################
        
        time_to_last_frame = time.time() - time_to_last_frame ##store time to last frame

        results[save_name] = {
            "time_to_first_frame": time_to_first_frame,
            "time_to_last_frame": time_to_last_frame,
            "num_frames": num_frames,
        }
    save_file = "_".join((args.team_name, Path(args.json_path).stem, LATENCY_NORMALISER_SAVE_NAME))
    with open(os.path.join(args.save_path, save_file), "w") as f:
        json.dump(results, f, indent=4)
    
    print(f"Latency normalizer saved at {os.path.join(args.save_path, save_file)}")
    
    with open(os.path.join(args.save_path, save_file), "r") as f:
        data = json.load(f)
    assert len(data) == NUM_TEST_AUDIOS, "Latency normalizer data is incorrect"        
        
if __name__ == '__main__':
    args = parser.parse_args()
    with torch.no_grad():
        eval_()

