# -*- coding: utf-8 -*-
from Tkinter import *
import os
import tkMessageBox


def start(event):
    put_prjn=ent.get()
    print ("downloading... step 1, project:",put_prjn)
    global put_prjn
    lab.destroy()
    ent.destroy()
    but.destroy()
    lab2.pack()
    #    root.destroy()

 

     
root = Tk()

but = Button(root,
             text="Apply", 
             width=10,height=1,
             bg="white",fg="green" )

ent = Entry(root,width=35,bd=3)

lab = Label(root, text="Название проекта",
            width=35,
            bd=10,
            font="Arial 14")

lab2 = Label(root, text="Downloading... waiting",
            width=35,
            bd=10,
            font="Arial 14")

but.bind("<Button-1>", start)

# visibility of button
lab.pack()
ent.pack()
but.pack()


# visibility of window
root.mainloop()

