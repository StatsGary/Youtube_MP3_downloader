# Youtube MP3 Downloader
<img src='imgs/youtube.jpg'>

A python module to take YouTube videos and convert to MP3. This is a wrapper function to download multiple MP3 files. 

## Preparing your data
The data needs to be a CSV file. The CSV file attached will serve as a good example of how it should be structured. There are two ways to run this:
1. The first way is via the download_mp3s.py script - this will expect a CSV and you need to pass the relevant parameters to the function contained therein
2. Download MP3s via the command line. I have included an argument parser for this purpose.

## Using the argument parser
The <a href='https://github.com/StatsGary/Youtube_MP3_downloader/blob/main/download_mp3s_AP.py'>download_mp3s_AP.py</a> file can be used as so:

```
python download_mp3s_AP.py /
    --dataframe_csv YoutubeDownloads.csv /
    --url_field YoutubeLink /
    --output_dir Downloads
```

This will ask you to prompt for the YouTubeDownloads.csv using the  `dataframe_csv` parameter, or whatever you have called your file. It will ask you which column the YouTube URL file in the parameter `url_field` and finally it will ask you for a directory to store the values in `output_dir`.

## Setting up your environment

I used `python==3.9.7` for this demo, so it would make sense for you to create a virtual environment with the same setup.

To duplicate the package requirements, once you have created your virtual environment, use the following command to duplicate the requirements.txt:

```
pip install -r requirements.txt
```

## Closing
If you have found this useful then please give the repository a star and happy downloading...