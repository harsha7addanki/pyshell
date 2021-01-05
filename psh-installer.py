"""
PyShell Installer
by Harsha Addanki
Oct Wen 7 2020
"""
import platform
import sys
from tkinter import *
import os
from tkinter.ttk import *
from tkinter.messagebox import *
root = Tk()

root.iconphoto(False, PhotoImage(file='./icon.ico'))
root.title("PyShell Installer")
b=platform.system()
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
            d.write('import subprocess\nimport platform\nimport getpass\nimport json\nimport re\nimport os\nwin = False\nprodef = False\nif platform.system() == \'Linux\':\n\tpass\nelif platform.system() == \'Darwin\':\n\tpass\nelif platform.system() == \'Windows\':\n    win=True\nwith open("settings.json") as settings_file:\n    settings = json.load(settings_file)\n    pro = settings[\'prompt\']\n    if pro == "$PRO":\n        prodef = True\n    home = settings[\'home\']\ncmd = ""\nif win == False:\n    os.system("clear")\n    print("Welcome To The \\033[1;34;47mPyt\\033[1;33;47mhon\\033[0;0m Shell v1.2.2\\n")\nelse:\n    os.system("cls")\n    print("Welcome To The Python Shell v1.2.2\\n")\nos.chdir(home)\nwhile True:\n    if prodef:\n        if os.getcwd() == home:\n            pro = getpass.getuser() + "@" + platform.node() + ":"+ "~" + "$ "\n        else:\n            pro = getpass.getuser() + "@" + platform.node() + ":"+ os.getcwd() + "$ "\n    try:\n        cmd = input(pro)\n    except KeyboardInterrupt:\n        print("^C")\n    except EOFError:\n        if win == False:\n            print("\\033[31mPyShell: " + cmd + ": Unkown Error\\033[0m")\n        else:\n            print("PyShell: " + cmd + ": Unkown Error")\n    if cmd != "exit":\n        if re.split("\\s",cmd)[0] != "cd":\n            try:\n                if win == False:\n                    process = subprocess.run(re.split("\\s", cmd))\n                    print(str(process.stdout).rstrip("\\nNone"))\n                else:\n                    os.system(cmd)\n            except FileNotFoundError:\n                if win == False:\n                    print("\\033[31mPyShell: " + cmd + ": Command Not Found\\033[0m")\n            except PermissionError:\n                if win == False:\n                    print("\\033[31mPyShell: " + cmd + ": Access Denied\\033[0m")\n            except EOFError:\n                try:\n                    if win == False:\n                        process = subprocess.run(re.split("\\s", cmd))\n                        print(str(process.stdout).rstrip("None").rstrip("\\n"))\n                    else:\n                        os.system(cmd)\n                except EOFError:\n                    if win == False:\n                        print("\\033[31mPyShell: " + cmd + ": Unkown Error\\033[0m")\n                    else:\n                        print("PyShell: " + cmd + ": Unkown Error")\n        else:\n            try:\n                os.chdir(re.split("\\s",cmd)[1])\n            except IndexError:\n                os.chdir(home)\n    elif cmd == "exit":\n        print("Closing pyshell ...")\n        if win == False:\n            subprocess.run(["sleep", "3"])\n            subprocess.run(["clear"])\n        else:\n            os.system("TIMEOUT /T 3")\n            os.system("CLS")\n        exit()')
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