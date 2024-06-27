import instaloader

def downloadInstagramVideo(url):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
    videoURL = post.video_url
    title = videoURL[-5:]
    return videoURL, title
