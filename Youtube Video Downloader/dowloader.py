from pytube import YouTube

# url = input("Paste the link of video you want to download: ")
url = 'https://www.youtube.com/watch?v=HtTUsOKjWyQ'

video = YouTube(url)
print("\n")
print("******* VIDEO TITLE *******")
print(video.title)
print("\n")
print("******* VIDEO THUMBNAIL *******")
print(video.thumbnail_url)
print("\n")
print("Downloading Video..............")
video = video.streams.get_highest_resolution()  # to set stream resolution

# video = video.streams.first() # Alternative to set resolution

# for stream in video.streams:        # To get all the streams
#     print(stream)   

video.download()
print("Downloaded!!!!!")