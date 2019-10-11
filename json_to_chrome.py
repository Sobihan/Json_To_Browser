#!/usr/local/bin/python3
import webbrowser
from os import path
from tkinter import * 
# coding: utf-8

def open_url(content):
    if (content == None):
        return (False)
    url = []
    split = content.split("\"")
    for i  in range(len(split)):
        if split[i] == 'url_de_base':
            url.append(split[i + 2])
    if (len(url) <= 0):
        print("[DEBUG] There is no url [DEBUG]")
        return (False)
    chrome_path = "open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome %s"
    for i  in range(len(url)):
        webbrowser.get(chrome_path).open(url[i])
    return (True)

my_string = None

def get_entry():
    global my_string, fenetre
    my_string = entree.get()
    fenetre.quit()

fenetre = Tk()
string = StringVar()
label = Label(fenetre, text="Paste your JSON")
label.pack()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()
bouton=Button(fenetre, text="Submit", command=get_entry)
bouton.pack()
fenetre.mainloop()
if (not open_url(str(my_string))):
    print("There is a problem")
    exit()
else:
    print("There is no problem")
