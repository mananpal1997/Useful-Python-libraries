from pytube import YouTube
from pprint import pprint
import sys

try:
    yt = YouTube(str(input("Enter youtube video link : ")))
except:
    print("Sorry, link is not correct. Exiting...")
    sys.exit(0)
    
y = 1
a = yt.get_videos()
print("Video options : ")
for x in a:
    print(y,x)
    y += 1

op = int(input("Enter index : "))
choice = str(a[op-1])
ext = choice[choice.find('(')+2 : choice.find(')')]
res = choice[choice.find('-')+2 : choice.find('p')+1]

video = yt.get(ext,res)
video.download('E:/')
