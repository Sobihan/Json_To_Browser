#!/usr/local/bin/python3
import webbrowser
from os import path
from tkinter import * 
# coding: utf-8

my_string = None
color = 'black'
fcolor = 'white'

def open_url(content):
    if (content == None):
        return (False)
    url = []
    tmp = None
    split = content.split("\"")
    for i  in range(len(split)):
        if split[i] == 'url':
            tmp = split[i + 2]
            if not tmp in url:
                url.append(tmp)
    if (len(url) <= 0):
        print("[DEBUG] There is no url [DEBUG]")
        return (False)
    chrome_path = "open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome %s"
    for i  in range(len(url)):
        webbrowser.get(chrome_path).open(url[i])
    return (True)

def get_entry():
    """ To get the string of the entry"""
    global my_string, fenetre
    my_string = entree.get()
    fenetre.configure(background = 'green')
    fenetre.quit()

def onclick(Event):
    get_entry()

##################################### Tkinter ########################################
fenetre = Tk()                                                                       #
fenetre.title("Json To Chrome by Soso")                                              #
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
fenetre.mainloop()                                                                   #
######################################################################################

if (not open_url(my_string)):
    print("There is a problem")
else:
    print("There is no problem")
