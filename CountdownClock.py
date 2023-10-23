# import all relevant libraries
#

from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime

window = Tk() # Creates a window using Tk() method
window.geometry('600x600') # gives size of window
window.title('PythonGeeks') # gives title to window
head = Label(window, text='Countdowm Clock and Timer', font=('Calibri 15')) 
head.pack(pady=20) # Pack() method is used. This method doesn't require x-, y- axis specificity, the program will figure it out.

tk.Label(window,text='Enter a time in HH:MM:SS',font=('Bold')).pack()
tk.Entry(window,textvariable = datetime.hour,width=30).pack()
tk.Entry(window,textvariable = datetime.minute,width=30).pack()
tk.Entry(window,textvariable = datetime.second,width=30).pack()

Checkbutton(text='Check for Music', onvalue=True,variable=check).pack() # creating checkbox

Button(window, text="Set Countdown", command=countdown,bg='yellow').place(x=260,y=230)

#to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
tk.Label(window,text=current_time).pack()

def countdown():
    t=count.get()
    while t:
        mins, secs = divmod(t, 60)
        display = ('{:02d}:{:02d}'.format(mins,secs))
        time.sleep(1) #sleep time 1 sec
        t -= 1
        tk.Label(window, text= display).pack()
        
    tk.Label(window, text='Time-Up', font=('bold', 20)).place(x=250, y=290)
    
