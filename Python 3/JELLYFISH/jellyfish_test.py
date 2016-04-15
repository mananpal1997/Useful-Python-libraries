import jellyfish

#checking if two words are homophones (not much accurate)
x,y = map(str,input("Enter two words : ").split())
if(jellyfish.metaphone(x) == jellyfish.metaphone(y) or jellyfish.soundex(x) == jellyfish.soundex(y)):
    print("Homophones !")
else:
    print("Not Homophones !")
'''
#check difference between two words
#returns number of changes
print(jellyfish.levenshtein_distance(x,y))
'''
