# -*- coding: utf-8 -*-
from Tkinter import *
import os
import tkMessageBox

'''
def printer(event):
    print ("downloading... step 1, a", a)
'''
def start(event):
    put_dir=ent.get()
    print ("downloading... step 1,  ",put_dir)
    global put_dir
    os.system("scp /tmp/12.py USER@SERVER:PATH")
# цель 1
# mkdir put_dir
# scp -r user@host:'/var/www/build3.4*' ./put_dir/
# цель 2
# scp -r user@host:'/var/www/put_dir' ./put_dir/


'''
думаю получение файлов надо обернуть в "трай"
как в примере:
плюс засунуть все в вайл - пока флаг ГОУ - качаем, как только готово - запускаем следующую закачку
подумать как изменять флаг - условие не придумала

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, reciever, message)
   print "Successfully sent email"
except Exception:
   print "Error: unable to send email"
'''


'''
os.system

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).'''

'''
example with paramiko


import os
import paramiko

ssh = paramiko.SSHClient() 
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()
'''

root = Tk()

but = Button(root,
             text="Apply", 
             width=10,height=1,
             bg="white",fg="green" )

# border for input field
# command???
ent = Entry(root,width=35,bd=3)
#ent = Entry(root,width=35,bd=3, textvariable=a)

lab = Label(root, text="Название проекта",
            width=35,
            bd=10,
            font="Arial 14")

#filename = get(ent)
#print filename
#user =
#server = 
#path = 
#os.system("scp FILE USER@SERVER:PATH")
#e.g. os.system("scp foo.bar joe@srvr.net:/path/to/foo.bar")


# click left button of mouse - <Button-1>
# relations (binding) events and function
#but.bind("<Button-1>", printer)
but.bind("<Button-1>", start)

# visibility of button
lab.pack()
ent.pack()
#tex.pack()
but.pack()


# visibility of window
root.mainloop()


'''
!list remote_dir[N]
N = 0
if ok:
N += 1

'''
''' 
кнопка дестроит окно

from Tkinter import *


class App():
    def __init__(self):
        self.root = Tk()
        button = Button(self.root, text = 'root quit', command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

app = App()
'''
