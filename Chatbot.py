from function.All_function import output
# from function import Database as db
import function.web_job as web_job
import function.All_function as fun
import pyautogui as py
import pywhatkit
import random
import function.variable as var
from colorama import Fore
import os
import webbrowser
import time
name = fun.Name()
fun.head()
output(fun.single_data('help'))
# if fun.internat_on() == "active":
def Main():
    while True:
        query = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
        if fun.json_process_input(query) != None:
                output(fun.json_process_input(query))
    
        elif fun.process_input(query,"time") == "yes":
            output(fun.get_time())
        elif fun.process_input(query,"my name") == "yes":
            output("your name is "+name)
        elif fun.process_input(query,"my ip") == "yes":
            output(var.ip)
            usr = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
            if "1" in usr or "private" in usr:
                pri_ip = fun.Ip()
                output("your private is is "+pri_ip)
            elif "2" in usr or "public" in usr:
                pub_ip = fun.getIP()
                output("your public is is "+pub_ip)
        elif "clear" in query:
            fun.Clear()
            fun.head()
        elif "exit" in query:
            exit()
        elif fun.searching(query) == "yes":
            a = query.replace("search","")
            output("searching "+a)
            time.sleep(2)
            pywhatkit.search(a)
        elif fun.opening(query) == "yes":
            a = query.replace("open","")
            if fun.process_input(a,"facebook") == "yes":
                output("opening facebook...")
                time.sleep(2)
                web_job.open_facebook()
            elif fun.process_input(a,"google") == "yes":
                output("opening google...")
                time.sleep(2)
                web_job.open_google()
            elif fun.process_input(a,"instagram") == "yes":
                output("opening instagram...")
                web_job.open_insta()
            elif fun.process_input(a,"linkedin") == "yes":
                output("opening linkedin...")
                web_job.open_linkedin()
            elif fun.process_input(a,"telegram") == "yes":
                output("opening telegram...")
                web_job.open_telegram()
            elif fun.process_input(a,"github") == "yes":
                output("opening github...")
                web_job.open_github()
            else:
                output("Searching "+a)
                time.sleep(2)
                pywhatkit.search(a)
            
        elif "what is" in query or "who is" in query or "say something" in query or "do you know" in query:
            fun.check_on_wikipedia(query)
        elif fun.process_input(query,"write note" or "write a note") == "yes":
            output("write here what you want to note down")
            note = input(Fore.GREEN +f"{name} :$ "+ Fore.RESET).lower()
            fun.Note_write(note)
        elif fun.process_input(query,"show note" or "see my note" or "show a note") == "yes":
            fun.show_note()
        elif fun.process_input(query,"remove note" or "remove a note" or "delete a note") == "yes":
            fun.remove_note()
        elif "me" in query or "about me" in query:
            sn = fun.json_single_data("me")
            output(sn) 
        elif "see you later" in query or "goodbye" in query or "i am leaving" in query or "have a good day" in query or "bye" in query:
            by = fun.single_data("bye")
            output(by)
        elif "i am good" in query or "not bad" in query or "I am fantastic" in query or "i am okey" in query or "iam feeling good" in query or "iam great" in query:
            wl = fun.single_data('doing well')
            output(wl)
        elif "how are you" in query:
            output(fun.single_data('good'))
        elif "male" in query or "female" in query:
            output(fun.single_data("gender"))
        elif fun.json_process_input(query) == None:
                output("I don't know,What it menes")
                quer = input(Fore.GREEN +f"{name}it menes :$ "+ Fore.RESET) # jahid
                if quer != "i dont know" or "sorry":
                    aa = quer.replace("it menes","")
                    fun.learng_mood(query,aa)
                    output("i will remember it next time")       
                else:
                    output("ok! sir.")

Main()