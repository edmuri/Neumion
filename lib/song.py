import os
import re
from pathlib import Path

class Song:
    def __init__(self, path):
        self.path = path
        self.title = re.sub(r'_+', ' ', Path(path).stem)

    def update_stats(self, tempo=None):
        self.tempo = tempo[0]

    def get_song_duo(self):
        return (self.title, self.path)
    
    def __str__(self):
        formatted = "Name: {0}\nTempo: {1:.2f} BPM\n".format(
                                            self.title,
                                            self.tempo)
        return formatted