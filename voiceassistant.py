
from cProfile import label
from cgitb import text
import subprocess
import wolframalpha
import pyttsx3
import sys
import tkinter as tk
from tkinter import PhotoImage, ttk
import json
import random
import operator
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PIL import ImageTk, Image


# Startup




def intro():
    speak("what is your name")
    boxstatus('Voice Assistant Status: Listening')
    name = str(takeCommand())
    if name != 'None':
        boxstatus(f'Hello {name}!')
        speak("hello" + name + ", how are you today! i hope you are well")
        accounts.write("USER: " + name + "\n")
        a = True
        while a:
            main()
            time.sleep(3)
    else:
        boxstatus('Did not understand.')
        speak("well, i wasn't able to catch your name, so i'll ask again.")
        time.sleep(0.5)
        intro()

def finduser(username):
    newdow.destroy()
    global name
    name = username
    maingui()
    boxstatus(f'Hello {name}!')
    speak("hello" + name + ", welcome back.")
    a = True
    while a:
        main()
        time.sleep(3)

def accountselection():
    global newdow
    window.destroy()
    newdow = tk.Tk()
    height = int(round(len(accountdata) * (150/6)))
    newdow.geometry(f'320x{height}+470+50')
    newdow.title("Available accounts: ")
    newdow.iconbitmap('./assets/voiceassistlogo.ico')
    for i in accountdata:
        newdow.button = ttk.Button(text = str(i))
        newdow.button['command'] = lambda i=i: finduser(i)
        newdow.button.pack()

def startup():
    boxstatus('Voice Assistant Status: Configuration')
    speak('processing, starting up')
    if not accountdata:
        speak('no previous user interaction detected')
        log('no previous user interaction detected')
        intro()
    elif len(accountdata) == 1:
        name = accountdata[0]
        log(f'username {name} detected')
        speak("hello" + name + ", welcome back.")
        a = True
        while a:
            main()
            time.sleep(3)
    else:
        speak('multiple users detected. please choose your account.')
        accountselection()
        

def main():
    boxstatus('Voice Assistant Status: Listening')
    speak("what would you like to do?")

    query = str(takeCommand()).split()
    boxstatus(f"Analysing input: '{' '.join(query)}'")
    
    if 'obsidian' in query:
        speak("Understood, opening Obsidian")
        os.startfile("C:\\Users\\edwar\\AppData\\Local\\Obsidian\\Obsidian.exe")
        boxstatus("Success!")
    elif 'restart' in query:
        speak("restarting")
        os.execv(sys.executable, ['python'] + sys.argv)
        boxstatus("Success!")
    elif 'Firefox' in query:
        speak("Understood, opening firefox.")
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        boxstatus("Success!")
    elif 'close program' in ' '.join(query):
        speak("Understood, see you again soon.")
        log('Program terminated')
        exit()
    else:
        boxstatus("Failed to understand command.")
        speak("Sorry. i didn't catch that.")

def maingui():
    global window
    window = tk.Tk()

    img = Image.open("./assets/voiceassistlogo.png")
    resized = img.resize((75,75) , resample=3)
    img = ImageTk.PhotoImage(resized)
    
    window.imageLabel = tk.Label(window, image = img)
    
    window.imageLabel.pack()

    window.iconbitmap('./assets/voiceassistlogo.ico')
    window.title("Ed's Voice Assistant!")
    window.geometry('320x130+5+5')

    global label
    window.label = ttk.Label(window, text='tkinter moment')
    window.label.pack()

    window.attributes('-topmost', 1)

    window.update()


#initial_window creation, i.e maingui with intialization button
log('Program Initialised')

global window
window = tk.Tk()

#visual stuff
global img
img = Image.open("./assets/voiceassistlogo.png")
resized = img.resize((75,75) , resample=3)
img = ImageTk.PhotoImage(resized)

window.imageLabel = tk.Label(window, image = img)
window.imageLabel.pack()

window.iconbitmap('./assets/voiceassistlogo.ico')

#core window code

window.title("Ed's Voice Assistant!")
window.text = tk.StringVar()
window.text.set("Press to start program!")
window.geometry('320x130+5+5')

window.label = ttk.Button(window, textvariable = window.text, command = startup)

window.label.pack()
window.attributes('-topmost', 1)
window.mainloop()

