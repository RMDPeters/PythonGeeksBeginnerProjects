# It’s a popular game among children.
# A story will be given to a user and without knowing the story they need to enter a word.
# After entering all the words, a story will be displayed to the user on the screen.

import tkinter as tk

Screen = tk.Tk() # Assign screen variable to tk() method
Screen.title("PythonGeeks Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg='pink')
tk.Label(Screen, text='PythonGeeks Mad Libs Generator').place(x=100, y=20)
Story1Button = tk.Button(Screen, text='A memorable day', font=('Times New Roman', 13), command=lambda: Story1(Screen), bg='Blue')
Story1Button.place(x=140, y=90)
Story2Button = tk.Button(Screen, text='Ambitions', font=('Times New Roman', 13), command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)

Screen.update()
Screen.mainloop()

def Story1(win):
    def final(t1: tk.Toplevel, name, sports, City, playername, drinkname, snacks):
        
        text = f'''
        One day me and my friend {name} decided to play a {sports} game in {City}.
        We wanted to watch {playername}.
        We drank {drinkname} and also ate some {snacks} 
        We really enjoyed! We are looking forward to go again and enjoy
        '''
        
        tk.tl.geometry(newGeometry='500x550')
        
        tk.Label(t1, text='Story:', wraplength=t1.winfo_width()).place(x=160, y=310)
        tk.Label(t1, text=text,wraplength=t1.winfo_width()).place(x=0, y=330)
        
    NewScreen = tk.Toplevel(win, bg='yellow')
    NewScreen.title("A memorable day")
    NewScreen.geometry('500x500')
    tk.Label(NewScreen, text='Memorable Day').place(x=100, y=0)
    tk.Label(NewScreen, text='Name:').place(x=0, y=35)
    tk.Label(NewScreen, text='Enter a game:').place(x=0, y=70)
    tk.Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    tk.Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    tk.Label(NewScreen, text='Enter the name of a drink:').place(x=0, y= 190)
    tk.Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
    Name = tk.Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = tk.Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = tk.Entry(NewScreen, width=17)
    city.place(x=250, y=105)
    player = tk.Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = tk.Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = tk.Entry(NewScreen, width=17)
    snack.place(x=250, y=220)
    SubmitButton = tk.Button(NewScreen, text="Submit", background='Blue', font=('Times', 12),
                            command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(),
                            drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)
    
    NewScreen.mainloop()
        