# LIMMITS25_evaluation

**Latency**

We will evaluate latency as shown in the [challenge website](https://sites.google.com/view/limmits25/challenge/challenge-evaluation). Towards this, we require 2 json files from participants, corresponding to latency. The first file will be named ``teamName_trackX_latency.json`` and the second file will be named ``teamName_trackX_latency_normaliser.json``. _teamName_ should only contain english alphabets and numbers, without space or any special charecters ; you may use upper / lower case. You should maintain the same team names if you are submitting for multiple tracks. Example latency file name - ``iisc_track1_latency.json``

Run [limmits_latency_eval.py](limmits_latency_eval.py) to generate ``teamName_trackX_latency_normaliser.json``. You should provide four arguments - 
1. ``--test_set_generated_audios_path``: Path to the synthesized audio files for challenge-track evaluation. All audios must be present in this folder, without any other files or folders.
2. ``--json_path``: Path to the test set metadata json file, for the specific track.
3. ``--team_name``: Your team name, should only contain english alphabets and numbers, without space or any special charecters.
4. ``--save_path``: Path to the directory where the extracted latency will be saved.
5. ``--device``: Use the device where you have synthesised your test audios. 

``teamName_trackX_latency_normaliser.json`` and ``teamName_trackX_latency.json`` should contain the data in the same format. For each synthesised file, we require the following values - 
1. ``time_to_first_frame``
2. ``time_to_last_frame``
3. ``num_frames``
You may refer to [limmits_latency_eval.py](limmits_latency_eval.py) on how to generate these values for your model, and how to save it.
