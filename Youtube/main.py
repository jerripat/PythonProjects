from pytube import YouTube
url = 'https://twitter.com/patloeber/status/1616429276999593987'

my_video = YouTube(url)
print(my_video.title)
print(my_video.thumbnail_url)
my_video = my_video.streams.get_highest_resolution()
for stream in my_video.streams:
    print(stream)

my_video.download()

