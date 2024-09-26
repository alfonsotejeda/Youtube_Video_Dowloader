import os
from pytube import YouTube

def display_progress(stream, chunk, bytes_remaining):
    """
    Display a progress bar for the download.
    
    Args:
        stream: The stream being downloaded.
        chunk: The chunk of data being processed.
        bytes_remaining: The number of bytes remaining to be downloaded.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress_percentage = (bytes_downloaded / total_size) * 100
    progress_bar = f"[{'#' * int(progress_percentage):{100}}]"
    print(f"\r{progress_bar} {progress_percentage:.2f}%", end="", flush=True)
    
    if bytes_downloaded >= total_size:
        print("\nDownload complete")
    
def download_youtube_video():
    """
    Download a YouTube video based on user input.
    """
    video_url = input('Enter YouTube video URL: ')
    
    try:
        yt = YouTube(video_url, on_progress_callback=display_progress)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    available_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
    resolution = input(f'Enter desired resolution {available_resolutions}: ')
    
    if resolution not in available_resolutions:
        print("Invalid resolution. Please choose from the available options.")
        return
    
    video_stream = yt.streams.filter(progressive=True, resolution=resolution).first()
    
    if not video_stream:
        print(f"No video available in {resolution}. Try another resolution.")
        return
    
    download_path = input('Enter download path: ')
    
    if not os.path.exists(download_path):
        print("Invalid download path. Please provide a valid directory.")
        return
    
    try:
        video_stream.download(download_path)
    except Exception as e:
        print(f"Error during download: {e}")

if __name__ == "__main__":
    download_youtube_video()
