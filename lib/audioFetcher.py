from spotdl import Spotdl
import yt_dlp
from lib.song import Song
import lib.output as out

def _construct_path(keep):
    if keep:
        return "./music/"
    else:
        return "./temp/"

def get_spotify_song(url, keep):

    out.spotify()
    dir = _construct_path(keep)

    spotdl_client = Spotdl(
        client_id="",
        client_secret="",
        downloader_settings={
            "output":"{0}{{title}}.{{output-ext}}".format(dir+"{album}/"),
            "format":"mp3",
        }
    )

    songs = spotdl_client.search([url])
    downloaded_files = spotdl_client.download_songs(songs)

    songs_list = []
    for song, path in downloaded_files:
        songs_list += (Song(path))

    out.spotify_complete()
    return songs_list

def get_youtube_song(url, keep):

    out.youtube()
    dir = _construct_path(keep)
    ydl_opts = {

        "format":"bestaudio/best",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', 
            'preferredquality': '192',
        }],
        'paths': {"home": dir},
        'outtmpl': "%(title)s.%(ext)s", 
        'quiet': True,
    }

    song_list = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = info.get('requested_downloads', [{}])[0].get('filepath')
        
        if not filename:
            filename = ydl.prepare_filename(info)
            if not filename.endswith('.mp3'):
                filename = filename.rsplit('.', 1)[0] + '.mp3'

        song_list += (Song(filename))
    out.youtube_complete()
    return song_list

        