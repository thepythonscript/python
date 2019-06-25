import tkinter
from tkinter import messagebox
import turtle
import time
from tqdm import tqdm
import os

root = tkinter.Tk()
root.withdraw()

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


