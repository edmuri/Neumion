import argparse

class ArgParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_args()

    def add_args(self):

        # Album/Playlist
        self.add_argument(
                        "-f",
                        "-folder",
                        dest="folder",
                        help="Specify Album/Playlist to test")
        # Song
        self.add_argument(
                        "-s",
                        "-song",
                        dest="song",
                        help="Specify single song to test")
        
        #spotify link
        self.add_argument(
                        "-sp",
                        "--spotify",
                        dest="spotify_link",
                        help="Specify Spotify Link (playlist/song) to analyze")

        #youtube link
        self.add_argument(
                        "-yt",
                        "--youtube",
                        dest="youtube_link",
                        help="specify Youtube Link ((playlist/song) to analyze)")