from pydub import AudioSegment
from io import BytesIO

def audioConverter(video, originalFormat='mp4', audioFormat='mp3'):
    audio = AudioSegment.from_file(BytesIO(video), format=originalFormat)
    audioBuffer = BytesIO()
    audio.export(audioBuffer, format=audioFormat)
    audioBuffer.seek(0)
    return audioBuffer