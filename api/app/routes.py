from flask import Blueprint, request, jsonify, send_file, make_response
from io import BytesIO
import requests
import os
from moviepy.editor import VideoFileClip, AudioFileClip
from .instagram import downloadInstagramVideo
from .youtube import downloadYoutubeVideo
from .reddit import downloadRedditVideo
from .utils import audioConverter

main = Blueprint('main', __name__)

@main.app_errorhandler(Exception)
def handleError(e):
    response = jsonify(error=str(e))
    response.status_code = 500
    return response

@main.get('/test') # remove later
def test():
    return "Test Passed"

@main.get('/download/youtube')
def downloadYoutube():
    url = request.args.get('url')
    downloadType = request.args.get('type', 'video')
    if not url:
        return jsonify(error='No URL provided.'), 500
    if downloadType != "video" and downloadType != "audio":
        return jsonify(error="Invalid media type."), 500
    try:
        videoURL, title = downloadYoutubeVideo(url)
        response = requests.get(videoURL)
        if response.status_code != 200:
            return jsonify(error="Failed to download video."), 500
        if downloadType == "video":
            file = make_response(send_file(BytesIO(response.content), as_attachment=True, download_name=f"{title}.mp4"))
            file.status_code = 200
            return file
        if downloadType == "audio":
            audioBuffer = audioConverter(response.content)
            file = make_response(send_file(audioBuffer, as_attachment=True, download_name=f"{title}.mp3"))
            file.status_code = 200
            return file
    except Exception as e:
        return jsonify(error=str(e)), 500

@main.get('/download/instagram')
def downloadInstagram():
    url = request.args.get('url')
    downloadType = request.args.get('type', 'video')
    if not url:
        return jsonify(error='No URL provided.'), 500
    if downloadType != "video" and downloadType != "audio":
        return jsonify(error="Invalid media type."), 500
    try:
        videoURL, title = downloadInstagramVideo(url)
        response = requests.get(videoURL)
        if response.status_code != 200:
            return jsonify(error="Failed to download video."), 500
        if downloadType == "video":
            file = make_response(send_file(BytesIO(response.content), as_attachment=True, download_name=f"{title}.mp4"))
            file.status_code = 200
            return file
        if downloadType == "audio":
            audioBuffer = audioConverter(response.content)
            file = make_response(send_file(audioBuffer, as_attachment=True, download_name=f"{title}.mp3"))
            file.status_code = 200
            return file
    except Exception as e:
        return jsonify(error=str(e)), 500
       
@main.get('/download/reddit')
def downloadReddit():
    url = request.args.get('url')
    downloadType = request.args.get('type', 'video')
    if not url:
        return jsonify(error="No URL provided."), 500
    if downloadType != "video" and downloadType != "audio":
        return jsonify(error="Invalid media type."), 500
    try:
        videoURL, audioURL, title = downloadRedditVideo(url)
        if downloadType == "video":
            videoResponse = requests.get(videoURL)
            audioResponse = requests.get(audioURL)
            if videoResponse.status_code != 200 or audioResponse.status_code != 200:
                return jsonify(error="Failed to download video."), 500
            with open("VID.mp4", 'wb') as tempVid, open("AUD.mp3", 'wb') as tempAud:
                tempVid.write(videoResponse.content)
                tempAud.write(audioResponse.content)
                vidClip = VideoFileClip("VID.mp4")
                audClip = AudioFileClip("AUD.mp3")
                output = vidClip.set_audio(audClip)
                output.write_videofile("OUT.mp4")
                with open("OUT.mp4", 'rb') as f:
                    outputFile = BytesIO(f.read())
                    f.close()
            file = make_response(send_file(outputFile, as_attachment=True, download_name=f"{title}.mp4"))
            file.status_code = 200
            return file
        elif downloadType == "audio":
            response = requests.get(audioURL)
            if response.status_code != 200:
                return jsonify(error="Failed to download audio."), 500
            file = make_response(send_file(BytesIO(response.content), as_attachment=True, download_name=f"{title}.mp3"))
            file.status_code = 200
            return file
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        if downloadType == "video":
            vidClip.close()
            audClip.close()
            os.remove("VID.mp4")
            os.remove("AUD.mp3")
            os.remove("OUT.mp4")