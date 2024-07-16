from pytube import *

def YT_downloader(url):
    SAVE_PATH= "/mnt/23C62AAA2960B420/PY_REPO/video_download"
    yt= YouTube(url)
    mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
    d_video = mp4_streams[-1]
    try:
    #yt.download()
    # downloading the video 
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except:
        print(f"error getting {url}")
    print("Download complete")
url=input("Paste Video URL")
url= url.strip()
YT_downloader(url)
# yt = YouTube(
        #url,
        # "https://youtu.be/8JJ101D3knE",
        # on_progress_callback=progress_func,
        # on_complete_callback=complete_func,
#  
# url=input("Paste Video URL")
# url= url.strip()
# yt = YouTube(
        # url,
        # "https://youtu.be/8JJ101D3knE",
        # on_progress_callback=progress_func,
        # on_complete_callback=complete_func,
        # proxies=my_proxies,
        # use_oauth=False,
        # allow_oauth_cache=True
    # )      proxies=my_proxies,
        # use_oauth=False,
        # allow_oauth_cache=True
    # )
#https://youtu.be/8JJ101D3knE