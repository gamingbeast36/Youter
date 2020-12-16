import subprocess

subprocess.run(['sudo', 'pip3', 'install', 'youtube-dl'])
subprocess.run(['sudo', 'pip3', 'install', 'requests'])
try:
    subprocess.run(['sudo', 'apt', 'install', 'ffmpeg'])
except:
    print("Unable to install dependency")
    print("Please install ffmpeg and add it to path")
    print("Go to https://ffmpeg.org/download.html to donload")