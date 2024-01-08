from pytube import YouTube
from pedalboard.io import AudioFile
from pedalboard import *
import noisereduce as nr
import os


def improve_audio_quality(audio_file_name: str):

    sr=44100
    print(audio_file_name)
    with AudioFile(audio_file_name).resampled_to(sr) as f:
        audio = f.read(f.frames)
    
    
    reduced_noise = nr.reduce_noise(y=audio, sr=sr, stationary=True, prop_decrease=0.75)

    board = Pedalboard([
        NoiseGate(threshold_db=-30, ratio=1.5, release_ms=250),
        Compressor(threshold_db=-16, ratio=2.5),
        LowShelfFilter(cutoff_frequency_hz=400, gain_db=10, q=1),
        Gain(gain_db=10)
    ])

    effected = board(reduced_noise, sr)


    with AudioFile('audio_enhenced.wav', 'w', sr, effected.shape[0]) as f:
        f.write(effected)
    

    return 'audio_enhenced.wav'

def download_youtube_video_to_audio(video_id: str):
        video_link = f"https://www.youtube.com/watch?v={video_id}"

        try:
            video = YouTube(video_link)  # .streams.first().download(video_id)
            # filtering the audio. File extension can be mp4/webm
            # You can see all the available streams by print(video.streams)
            audio = video.streams.filter(only_audio=True)[0]
            audio.download(filename=f"{video_id}.mp3")
            return True, f"{video_id}.mp3"

        except Exception as e:
            print("Connection Error")
            print(e)
            return False, None
