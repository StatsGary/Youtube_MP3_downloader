""" 
Name:       download_mp3s_AP.py
Author:     Gary Hutson
Date:       13/06/2022
Purpose:    Downloading YouTube videos and extracting the audio to make MP3 files for 
            burning onto CDs, storing on media players or importing into other music
            libraries
Usage:      python download_mp3s_AP.py --dataframe_csv YoutubeDownloads.csv 
            --url_field YoutubeLink --output_dir Downloads
"""


from youtubedownloader.getyoutubemp3 import get_youtube_mp3
import pandas as pd
from tqdm import tqdm
import os.path
import os
import glob
import argparse as ap

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
    # Setup argument parser
    parser = ap.ArgumentParser()
    parser.add_argument('-d', '--dataframe_csv', required=True, 
        help='Data frame with list of urls to download')
    parser.add_argument('-f', '--url_field', required=True, default='YoutubeLink',
        help='Field containing the unique YouTube URL')
    parser.add_argument('-o', '--output_dir', default='Downloads',
        help='Directory where to output converted MP3s')
    args = vars(parser.parse_args())

    
    # Use our download function
    download_list = download_multi_mp3s(
        download_df=args['dataframe_csv'],
        url_field=args['url_field'],
        output_dir=args['output_dir'],
        verbose=False)

    print(download_list)