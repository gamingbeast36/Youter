import requests
import re
import subprocess

API_KEY = ''
Search_url = 'https://www.googleapis.com/youtube/v3/search'

def youtquery(q):
	params = {
		'part' : 'snippet',
		'q' : q ,
		'key' : API_KEY,
		'type' : 'video'
	}

	req = requests.get(Search_url, params=params).text
	parse(req)



def parse(req):
	data = req
	for i in range(5):
		video_id = re.findall(r'"videoId".*', data)[i]
		title = re.findall(r'"title".*', data)[i]
		channel_title = re.findall(r'"channelTitle".*', data)[i]
		print(title)
		print(channel_title)
		print(video_id)
		print(" ")


def line_download_music(path, topath):
	a_file = open(path, "r")
	list_of_lists = [(line.strip()).split() for line in a_file]
	a_file.close()
	for line in list_of_lists:
		subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s",'--extract-audio', '--audio-format', 'mp3'] + line)


def line_download_videos(path,topath):
	a_file = open(path, "r")
	list_of_lists = [(line.strip()).split() for line in a_file]
	a_file.close()
	for line in list_of_lists:
		subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s", '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'] + line)

def download_musicid(id, topath):
	subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s", '--extract-audio', '--audio-format', 'mp3', f'https://www.youtube.com/watch?v={id}'])

def download_videosid(id, topath):
	subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s", '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', f'https://www.youtube.com/watch?v={id}'])

def download_musiclink(link, topath):
	subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s", '--extract-audio', '--audio-format', 'mp3', link])

def download_videolink(link, topath):
	subprocess.Popen(['youtube-dl', '-o', f"{topath}%(title)s.%(ext)s", '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', link])
	


