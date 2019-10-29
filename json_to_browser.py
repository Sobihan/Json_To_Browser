#!/usr/local/bin/python3
import webbrowser, validators
from os import path
from tkinter import *
 
# coding: utf-8

# TODO: Faire une sorte d'interface pour les mises à jour ou faire automatiquement les mises à jour via github

my_string = None
color = 'black'
fcolor = 'white'

def is_json(data):
    import json

    try:
        my_json = json.loads(data)
    except ValueError as e:
        return False
    return True

def open_url(content):
    if (not is_json(content)):
        return False
    url = []
    tmp = None
    split = content.split("\"")
    for i  in range(len(split)):
        if i + 2 >= len(split):
            break
        if split[i] == 'url':
            tmp = split[i + 2]
            if not tmp in url and validators.url(tmp) == True:
                url.append(tmp)
    if (len(url) <= 0):
        print("[DEBUG] There is no url [DEBUG]")
        return (False)
    for i  in range(len(url)):
        webbrowser.open(url[i])
    return (True)

def get_entry():
    """ To get the string of the entry"""
    global my_string, fenetre
    my_string = entree.get()
    if (not open_url(my_string)):
        fenetre.configure(background = 'red')
    else:
        fenetre.configure(background = 'green')
    entree.delete(first = 0, last=len(my_string))

def onclick(Event):
    get_entry()

##################################### Tkinter ########################################
fenetre = Tk()                                                                       #
fenetre.title("Json To Browser by Soso")                                              #
fenetre.configure(background = color)                                                #
canvas = Canvas(fenetre, width = 500, height = 400, bd = 0, bg = color)              #
canvas.pack(padx = 10, pady = 10)                                                    #
string = StringVar()                                                                 #
label = Label(canvas, text= "Paste your JSON", bg = color, fg = fcolor)              #
label.pack()                                                                         #
entree = Entry(canvas, textvariable=string, width=20, fg = 'black', bg = 'grey')     #
entree.pack(padx = 10, pady = 10)                                                    #
fenetre.bind('<Return>', onclick)                                                    #
bouton = Button(canvas, text = "Submit", command = get_entry, fg = 'grey', bg = 'black')            #
bouton.pack()                                                                        #
version = Label(canvas, text = "Version: 2.2.2", bg = color, fg = fcolor)            #
version.pack()
fenetre.mainloop()                                                                   #
######################################################################################

