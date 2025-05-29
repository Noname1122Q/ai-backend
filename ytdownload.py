from pytubefix import YouTube
from pytubefix.cli import on_progress

url1 = "https://youtu.be/SOG0GmKts_I"
url2 = "https://youtu.be/-vMgbJ6WqN4"

yt = YouTube(url2, on_progress_callback=on_progress)
print(yt.title)

yt = yt.streams.get_highest_resolution()
yt.download()