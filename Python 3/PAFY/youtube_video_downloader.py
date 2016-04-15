import pyperclip, pafy, os

os.makedirs('E:/YouTube', exist_ok=True)
url = pyperclip.paste()
type = int(input("Hit 1 for video,2 for playlist : "))
qual = int(input("Hit 1 for best clarity, 2 for worst, 3 for other : "))

flag = 0
c = 0
if(qual == 3):
    flag = 1

if(type == 1):
    
    video = pafy.new(url)
    if(flag == 1):
        streams = video.streams
        for s in streams:
            print(str(c)+'. '+s.resolution+', '+s.extension)
            c += 1
        index = int(input("Enter index : "))
        filename = video.streams[index]

    elif(qual == 2):
        index = c - 1
        filename = video.streams[index]

    elif(qual == 1):
        streams = video.streams
        for s in streams:
            c += 1
        filename = video.streams[c-1]

    x = filename.download(filepath='E:/YouTube/')
    print("Download completed.")

else:
    name = str(input("Enter name of playlist folder : "))
    os.makedirs('E:/YouTube/'+name, exist_ok=True)
    video = pafy.get_playlist(url)
    for i in range(0,int(input("Number of videos in playlist you want to download : "))):
        c = 0
        best = video['items'][i]['pafy'].streams
        if(flag == 1):
            for s in best:
                print(str(c)+'. '+s.resolution+', '+s.extension)
                c += 1
            index = int(input("Enter index : "))
            filename = video['items'][i]['pafy'].streams[index]

        elif(qual == 2):
            index = c - 1
            filename = video['items'][i]['pafy'].streams[index]

        elif(qual == 1):
            for s in best:
                c += 1
            filename = video['items'][i]['pafy'].streams[c-1]

        x = filename.download(filepath="E:/YouTube/" + name + "/")
        print(str(i)+" videos downloaded till now.")
    print("Downloads completed.")
