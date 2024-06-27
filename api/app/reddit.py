import praw
from config import Config
import re

reddit = praw.Reddit(client_id=Config.REDDIT_CLIENT_ID,
                     client_secret=Config.REDDIT_CLIENT_SECRET,
                     user_agent=Config.REDDIT_USER_AGENT)

def downloadRedditVideo(url):
    post = reddit.submission(url=url)
    videoURL = post.media['reddit_video']['fallback_url']
    audioURL = re.sub(r'DASH_\d+', 'DASH_AUDIO_128', videoURL)
    title = post.title[:10]
    return videoURL, audioURL, title
