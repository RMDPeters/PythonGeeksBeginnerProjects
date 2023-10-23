from tkinter import *       # tkinter is the python GUI
import tkinter as tk

def binary_search():
    l=e.get().split(" ")
    for i in range(0, len(l)):
        l[i] = int(l[i])
        
    num=(n.get())
    first = 0
    last = len(l)-1
    found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if (l[mid] == num) :
            found = True
        else:
            if num < l[mid]:
                last = mid - 1
            else:
                first = mid - 1
    if found == True:
        Label(window, text="Number found in the list",
              font=('Calibri')).place(x=280,y=180)
    else:
        Label(window, text="number NOT found in the list", font=("Calibri")).place(x=240,y=210)

n=tk.IntVar()    
e=tk.StringVar()

# Create an instance of tkinter frame or winow
window = Tk()
# Set the size of the tkionter window
window.geometry('700x350')
window.title('PythonGeeks') #give title
head=Label(window, text="Let's perform Binary Search", font=('Calibri 15')) 
head.pack(pady=20)
Label(window, text="Enter number you want to search", font=('Calibri')).pack()
Entry(window, textvariable=e).pack()
Entry(window,textvariable=n).place(x=280,y=110)
Button(window, text='Search',
       command=binary_search).place(x=320,y=160).pack()

window.mainloop()     