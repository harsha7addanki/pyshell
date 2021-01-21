"""
PyShell Installer
by Harsha Addanki
Oct Wen 7 2020
Edited By Harsha Addanki On Jan 20 2021
"""
import platform
import sys
from tkinter import *
import os
from tkinter.ttk import *
from tkinter.messagebox import *
from http.client import *
import time
root = Tk()

root.iconphoto(False, PhotoImage(file='./icon.ico'))
root.title("PyShell Installer")
b=platform.system()
g6 = HTTPSConnection("raw.githubusercontent.com")
g6.request("GET","/harsha7addanki/pyshell/master/src/pyshell.py")
g98 = g6.getresponse()
dat6 = g98.read()
def x():
    with open("settings.json", "w") as d:
        fr = globals()["r1"].get()
        global b
        if(b == "Windows"):
            d.write('{' + f'\n\t"prompt":"$PRO",\n\t"home":"C:\\\{"Users"}\\\{fr}"\n' + "}")
            globals()["r1"].pack_forget()
            globals()["r2"]["text"] = "We Are Done!"
            globals()["b1"]["text"] = "Quit"
            globals()["b1"]["command"] = root.destroy
        elif(b == "Linux"):
            d.write('{\n\t"prompt":"$PRO",\n\t"home":"/home/' + fr + '"\n}')
            globals()["r1"].pack_forget()
            globals()["r2"]["text"] = "We Are Done!"
            globals()["b1"]["text"] = "Quit"
            globals()["b1"]["command"] = root.destroy
        elif(b == "Darwin"):
            d.write('{\n\t"prompt":"$PRO",\n\t"home":"/Users/' + fr + '"\n}')
            globals()["r1"].pack_forget()
            globals()["r2"]["text"] = "We Are Done!"
            globals()["b1"]["text"] = "Quit"
            globals()["b1"]["command"] = root.destroy
        else:
            globals()["r1"].pack_forget()
            globals()["r2"]["text"] = "Sorry The Operating System Is Not Supported"
            globals()["b1"]["text"] = "Quit"
            globals()["b1"]["command"] = root.destroy
            exit(code=1)
def e():
    if askyesno("Proceed?", "Proceed?") == True :
        globals()["b1"].pack_forget()
        globals()["b1"]["text"] = "Done"
        globals()["b1"]["command"] = x
        globals()["r1"] = Entry(root)
        globals()["r2"] = Label(root,text="Your User Home Folder Name:")
        globals()["r2"].pack()
        globals()["r1"].pack()
        globals()["b1"].pack()
            
        with open("pyshell.py","w") as d:
            d.write(dat6.decode("utf-8"))
            d.close()
        os.remove("psh-installer.py")
        os.remove("icon.ico")
    else:
        exit()
f1 = Label(text="PyShell",font=("monospace", 40))
b1 = Button(root,text="install",command = e)
f1.pack()
b1.pack()

root.mainloop()
exit()
