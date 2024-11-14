# LIMMITS25_evaluation

**Latency**

We will evaluate latency as shown in the [challenge website](https://sites.google.com/view/limmits25/challenge/challenge-evaluation). Towards this, we require 2 json files from participants, corresponding to latency. The first file will be named ``teamName_trackX_latency.json`` and the second file will be named ``teamName_trackX_latency_normaliser.json``. _teamName_ should only contain english alphabets and numbers, without space or any special charecters ; you may use upper / lower case. You should maintain the same team names if you are submitting for multiple tracks. Example latency file name - ``iisc_track1_latency.json``

Run [limmits_latency_eval.py](limmits_latency_eval.py) to generate __teamName_trackX_latency_normaliser.json_. You should provide four arguments - 
1. ``--test_set_generated_audios_path``: Path to the synthesized audio files for challenge-track evaluation. All audios must be present in this folder, without any other files or folders.
2. ``--json_path``: Path to the test set metadata json file, for the specific track.
3. ``--team_name``: Your team name, should only contain english alphabets and numbers, without space or any special charecters.
4. ``--save_path``: Path to the directory where the extracted latency will be saved.
5. ``--device``: Use the device where you have synthesised your test audios. 
