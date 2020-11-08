"""
PyShell Installer
by Harsha Addanki
Oct Wen 7 2020
"""
import platform
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
root = Tk()

root.iconbitmap("./icon.ico")
root.title("PyShell Installer")
b=platform.system()
def e():
    if askyesno("Proceed?", "Proceed?") == "yes" :
        with open("pyshell.py","a") as d:
            d.write('import subprocess\nimport platform\nimport getpass\nimport json\nimport re\nimport os\nwin = False\nprodef = False\nif platform.system() == \'Linux\':\n    pass\nelif platform.system() == \'Darwin\':\n    pass\nelif platform.system() == \'Windows\':\n    win=True\nwith open("settings.json") as settings_file:\n    settings = json.load(settings_file)\n    pro = settings[\'prompt\']\n    if pro == "$PRO":\n        prodef = True\n    home = settings[\'home\']\ncmd = ""\nif win == False:\n    os.system("clear")\n    print("Welcome To The \\033[1;34;47mPyt\\033[1;33;47mhon\\033[0;0m Shell v1.1.1\\n")\nelse:\n    os.system("cls")\n    print("Welcome To The Python Shell v1.1.1\\n")\nos.chdir(home)\nwhile True:\n    if prodef:\n        if os.getcwd() == home:\n            pro = getpass.getuser() + "@" + platform.node() + ":"+ "~" + "$ "\n        else:\n            pro = getpass.getuser() + "@" + platform.node() + ":"+ os.getcwd() + "$ "\n    try:\n        cmd = input(pro)\n    except KeyboardInterrupt:\n        print("^C")\n    except EOFError:\n        if win == False:\n            print("\\033[31mPyShell: " + cmd + ": Unkown Error\\033[0m")\n        else:\n            print("PyShell: " + cmd + ": Unkown Error")\n    if cmd != "exit":\n        if re.split("\\s",cmd)[0] != "cd":\n            try:\n                if win == False:\n                    process = subprocess.run(re.split("\\s", cmd))\n                    print(str(process.stdout).rstrip("\\nNone"))\n                else:\n                    os.system(cmd)\n            except FileNotFoundError:\n                if win == False:\n                    print("\\033[31mPyShell: " + cmd + ": Command Not Found\\033[0m")\n            except PermissionError:\n                if win == False:\n                    print("\\033[31mPyShell: " + cmd + ": Access Denied\\033[0m")\n            except EOFError:\n                try:\n                    if win == False:\n                        process = subprocess.run(re.split("\\s", cmd))\n                        print(str(process.stdout).rstrip("None").rstrip("\\n"))\n                    else:\n                        os.system(cmd)\n                except EOFError:\n                    if win == False:\n                        print("\\033[31mPyShell: " + cmd + ": Unkown Error\\033[0m")\n                    else:\n                        print("PyShell: " + cmd + ": Unkown Error")\n        else:\n            try:\n                os.chdir(re.split("\\s",cmd)[1])\n            except IndexError:\n                os.chdir(home)\n    elif cmd == "exit":\n        print("Closing pyshell ...")\n        if win == False:\n            subprocess.run(["sleep", "3"])\n            subprocess.run(["clear"])\n        else:\n            os.system("TIMEOUT /T 3")\n            os.system("CLS")\n        exit()')
            d.close()
        with open("settings.json", "a") as d:
            fr = input("Your User Folder Name:")
            global b
            if(b == "Windows"):
                d.write('{' + f'\n    "prompt":"$PRO",\n    "home":"C:\\\{"Users"}\\\{fr}"\n' + "}")
            elif(b == "Linux"):
                d.write('{\n    "prompt":"$PRO",\n  "home":"/home/' + fr + '"\n}')
            elif(b == "Darwin"):
                d.write('{\n    "prompt":"$PRO",\n  "home":"/Users/' + fr + '"\n}')
            else:
                print("ERROR:UNKOWN_OPERATING_SYSTEM")
                exit(code=1)
    else:
        exit()

def a(a):
    b = open(a,"w",encoding='utf-8')
    b.write("")
    b.close()
a("pyshell.py")
label = Label(text="PyShell",font=("monospace", 40))
button = Button(root,text="install",command = e)
label.pack()
button.pack()
root.mainloop()
exit()