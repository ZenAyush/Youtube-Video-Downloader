from pytube import YouTube

user=input('Enter the url:')
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

ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download('Desktop')
print("Download completed!!")