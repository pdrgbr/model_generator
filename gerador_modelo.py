import pandas as pd
from fpgrowth_py import fpgrowth
from datetime import datetime
import requests
from io import StringIO

url_tracks = "https://homepages.dcc.ufmg.br/~cunha/hosted/cloudcomp-2023s2-datasets/2023_spotify_ds1.csv"
url_songs = "https://homepages.dcc.ufmg.br/~cunha/hosted/cloudcomp-2023s2-datasets/2023_spotify_songs.csv"

response_tracks = requests.get(url_tracks)
response_songs = requests.get(url_songs)

if response_tracks.status_code == 200 and response_songs.status_code == 200:
    tracks  = pd.read_csv(StringIO(response_tracks.text))
    songs = pd.read_csv(StringIO(response_songs.text))

pid_to_track_names = {}
for _, row in tracks.iterrows():
    pid = row['pid']
    track_name = row['track_name']
    if pid not in pid_to_track_names:
        pid_to_track_names[pid] = []
    pid_to_track_names[pid].append(track_name)

array_de_arrays = [track_names for pid, track_names in pid_to_track_names.items()]

lista_de_listas = [track_names for track_names in array_de_arrays]

min_support_ratio = 0.05
min_confidence = 0.05
freqItemSet, rules = fpgrowth(lista_de_listas, minSupRatio=min_support_ratio, minConf=min_confidence)

output_file_path = '/model_gen/project2-pv/association_rules.txt'

with open(output_file_path, 'w') as file:
    file.write("version: 1.0\n")

    run_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file.write(f"run_time: {run_time}\n")
    for rule in rules:
        file.write(f"{rule}\n")