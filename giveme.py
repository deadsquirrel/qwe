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

    exit_code10 = os.system ("mkdir "+put_prjn+"")

    
    exit_code1 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/frontend ./"+put_prjn+"/frontend/")
    print "!!!1",exit_code1
    exit_code2 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/out ./"+put_prjn+"/out/")
    print "!!!2",exit_code2
    exit_code3 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/core ./"+put_prjn+"/core/")
    print "!!!3",exit_code3
    exit_code4 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/edit ./"+put_prjn+"/edit/")
    print "!!!4",exit_code4
    exit_code5 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/config ./"+put_prjn+"/config/")
    print "!!!5",exit_code5
    exit_code6 = os.system("scp -pr "+hostname+":'/var/www/'build.horoshop.com.ua/requirements ./"+put_prjn+"/requirements/")
    print "!!!6",exit_code6
    if exit_code6 == 0:
        print "Ok Download complete!"
        lab2.destroy()
        down_ok.pack()
    else:
        print exit_code,"Ahtung!! ERROR"
        lab2.destroy()
        down_ahtung.pack()

    
    
    # не копирует скрытые дир и файлы
    exit_code7 = os.system("scp -pr "+hostname+":'/var/www/'"+put_prjn+".horoshop.com.ua/* ./"+put_prjn+"/")
    print "!!!7!!",exit_code7
    if exit_code7 == 0:
        print "Ok Download complete!"
        lab2.destroy()
        down_ok.pack()
    else:
        print exit_code7,"Ahtung!! ERROR"
        lab2.destroy()
        down_ahtung.pack()

# директория проекта _создается_ при скачивании scp
# поэтому ее не должно быть перед запуском скрипта, проверку потом сделаю
# -p сохраняет время модификации и по возможности права доступа
# os.system(command) - исполняет системную команду, возвращает
# код её завершения (в случае успеха 0).

#hostname ="yanki@192.168.0.137"
hostname ="cent"
#43y7510bjLV6t3L-1

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
