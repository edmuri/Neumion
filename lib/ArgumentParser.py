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