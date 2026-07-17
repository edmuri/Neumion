from spotdl import Spotdl
import yt_dlp

def get_spotify_song(url):

    spotdl_client = Spotdl(
        client_id="",
        client_secret="",
        downloader_settings={
            "output":"./Music/{album}/{title}.{output-ext}",
            "format":"mp3",
        }
    )

    songs = spotdl_client.search([url])
    downloaded_files = spotdl_client.download_songs(songs)
    print(downloaded_files)
    for song in downloaded_files:
        print(song.Song)
    return downloaded_files

def get_youtube_song(url):
    print("TBI")
    return
    ydl_opts = {
        "format":"bestaudio/best",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # Tell FFmpeg to extract the audio
            'preferredcodec': 'mp3',     # Convert it to WAV for clean librosa parsing
            'preferredquality': '192',   # Standard high-quality bit rate
        }],
        # Save the file with the video title as the filename inside our directory
        'outtmpl': '%(title)s.%(ext)s', 
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(info)
        filename = ydl.prepare_filename(info)
        print(filename)