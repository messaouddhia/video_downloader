from pytube import *
import ffmpeg
from time import sleep
import os

global str
userurl = (input("Enter a youtube video URL : "))
q = str(input("Which quality you want ?  360p,480p,720p,1080p,2K,4K: ")).lower()
yt = YouTube(userurl)
print ("Title of the video : ",yt.title)


def hd2k():
    print("Downloading a 2K video...")
    v = yt.streams.filter(res="1440p", adaptive = True).first().download(filename = "2K")
    print("Video downloaded")
    yt.streams.filter(mime_type="audio")
    a = yt.streams.get_audio_only()
    print("Downloading audio")
    a.download(filename = "audio2K")
    print("audio downloaded")
    sleep(3)
    input_video = ffmpeg.input("2K.webm")
    input_audio = ffmpeg.input('audio2K.mp4')
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output("2Kreadyvideo.mp4").run()
    sleep(0.75)
    os.remove("2K.webm")
    os.remove("audio2K.mp4")

def hd4k():
    print("Downloading a 4K video...")
    v = yt.streams.filter(res="2160p", adaptive = True).first().download(filename = "4K")
    print("Video downloaded")
    yt.streams.filter(mime_type="audio")
    a = yt.streams.get_audio_only()
    print("Downloading audio")
    a.download(filename = "audio4K")
    print("audio downloaded")
    sleep(3)
    input_video = ffmpeg.input("4K.webm")
    input_audio = ffmpeg.input('audio4K.mp4')
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output("4Kreadyvideo.mp4").run()
    sleep(0.75)
    os.remove("4K.webm")
    os.remove("audio4K.mp4")


def hd1080p():
    print("Downloading a HD 1080p video...")
    v = yt.streams.filter(mime_type="video/mp4", res="1080p", adaptive = True).first().download(filename = "HD1080P")
    print("Video downloaded")
    yt.streams.filter(mime_type="audio")
    a = yt.streams.get_audio_only()
    print("Downloading audio")
    a.download(filename = "audio")
    print("audio downloaded")
    sleep(3)
    input_video = ffmpeg.input("HD1080P.mp4")
    input_audio = ffmpeg.input('audio.mp4')
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output("HD1080Preadyvideo.mp4").run()
    sleep(0.75)
    os.remove("HD1080P.mp4")
    os.remove("audio.mp4")


def hd720p():
    print("Downloading a 720p video")
    yt.streams.filter(res="720p", progressive=True).first().download()
    print("Finished.")


def l480p():
    print("Downloading a 480p video.....")
    yt.streams.filter(res="480p", progressive=True).first().download()
    print("Finished.")

def l360p():
    print("Downloading...")
    yt.streams.filter(res="360p", progressive=True).first().download() 
    print("Finished.")
    

if q == "1080" or q == "1080p":
    hd1080p()
elif q == "720" or q == "720p":
    hd720p()
elif q == "480" or q == "480p":
    l480p()
elif q == "360" or q == "360p":
    l360p()
elif q ==  "4" or q == "4k":
    hd4k()
elif q ==  "2" or q == "2k":
    hd2k()
elif q ==  "flh" or q == "flh":
    flh()
else:
    print("invalid choice")







#madeby: Messaouddhia
#instagram: messaouddhia