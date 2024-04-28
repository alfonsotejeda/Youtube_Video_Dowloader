from pytube import YouTube
import sys
import os

def show_progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = (bytes_downloaded / total_size) * 100
    progress_bar = "#" * int(percentage_completed) + "-" * (100 - int(percentage_completed))
    print(f"\r[{progress_bar}] {percentage_completed:.2f}%", end="")
    if bytes_downloaded >= total_size:
        print("Dowload complete")
    
link = str(input('Url video: '))

yt = YouTube(link , on_progress_callback= show_progress_bar)

available_video = yt.streams.filter(progressive=True)
video = available_video.filter(resolution=str(input('Reolution (144p , 244p , 360p , 480p, 720p, 1080p) : '))).first() 
if video:
    video.download(str(input('Dowload path: ')))

else:
    print('Try another resolution')
