import os
import re
from pathlib import Path
import librosa
import numpy as np

class Song:

    def __init__(self, path):
        self.path = path
        self.title = re.sub(r'_+', ' ', Path(path).stem)


    def update_stats(self, tempo=None):
        self.tempo = tempo[0]

    def get_song_path(self):
        return self.path
    
    def analyze(self):
            wave, sample_rate = librosa.load(self.path)
            onset_env = librosa.onset.onset_strength(y=wave, sr= sample_rate)
            tempo, beat_frames = librosa.beat.beat_track(y=wave,sr=sample_rate)
            self.update_stats(tempo)
    
    def __str__(self):
        formatted = "Name: {0}\nTempo: {1:.2f} BPM\n".format(
                                            self.title,
                                            self.tempo)
        return formatted