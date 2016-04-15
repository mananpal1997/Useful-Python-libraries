from facepy import *
import os, urllib, sys, time, pyperclip
import tkinter as tk
from tkinter.filedialog import askopenfilename
##############################################################
def get_name_from_uid(author_id):  
    query_string = "SELECT name FROM user WHERE uid = " + str(author_id)  
    author = graph.fql(query_string)  
    if author['data']:  
        return author['data'][0]['name']  
    else:  
        return "Invalid ID"
    
def print_recipients(recipients, message):  
    recipients.remove(message['snippet_author'])  
    for recipient in recipients:  
        print ("  " + get_name_from_uid(recipient))

def get_messages(message_list):  
    for message in message_list:  
        if message:  
            print ("FROM")
            print ("  " + get_name_from_uid(message['snippet_author']))

        print ("RECIPIENT(S)"  )
        print_recipients(message['recipients'], message)
        print ("BODY: " + message['snippet']  )
        print ("-" * 40 + '\n')
        time.sleep(2)
###############################################################
print('WELCOME TO FACEBOOK CONSOLE\n')
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
graph = GraphAPI(token)

print('Press Q to quit')
while(True):
    print('What would you like to do ?')
    print('\t1. Update status')
    print('\t2. Upload photo')
    print('\t3. How many male/female friends you have ?')
    print('\t4. List of pages liked by friends')
    print('\t5. Unread notifications')
    print('\t6. Unread messages')
    x = input("Index : ")
    #try:
    if(x == 'q' or x == 'Q'):
        print('Thanks for using the program.')
        break
    elif(int(x) == 1):
        status = input("Enter your status : ")
        graph.post(path = 'me/feed', message = status)
    try:
        if(int(x) == 2):
            root = tk.Tk()
            root.withdraw()
            file_path = askopenfilename()
            try:
                graph.post(path = 'me/photos', source = open(file_path,'rb'), message = input("Description (Just press Enter if none) : "))
            except:
                print("Error occurred !\nEither file doesn't exist or the file selected is not an image.")
        elif(int(x) == 3):
            male_count = 0
            female_count = 0
            flist = graph.get('me/friends?fields=gender')
            count = len(flist['data'])

            for friend in flist['data']:
                #Checks whether the friend has his gender set to visible.
                if('gender' in friend):
                    friend_gender = friend['gender']
                    if(friend_gender == 'male'):
                        male_count += 1
                    else:
                        female_count += 1

            male_percentage = (male_count/count)*100
            female_percentage = (female_count/count)*100
            print("male friends percentage = " + str(male_percentage))
            print("female friends percentage = " + str(female_percentage))
        elif(int(x) == 4):
            friend_likes = graph.get('me?fields=friends.fields(likes)')
            aa = str(friend_likes)
            aa.replace(':','')
            zz = aa.split(',')
            for i in range(len(zz)):
                if('name' in zz[i]):
                    x = zz[i]
                    for j in range(len(x)):
                        if(x[j] == ':'):
                            start = j+2
                        if(x[j] == "'"):
                            end = j
                    try:
                        if(x[start:end] != '\n'):
                            print(x[start:end].strip())
                            time.sleep(1)
                    except:
                        pass
        elif(int(x) == 5):
            aa = graph.get('me/notifications')
            bb = str(aa)
            notifications = []
            links = []
            try:
                for i in range(len(bb)):
                    if(bb[i:i+5] == 'title'):
                        for j in range(i+9,len(bb)):
                            if(bb[j] == '.'):
                                end = j
                                break
                            if(bb[j] == ','):
                                end = j - 1
                                break
                        notifications.append(bb[i+9 : end])
                    if(bb[i:i+4] == 'link'):
                        for j in range(i+8,len(bb)):
                            if(bb[j] == ','):
                                end = j - 1
                                break
                        if('http' in bb[i+8 : end]):
                            links.append('link : ' + bb[i+8 : end])
            except:
                pass
            print("You have %d unread notifications." % len(notifications))
            for i in range(len(notifications)):
                print("Notification : ",notifications[i])
                print(links[i])
                print()
                time.sleep(4)
        elif(int(x) == 6):
            # FQL: get all messages from inbox  
            fql_get_messages = graph.fql('SELECT snippet, recipients, snippet_author, updated_time FROM thread WHERE folder_id = 1 and unread != 0')
            # Get the data of the messages in a list  
            message_list = fql_get_messages['data']
            # print the messages 
            if message_list:
                get_messages(message_list)  
            else:
                print ("Inbox is Empty")
    except:
        print("Invalid option.")
        print("Terminating",end = '')
        time.sleep(0.5)
        print('.',end = '')
        time.sleep(0.5)
        print('.',end = '')
        time.sleep(0.5)
        print('.',end = '')
        break
