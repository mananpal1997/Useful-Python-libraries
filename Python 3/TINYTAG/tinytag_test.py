from tinytag import TinyTag
import os, shutil

#separate songs according to genre
not_found = []
for f1,f2,f3 in os.walk('E:/Songs/Songs/'):
    for f in f3:
        try:
            if('.mp3' not in f):
                continue
            tag = TinyTag.get('E:/Songs/Songs/'+f)
            ge = tag.genre
            os.makedirs('E:/Songs/Songs/'+ge, exist_ok = True)
            shutil.move('E:/Songs/Songs/'+f,'E:/Songs/Songs/'+ge+'/')
        except:
            not_found.append(f)

print("Following were not categorized : ")
for x in not_found:
    print(x)

#remove duplicate songs(not 100 % accurate)
songs = []
for f1,f2,f3 in os.walk('E:/Songs/Songs'):
	for f in f3:
		try:
			t = TinyTag.get('E:/Songs/Songs/'+str(f))
			name = str(t.title)
			if(name not in songs):
				songs.append(name)
			elif(name == 'None' or name == None or name == ''):
				songs.append(str(f))
			else:
				os.unlink('E:/Songs/Songs/'+str(f))
		except:
			pass

#Other features : t.bitrate / t.duration / t.filesize
