# LIMMITS25_evaluation

**Latency**

We will evaluate latency as shown in the [challenge website](https://sites.google.com/view/limmits25/challenge/challenge-evaluation). Towards this, we require 2 json files from participants, corresponding to latency. The first file will be named _teamName_track_X_latency.json_ and the second file will be named _latency_normaliser.json_. 

Run [limmits_latency_eval.py](limmits_latency_eval.py) to generate __teamName_track_X_latency_normaliser.json_. You should provide four arguments - 
1. ``--test_set_generated_audios_path``: Path to the synthesized audio files for challenge-track evaluation. All audios must be present in this folder, without any other files or folders.
2. ``--json_path``: Path to the test set metadata json file, for the specific track.
3. ``--save_path``: Path to the directory where the extracted latency will be saved.
4. ``--device``: Use the device where you have synthesised your test audios. 
