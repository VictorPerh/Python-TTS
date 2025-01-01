import subprocess
import sys
import atexit
import msvcrt

from tkinter import*

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print (f"{package} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall_package(package):
    print(f"Uninstalling {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-y"])


install_package("pyttsx3")

import pyttsx3


engine = pyttsx3.init();

def text_reader():
    text = txtSpeech.get("1.0", END).strip()
    if text:
        engine.say(text)
    else:
        engine.say("Please input your text")
    engine.RunAndWait()


root = Tk()
root.title("Text To Speech Prototype")
root.geometry("1280x720")
Label(root, text = "Enter your Text: ").grid(row=0, column=0, padx=20, pady=20)



#wip
tts_del = input("Would you like to uninstall Python Text-To-Speech Now? Y/N")
if tts_del == "Y":
    atexit.register(uninstall_package, "pyttsx3")
else:
    print ("Press any key to Exit")
    msvcrt.getch()
