from pytube import YouTube
import os

def get_youtube_mp3(youtube_link, output_dir='.', verbose=True):
    yt = YouTube(youtube_link)
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    destination = str(output_dir)
    # download the file
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # Switch console printing on and off
    if verbose:
        print('\n[DOWNLOAD COMPLETE] ' + yt.title + " has been successfully downloaded.")
        print('-' * 90)
