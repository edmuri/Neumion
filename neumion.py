import librosa
import numpy as np
import os

import lib.output as out
import lib.ArgumentParser as ap

class Neumion:
    def __init__(self, args):
        self.args = args
        self.construct_paths()

        self.analyze()
    
    def construct_paths(self):
        base = "Music/"
        self.songs = []
        
        match(bool(self.args.folder), bool(self.args.song)):
            case(False, False):
                # No Folder, No Song
                print("Nothing to analyze, returning..")
                pass
            case(False, True):
                # No Folder, Yes Song
                self.songs+= (self.args.song, 
                              base+self.args.song)
                pass
            case(True, False):
                #Yes Folder, No Song
                print("TBD")
                pass
            case(True,True):
                # Yes Folder, Yes Song
                self.songs+= [(self.args.song, 
                              base+self.args.folder+"/"+self.args.song)]
                pass

    def analyze(self):
        print(self.songs)
        for song,path in self.songs:
            wave, sample_rate = librosa.load(path)
            tempo, beat_frames = librosa.beat.beat_track(y=wave,sr=sample_rate)
            print(song+ ": TEMPO: " + str(tempo))

def main():
    out.start()
    parser = ap.ArgParser()
    args = parser.parse_args()

    Neumion(args)

if __name__ == "__main__":
    main()