# import glob
# import subprocess
from pytube import YouTube

user=input('Enter the url:')
chi = input('Kya Aap 720p se Jada Quality ka Video Download Krna Chahte Hai? Yes or No: ').capitalize()
yt=YouTube(user)
print('Video information!')
print('Title : ', yt.title)
print('Number of views: ',yt.views)
#Length of the video
print('Length of video: ',yt.length,'seconds')
#Description of video
print('Description:' ,yt.description)
#Rating
print('Ratings:' ,yt.rating)


if chi == "No":
    print("Downloading....")
    ys = yt.streams.get_highest_resolution()
    ys.download('Desktop')
    print("Download completed!!")

else:
    print("Video Downloading....")
    ys = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
    print("Video Downloaded!!")
    ys.download("Desktop")
    print("Audio Downloading....")
    ya = yt.streams.filter(only_audio=True).first()
    print("Audio Downloaded!!")
    ya.download("Desktop")
    print("Download completed!!")


# Isko Mai Bad Mei Banaunga

# video_files = glob.glob("*.webm")
# audio_files = glob.glob("*.mp4")

# if len(video_files) == 0 or len(audio_files) == 0:
#     print("No video or audio files found.")
#     exit()

# video_file = video_files[0]
# audio_file = audio_files[0]

# # Extract the file name without extension
# video_file_name = video_file.split(".")[0]
# audio_file_name = audio_file.split(".")[0]

# output_file = f"{video_file_name}_merged.mp4"

# # Run the ffmpeg command to merge the video and audio
# command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -strict experimental "{output_file}"'
# subprocess.call(command, shell=True)


