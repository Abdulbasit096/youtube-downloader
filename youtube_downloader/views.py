from django.shortcuts import render , redirect
from pytube import YouTube
from moviepy.editor import *
import os , shutil


url = ''


def home(request):
    return render(request , 'home.html')


def audio(req,format):
    if req.method == 'POST':
        yt = YouTube(url).streams.get_highest_resolution().download()
        mp3 = yt.split('.mp4',1)[0] + f".{format}"
        video = VideoFileClip(yt)
        audio = video.audio
        audio.write_audiofile(mp3)
        homedir = os.path.expanduser('~')
        audio.close()
        video.close()
        os.remove(yt)
        shutil.move(mp3, homedir + '/Downloads')
        return render(req,'complete.html' , {'downloading' : True})
    else:
        return render(req, 'complete.html' , {{'downloading' : False}})



def download(req):
    global url
    url = req.GET.get('url')
    yt = YouTube(url)
    streams = yt.streams
    resolutions = []
    for stream in streams:
        resolutions.append(stream.resolution)
    resolutions = list(dict.fromkeys(resolutions))
    link = url.replace('watch?v=' , 'embed/')
    return render(req , 'home.html',{'resolutions' : resolutions , 'link' :link })




def complete(req,res):
    global url
    resolution = str(res)
    homedir = os.path.expanduser('~')
    dirs = homedir + '/Downloads'
    if req.method  == 'POST':
        yt = YouTube(url).streams.get_by_resolution(resolution).download(homedir + '/Downloads')
        return render(req,'complete.html' , {'downloading' : True})
    else:
        return render(req,'complete.html', {'downloading' : False})
            
    return redirect('home')








