#1. Hashing a string 
import hashlib 
s = 'Python Bootcamp'
hash_string = hashlib.md5(s.encode())
hash_string = hashlib.md5(s.encode())
print(hash_string.hexdigest())

#2 Tik Tok video to gif 
from moviepy.editor import VideoFileClip
import os
import urllib

def create_gif():
  urllib.request.urlretrieve(input('Enter video URL:'),'tiktok'+'.mp4')
  tik_tok_vid = VideoFileClip('tiktok.mp4')
  tik_tok_vid.write_gif('tik_tok_gif.gif')
  path = os.path.abspath('tik_tok_gif.gif')
  print(path)
  
create_gif()