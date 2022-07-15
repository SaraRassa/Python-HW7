from moviepy import editor

video= editor.VideoFileClip('C:\Python Codes\session7\sample.mp4.mp4')
audio=video.audio.write_audiofile('sample.mp3')