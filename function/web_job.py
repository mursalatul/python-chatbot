import webbrowser
import os
import time

def open_facebook():
    webbrowser.open("https://facebook.com")

def open_google():
    webbrowser.open("https://google.com")
def open_insta():
    time.sleep(2)
    webbrowser.open("https://www.instagram.com")
def open_linkedin():
    time.sleep(2)
    webbrowser.open("https://www.linkedin.com/")
def open_github():
    time.sleep(2)
    webbrowser.open("https://www.github.com/")
def open_telegram():
    time.sleep(2)
    webbrowser.open("https://web.telegram.org/")
def close_browser():
    os.system('pkill chrome')