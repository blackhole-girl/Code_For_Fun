# script that downloads youtube videos given a URL

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("there has been an error in downloading your video")
    
    print("this download has completed :-).")

link = input("paste your youtube link here URL: ")
Download(link)
