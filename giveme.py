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
    exit_code = os.system("scp -pr "+hostname+":'/var/www/'build3.4.horoshop.com.ua ./"+put_prjn+".com.ua/")
    print "!!!",exit_code
    if exit_code == 0:
        print "Ok Download complete!"
        lab2.destroy()
        down_ok.pack()
    else:
        print exit_code,"Ahtung!! ERROR"
        lab2.destroy()
        down_ahtung.pack()
    exit_code2 = os.system("scp -pr "+hostname+":'/var/www/'"+put_prjn+".horoshop.com.ua/* ./"+put_prjn+".com.ua/")
    print "!!!",exit_code2
    if exit_code2 == 0:
        print "Ok Download complete!"
        lab2.destroy()
        down_ok.pack()
    else:
        print exit_code2,"Ahtung!! ERROR"
        lab2.destroy()
        down_ahtung.pack()

# директория проекта _создается_ при скачивании scp
# поэтому ее не должно быть перед запуском скрипта, проверку потом сделаю
# -p сохраняет время модификации и по возможности права доступа
# os.system(command) - исполняет системную команду, возвращает
# код её завершения (в случае успеха 0).
# check -1 
# hostname ="yanki@192.168.0.137"
hostname ="horoshop@89.184.65.107"

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

down_ok = Label(root, text="Ok Download complete!",
            width=35,
            bd=10,
            font="Arial 14")

down_ahtung = Label(root, text="Ahtung!! ERROR",
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

