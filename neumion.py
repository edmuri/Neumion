import lib.argumentParser as ap
import lib.audioFetcher as af
import lib.dir as d
import lib.output as out
from lib.song import Song

class Neumion:
    def __init__(self, args):
        self.args = args
        self.songs = []

        self.handle_args()

    def handle_args(self):
        if self.args.spotify_link:
            self.song = af.get_spotify_song(
                                self.args.spotify_link, 
                                self.args.keep)
            
        elif self.args.youtube_link:
            self.song = af.get_youtube_song(
                                self.args.youtube_link, 
                                self.args.keep)
            
        else:
            self._construct_paths()

    def _construct_paths(self):
        base = "music/"

        match(bool(self.args.folder), bool(self.args.song)):
            case(False, False):
                raise Exception("Nothing to analyze, returning..")
            case(True, False):
                for path in d.get_files(base+self.args.folder):
                    song_path = base + path
                    self.songs+=[Song(song_path)]
                return
            case(True,True):
                song_path = base+self.args.folder+"/"+self.args.songs
                pass
            case(False, True):
                song_path = base+self.args.song
                pass
        
        self.songs+= [Song(song_path)]

    def analyze(self):
        out.analysis()
        for song in self.songs:
            song.analyze()

    def print(self):
        for song in self.songs:
            print(song)


def main():
    out.start()
    parser = ap.ArgParser()
    args = parser.parse_args()

    neumion_app = Neumion(args)
    neumion_app.analyze()
    neumion_app.print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        out.error(e)
    finally:
        d.clean()