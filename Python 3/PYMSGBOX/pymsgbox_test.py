from pymsgbox import *

#confirm(text='', title='', buttons=['OK', 'Cancel'])

users = ['admin1','admin2','admin3']

name = prompt(text='Enter username', title='LogIn' , default='')
if(name not in users):
    while(True):
        if(prompt(text='Incorrect username. Type again.', title='LogIn' , default='username') in users):
            break

pasw = prompt(text='Enter password', title='LogIn' , default='', mask='*')
if(pasw != 'admin'):
    while(True):
        if(prompt(text='Enter password', title='LogIn' , default='', mask='*') in users):
            break
else:
    alert(text='Successfully logged in', title='Message', button='OK')
