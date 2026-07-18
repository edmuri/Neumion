import librosa
import numpy as np
import os

import lib.output as out
from lib.song import Song
import lib.argumentParser as ap
import lib.audioFetcher as af

class Neumion:
    def __init__(self, args):
        self.args = args

    def handle_args(self):
        if self.args.spotify_link:
            af.get_spotify_song(self.args.spotify_link, self.args.keep)
        elif self.args.youtube_link:
            af.get_youtube_song(self.args.youtube_link, self.args.keep)

    def construct_paths(self):
        base = "Music/"
        self.songs = []

        match(bool(self.args.folder), bool(self.args.song)):
            case(False, False):
                # No Folder, No Song
                raise Exception("Nothing to analyze, returning..")
                pass

            case(False, True):
                # No Folder, Yes Song
                self.songs+= [Song(self.args.song)]
                pass

            case(True, False):
                #Yes Folder, No Song
                for song_path in librosa.util.find_files(base+self.args.folder):
                    self.songs+=[Song(song_path)]
                pass
            
            case(True,True):
                # Yes Folder, Yes Song
                self.songs+= [Song(base+self.args.folder+"/"+self.args.song)]
                pass

    def analyze(self):
        for song in self.songs:
            title,path = song.get_song_duo()
            wave, sample_rate = librosa.load(path)
            tempo, beat_frames = librosa.beat.beat_track(y=wave,sr=sample_rate)
            song.update_stats(tempo)

    def print(self):
        for song in self.songs:
            print(song)


def main():
    out.start()
    parser = ap.ArgParser()
    args = parser.parse_args()

    neumion_app = Neumion(args)
    neumion_app.handle_args()
    # neumion_app.analyze()
    # neumion_app.print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        out.error(e)