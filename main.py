from youtubedownloader.getyoutubemp3 import get_youtube_mp3
import pandas as pd
from tqdm import tqdm

if __name__== '__main__':
    # Create a function to read a CSV full of Youtube links and then use
    # function to download them one by one
    downloads = pd.read_csv('YoutubeDownloads.csv')
    # Use the URL and convert to list
    url_list = list(downloads.YoutubeLink)

    for idx, link in enumerate(tqdm(url_list)):
        print(f'[INFO] downloading {link} at index {idx + 1}.')
        get_youtube_mp3(link, output_dir='Downloads')
    