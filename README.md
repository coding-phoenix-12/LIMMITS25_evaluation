# LIMMITS25_evaluation

**Latency** (for Tracks 1 and 3)

We will evaluate latency as shown in the [challenge website](https://sites.google.com/view/limmits25/challenge/challenge-evaluation). Towards this, we require 2 json files from participants, corresponding to latency. The first file will be named ``teamName_trackX_latency.json`` and the second file will be named ``teamName_trackX_latency_normaliser.json``. _teamName_ should only contain english alphabets and numbers, without space or any special charecters ; you may use upper / lower case. You should maintain the same team names if you are submitting for multiple tracks. Example latency file name - ``iisc_track1_latency.json``

Run [limmits_latency_eval.py](limmits_latency_eval.py) to generate ``teamName_trackX_latency_normaliser.json``. You should provide four arguments - 
1. ``--test_set_generated_audios_path``: Path to the synthesized audio files for challenge-track evaluation. All audios must be present in this folder, without any other files or folders.
2. ``--json_path``: Path to the test set metadata json file, for the specific track.
3. ``--team_name``: Your team name, should only contain english alphabets and numbers, without space or any special charecters.
4. ``--save_path``: Path to the directory where the extracted latency will be saved.
5. ``--device``: Use the device where you have synthesised your test audios. 

``teamName_trackX_latency_normaliser.json`` and ``teamName_trackX_latency.json`` should contain the data in the same format. For each synthesised file, we require the following values - 
1. ``time_to_first_frame``: Time taken to produce first output speech frame (this includes preprocessing, tokenizing and embedding the text and all operations leading to decoding first frame) 
2. ``time_to_last_frame``: Time taken to produce last output speech frame (this is the time taken from first frame to last frame. If you are processing any text embeddings while continously producing frames, you should include it as well)
3. ``num_frames``: Number of output frames generated
   
You may refer to [limmits_latency_eval.py](limmits_latency_eval.py) on how to generate these values for your model, and how to save it. [iisc_track1_latency_normaliser.json](iisc_track1_latency_normaliser.json) is an example file with 2 entries for your reference. If you are not clear regarding the format or the data to store, contact us.

Note: If you are using GPU to decode your model for the test set, use only 1 GPU and a batch size of 1. You must run [limmits_latency_eval.py](limmits_latency_eval.py) on the same hardware.







**Bitrate** (for Tracks 2 and 3)

We will also evaluate Bitrate as shown in the [challenge website](https://sites.google.com/view/limmits25/challenge/challenge-evaluation). For that we need one JSOn file from participants. Units JSON files for track 2 and 3  should be named  teamName_trackX_units.json. teamName should only contain English alphabets and numbers, without space or any special characters. You may use upper / lower case. You should maintain the same team names if you are submitting for multiple tracks. 
Example units file name - ``iisc_track2_units.json`` for track 2 and ``iisc_track3_units.json`` for track 3

	

For Track 2, ``teamName_track2_units.json`` each entry will have a unique identifier which is the ``save_file_name`` field in the provided test file JSON. As attribute-specific units are required for track 2, the ``units`` field will contain a dictionary, with each key being an attribute name (e.g., prosody, content, acoustics). Each key’s value is a list of indices. These indices represent the quantised output from the codebook specific to that attribute. You can refer to the example JSON here 



For Track 3, ``teamName_track3_units.json`` each entry will have a unique identifier which is the ``save_file_name`` field in the provided test file JSON. The ``units`` field will contain a dictionary, where each key is named ``vq1, vq2, ..., vqN``, corresponding to each of the ``N`` codebooks. Each key in the dictionary has a list of indices representing the quantized outputs for that specific codebook.	You can refer to the example JSON here 
