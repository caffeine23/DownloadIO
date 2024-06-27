import yt_dlp

def downloadYoutubeVideo(url):
    options = {'format': 'mp4'}
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)
        videoURL = info['url']
        return videoURL, info['title']
