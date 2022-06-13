from youtubedownloader.getyoutubemp3 import get_youtube_mp3
import pandas as pd
from tqdm import tqdm
import os.path
import os
import glob

def download_multi_mp3s(download_df, url_field, output_dir='Downloads', verbose=True):
    if os.path.exists('Downloads'):
        files = glob.glob('Downloads/*')
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