#this script is for unix systems
#A program written by Mohammad Jafarzadeh with Python language in 2024 
#which changes the user's IP at any given time.
#This app is supported by the Tor project
#The next updates will also be applied to other systems








import os
import time
import platform
import webbrowser

run = os.system
print(r'''
/------------\           ---------
|___******___|         \/***___***\/
    |****|            \/***/   \***\/
    |****|           \/***/     \***\/
    |****|          \/***/       \***\/
    |****|         \/***/_________\***\/     __________   ________  |------|
    |****|        \/***/***********\***\/   |**********| |********| |***__/
/----****|       \/***/-------------\***\/   ---|**|---  |**(__)**| |**|
|********|      \/***/               \***\/     |**|     |********| |**|
\--------/     \/___/                 \___\/    |__|      --------  |**|
                        V 1.0
             https://github.com/Japharzadeh
''')
webbrowser.open('https://github.com/Japharzadeh', 2)

def ubuntu():
    run('sudo apt upgrade -y')
    run('sudo apt update -y')
    run('sudo apt install tor -y')
    run('python -m pip install requests')
    print('Downloads completed!!')
    sec = input('[+] time to change Ip in Sec [type=60] >> ')
    while True:
        run('service tor start')
        print("IP changed")
        time.sleep(sec)
def termux():
    run('pkg upgrade -y')
    run('pkg update -y')
    run('pkg install tor -y')
    run('python -m pip install requests')
    print('Downloads completed!!')
    sec = input('[+] time to change Ip in Sec [type=60] >> ')
    while True:
        run('service tor start')
        print("IP changed")
        time.sleep(sec)

platform = platform.system()
if platform == 'windows':
    print("Can't open in windows:(" )
elif platform == 'linux':
    type = input('''[1] Ubuntu
    [2] Termux
    [3] Kalli''')
    if type == '1':
        ubuntu()
    elif type == '2':
        termux()
    elif type == '3':
        ubuntu()



