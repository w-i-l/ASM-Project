import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
from tkinter import Widget
from termcolor import colored
from tkinter import colorchooser
from tkmacosx import *
import tkinter.messagebox as tkmb




#generare cuvant random
f = open("cuvinte.txt", "r")
words = list(x.strip() for x in f)

k1 = 3
k2 = 3


#tkinter interfata
root = tk.Tk()
root.title("Wordle Game")
root.geometry('800x800')
word_to_guess = random.choice(words)
print(word_to_guess)

'''def clear():
    for widgets in root:
        widgets.destroy()
  '''
def color1():
    global k1
    word=e1.get()
    if word in words:
        if not word == word_to_guess:
            for i in range (5):
                    label = Label(test1, text=word[i].upper(), relief=GROOVE)
                    label.grid(row=k1, column=i , padx=10, pady=10)
                    if word[i] == word_to_guess[i]:
                        label.config(foreground = 'green')
                    elif word[i] in word_to_guess:
                        label.config(foreground = 'yellow')
                    else:
                        label.config(foreground= 'white')
    e1.delete(0, 'end')
    k1 += 1
def color2():
    global k2
    word=e2.get()
    pattern=''
    if word in words:
        if not word == word_to_guess:
            for i in range (5):
                    label = Label(test2, text=word[i].upper(), relief=GROOVE)
                    label.grid(row=k2, column=i , padx=10, pady=10)
                    if word[i] == word_to_guess[i]:
                        label.config(foreground = 'green')
                        pattern+='🟩'
                    elif word[i] in word_to_guess:
                        label.config(foreground = 'yellow')
                        pattern+='🟨'
                    else:
                        label.config(foreground= 'white')
                        pattern+='⬜'

    e2.delete(0,'end')
    k2 += 1
    print(pattern)
def instantiate_manual():
    root.destroy()
    global test1
    test1 = tk.Tk()
    global e1
    e1 = Entry(test1, width=50)
    e1.grid(column = 0, row=1, columnspan=10)
    button_go=Button(test1, text='GO!', command= color1)
    button_go.grid(column = 10, row=1)
    test1.geometry("800x800")
    test1.title("Manual Mode")
    label1=Label(test1, text = 'Enter the word...', font= ('Times New Roman', 30), justify = CENTER, anchor=CENTER)
    label1.grid(row=0, column=5 ,columnspan = 15, sticky=N+S+E+W)
    test1.mainloop() 
def instantiate_auto():
    root.destroy()
    global test2
    test2 = tk.Tk()
    global e2
    e2 = Entry(test2, width=50)
    e2.grid(column = 0, row=1, columnspan=10)
    button_go=Button(test2, text='GO!', command= color2)
    button_go.grid(column = 10, row=1)
    test2.geometry("800x800")
    test2.title("Auto Mode")
    label1=Label(test2, text = 'Entry', font= ('Times New Roman', 30), justify = CENTER, anchor=CENTER)
    label1.grid(row=0, column=5 ,columnspan = 15, sticky=N+S+E+W)
    test2.mainloop()
#Butoane meniu
label1 = Label(root, text = 'Wordle Game', font=('Times New Roman', 40, 'bold')).pack(padx=30, pady=100)
button1 = Button(root, text = "Manual", command =  instantiate_manual).pack()
button2 = Button(root, text = "Auto", command = instantiate_auto).pack()

root.mainloop()
