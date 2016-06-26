# -*- coding: utf-8 -*-
from Tkinter import *

def printer(event):
    print ("downloading... step 1")
    
root = Tk()

but = Button(root,
             text="Apply", 
             width=10,height=1,
             bg="white",fg="green")

# border for input field
ent = Entry(root,width=35,bd=3)

lab = Label(root, text="Название проекта",
            width=35,
            bd=10,
            font="Arial 14")

# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)


# visibility of button
lab.pack()
ent.pack()
#tex.pack()
but.pack()


# visibility of window
root.mainloop()
