
from pytube import YouTube


def download_youtube_video_to_audio(video_id: str):
        video_link = f"https://www.youtube.com/watch?v={video_id}"

        try:
            video = YouTube(video_link)  # .streams.first().download(video_id)
            # filtering the audio. File extension can be mp4/webm
            # You can see all the available streams by print(video.streams)
            audio = video.streams.filter(only_audio=True)[0]
            audio.download(filename=f"{video_id}.mp3")
            return True

        except Exception as e:
            print("Connection Error")
            print(e)
            return False