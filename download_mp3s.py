""" 
Name:       download_mp3s.py
Author:     Gary Hutson
Date:       13/06/2022
Purpose:    Downloading YouTube videos and extracting the audio to make MP3 files for 
            burning onto CDs, storing on media players or importing into other music
            libraries
Usage:      Prepare CSV and pass the relevant arguments into the download_multi_mp3s
            function. This expects a CSV as contained in this example
"""

from youtubedownloader.getyoutubemp3 import get_youtube_mp3
import pandas as pd
from tqdm import tqdm
import os.path
import os
import glob

def download_multi_mp3s(download_df, url_field, output_dir='Downloads', verbose=True):
    if os.path.exists(output_dir):
        files = glob.glob(output_dir + '/*')
        for f in files:
            os.remove(f)
    
    downloads = pd.read_csv(download_df)
    url_list = downloads[url_field]
    for idx, link in enumerate(tqdm(url_list)):
        if verbose:
            print(f'\n[INFO] downloading {link} at index {idx + 1}.')
        # Run the function to get our MP3 files    
        get_youtube_mp3(link, output_dir=output_dir)
    return url_list


if __name__== '__main__':
    # Use our download function
    download_list = download_multi_mp3s(
        download_df='YoutubeDownloads.csv',
        url_field='YoutubeLink',
        output_dir='Downloads',
        verbose=False)

    print(download_list)