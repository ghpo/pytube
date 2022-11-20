#pip install pytube
# importing the module
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=3IWBkDQG9D8')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
