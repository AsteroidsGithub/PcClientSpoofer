# Import module 
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

import threading
import os

import time
import datetime

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
  
# Create object 
root = tk.Tk()
root.configure(background='green')

finish = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'Images/finish.png'))
lock = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'Images/lock.png'))
finishO = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'Images/finishOrange.png'))
lockO = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'Images/lockOrange.png'))
  
# Adjist size 
root.geometry("365x40") 
  
# Use overrideredirect() method 
root.overrideredirect(True) 

lockButton = tk.Button(
    image=lock,
    bg="green",
    bd=0,
)

FinishButton = tk.Button(
    image=finish,
    bg="green",
    bd=0,
)

entry = tk.Entry(
    width=11,
    bd=0,
    bg="white",
    justify="center",
    font=("Calibri 13")
)

padx = 4
pady = 4

entry.pack(fill=tk.Y, side=tk.LEFT, padx=padx, pady=pady,)
FinishButton.pack(fill=tk.Y, side=tk.RIGHT, padx=padx, pady=pady,)
lockButton.pack(fill=tk.Y, side=tk.RIGHT, padx=padx, pady=pady,)

root.call('wm', 'attributes', '.', '-topmost', True)

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

def convertTime(x):
    return time.strftime('%H:%M:%S', time.gmtime(x))

def countdown():
    global my_timer
    my_timer = 3300
    while my_timer > 0:
        if my_timer < 300:
            root.configure(background='#EC9C25')
            lockButton.configure(image=lockO,background='#EC9C25')
            FinishButton.configure(image=finishO,background='#EC9C25')
        
        time.sleep(1)
        my_timer -= 1
        entry.delete(0, tk.END)
        entry.insert(0, f"{convertTime(my_timer)}")
    my_timer = 3300

countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

# Execute tkinter 
root.mainloop() 
