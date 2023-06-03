import os
import subprocess
from pytube import YouTube

user = input('Enter the url:')
yt = YouTube(user)
print('Video information!')
print('Title : ', yt.title)
print('Number of views: ', yt.views)
# Length of the video
print('Length of video: ', yt.length, 'seconds')
# Description of video
print('Description:', yt.description)
# Rating
print('Ratings:', yt.rating)

print("Video Downloading....")
ys = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
print("Video Downloaded!!")
ys.download("./ytVideos")
print("Audio Downloading....")
ya = yt.streams.filter(only_audio=True).first()
print("Audio Downloaded!!")
ya.download("./ytVideos")
print("Download completed!!")

path = "./ytVideos"  # Lists Current Dir Files & Folders
files = os.listdir(path)

# Get all video and audio files in the folder
video_files = [file for file in os.listdir(path) if file.endswith('.webm')]
audio_files = [file for file in os.listdir(path) if file.endswith('.mp4')]

if len(video_files) == 0 or len(audio_files) == 0:
    print("No video or audio files found in the folder.")
    exit()

video_file = os.path.join(path, video_files[0])
audio_file = os.path.join(path, audio_files[0])

# Extract the file name without extension
video_file_name = os.path.splitext(video_files[0])[0]
audio_file_name = os.path.splitext(audio_files[0])[0]

output_file = os.path.join(path, f"{video_file_name}_merged.mp4")

# Run the ffmpeg command to merge the video and audio
command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -strict experimental "{output_file}"'
subprocess.call(command, shell=True)

os.remove(video_file)
os.remove(audio_file)
