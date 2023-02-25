import requests     
from datetime import datetime, date
import wikipedia
import os
import json
import pyautogui
import random
import re
import wikipedia
import shutil
import colorama
from colorama import Fore
import pyautogui as py
from time import sleep
import requests
from os import path
from urllib.request import urlopen
import re as r
import socket
def internat_on():
  timeout = 1
  try:
      requests.head("http://www.google.com/", timeout=timeout)
      return 'active'
  except requests.ConnectionError:

      return "down"
def get_news(): 
    if internat_on()== "active":
      
        # BBC news api 
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=3b651a51643045f7a8d0c4ee775c68de"
    
        # fetching data in json format 
        open_bbc_page = requests.get(main_url).json() 
    
        # getting all articles in a string article 
        article = open_bbc_page["articles"] 
    
        # empty list which will  
        # contain all trending news 
        results = [] 
        
        for ar in article: 
            results.append(ar["title"]) 
            
        for i in range(len(results)): 
            
            # printing all trending news 
            output(str(i + 1) + " " +results[i]) 
        

        return "So these were the top news from today "
    else:
        return "please check your internet connection first"

def is_ubuntu():
    if 'Ubuntu' in str(os.uname()):
        return True 
    else:
        return False

def Clear():
    if is_ubuntu() == True:
        b = os.system("clear")
        return b
    else:
        a = os.system("cls")
        return a

def get_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%p")
    current_time = ("the current time is "+current_time)
    return current_time

def get_hours():
    now = datetime.now()
    return(now.strftime("%H"))

def get_date():
    return str(date.today())


# ===== screensort ======

def screenshot():
    date = get_date()
    im1 = pyautogui.screenshot()
    im1.save(f'Screensort/my_screenshot({date}).png')
    im2 = pyautogui.screenshot('my_screenshot.png')


# ======== wikipedia module =========

def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("who is", "")
    query = query.replace("what is", "")
    query = query.replace("do you know", "")

    query = query.strip()

    try:
        data = wikipedia.summary(query,  sentences=3)
        output(data)
    except Exception as e:
        return ""


# ======== change welpaper =========

# def change_wallpaper():
#     wallpaper_path = '/media/indrajeet/Inderjit/wallpapers'
#     wallpapers = os.listdir(wallpaper_path)
    
#     wallpaper = random.choice(wallpapers)
#     command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+ wallpaper_path +"/" + wallpaper
#     os.system(command)

#     return "wallpaper changed"



def output(o):
    print(Fore.MAGENTA+"\nBot"+": " + Fore.RESET + f"{o}\n")
    # speak(o)

def process_input(In,out):
    count= 0
    txt = In
    x = re.split("\s", txt)
    y = re.split("\s",out)
    for i in range(len(y)):
        for j in range(len(x)):
            if y[i] == x[j]:
                count +=1
    if len(y) == count:
        return "yes"




def json_process_input(out):
    data_list = []
    file = "Data/Learning_data.json"
    with open(file) as qn:
        data = json.load(qn)
        for i in data:
            data_list.append(i)

    for k in range(len(data_list)):
        t = data_list[k]
        txt = t.lower()
        count = 0
        x = re.split("\s", txt) #how are you
        y = re.split("\s",out) # name
        for i in range(len(y)):
            for j in range(len(x)):
                if y[i] == x[j]:
                    count +=1
        if count == len(x):
            return learing_data(txt) 

def opening(a):
    x = re.split("\s", a)
    for i in range(len(x)):
        if "open" in x[i]:
            return "yes"

def searching(a):
    x = re.split("\s", a)
    for i in range(len(x)):
        if "search" in x[i]:
            return "yes"

def playing(a):
    x = re.split("\s", a)
    for i in range(len(x)):
        if "playing" in x[i]:
            return "yes"

#  === its for linux ===
def kyeboard_shortcuts(query):
    if process_input(query,"switch another wandows")== "yes":
        py.hotkey('alt','tab')
    elif process_input(query,"switch right desktop") == "yes":
        py.hotkey('ctrl','alt','right')
        output("switch right desktop")
    elif process_input(query,"switch left desktop") == "yes":
        py.hotkey('ctrl','alt','left')
    elif process_input(query,"open my terminal") == "yes":
        py.hotkey('ctrl','alt','t')
    elif process_input(query,"close this tab")== "yes":
        py.hotkey('ctrl','w')
    elif process_input(query,"exit firefox") == "yes":
        py.hotkey('clrl','shift','q')
    elif process_input(query,"open private tab") == "yes":
        py.hotkey('clrl','shift','p')
    elif process_input(query,"lock my screen") == "yes":
        py.hotkey('win','l')
    elif process_input(query,"show full screen") == "yes":
        py.hotkey('win','up')
    elif process_input(query,"screen in left") == "yes":
        py.hotkey('win','left')
    elif process_input(query,"screen in right") == "yes":
        py.hotkey('win','right')
    else:
        return "sorry"

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def learing_data(a):
    try:
        filename = "Data/Learning_data.json"
        with open(filename) as QNA:
            data = json.load(QNA)
            da = data[a]
            if a in data:
                if type(data[a]) == list:
                    da = random.choice(data[a])
                    return da
                else:
                    return data[a]
            else:
                output("sorry , no find data")
    except Exception as e:
        return "No"
def head():
    os.system("clear")
    name = "Chat-Bot"
    version = "  version 0.1"
    nm = "="*15+"* "+name+" *"+"="*15
    d = "="*35
    c = "="*29
    print(Fore.GREEN)
    print_centre(d)
    print_centre(nm)
    print_centre(c+" V 0.1")
    print(Fore.RESET)

def learng_mood(a, b):
    filename = 'Data/Learning_data.json'
    dictObj = []
    if path.isfile(filename) is False:
        raise Exception("File not found")
    with open(filename) as fp:
        dictObj = json.load(fp)
    dictObj.update({f"{a}": f"{b}"})
    with open(filename, 'w') as json_file:
        json.dump(dictObj, json_file,
                  indent=4,
                  separators=(',', ': '))

def single_data(a):
    ans = []
    file = 'Data/single.json'
    with open(file) as single:
        data = json.load(single)
        for da in data[f'{a}']:
            ans.append(da)
        daa = random.choice(ans)
        return daa
        
def json_single_data(a):
    ans = []
    file = 'Data/single.json'
    with open(file) as single:
        data = json.load(single)
        for da in data[f'{a}']:
            ans.append(da)
        daa = random.choice(ans)
        return daa


def Name():
    return socket.gethostname()
def Ip():
    ip = socket.gethostbyname(name())
    return ip

def getIP():
	d = str(urlopen('http://checkip.dyndns.com/').read())
	return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

name = Name()


def Note_write(a):
    output("Here give the file name.")
    file = input(Fore.GREEN +f"File name:$ "+ Fore.RESET).lower()
    f = open(f"Data/Note/{file}.txt", "a")
    output("OK! I am saving it")
    f.write(a)
    f.close()
def remove_note():
    output("Here give your file name")
    nm = input(Fore.GREEN +"File name:$ "+ Fore.RESET).lower()
    if os.path.exists(f"Data/Note/{nm}.txt"):
        os.remove(f"Data/Note/{nm}.txt")
        output("Deleted done!")
    else:
        output("The file does not exist")
def show_note():
    output("Here give your file name")
    fnm = input(Fore.GREEN +"File name:$ "+ Fore.RESET).lower()
    f = open(f"Data/Note/{fnm}.txt", "r")
    output(f.read())
