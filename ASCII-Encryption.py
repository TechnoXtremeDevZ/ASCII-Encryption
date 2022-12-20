# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.title("Encryption with ASCII Code")

root.geometry("400x400")
root.configure(background="aquamarine")

user_input = Entry(root)
user_input.place(relx=0.5, rely=0.5, anchor=CENTER)

label = Label(root, text="ASCII Value: ", bg="medium aquamarine", fg="white")
second_label = Label(root, text="Encrypted Value: ", bg="medium aquamarine", fg="white")

def convertASCII():
    input_value = str(user_input.get())
    
    for letter in input_value:
        label["text"] += str(ord(letter)) + " "
        
        ascii = int(ord(letter))     
        encrypted_value = ascii - 1
        
        second_label["text"] += str(chr(encrypted_value))
        
btn = Button(root, text="Display ASCII & Encrypted Values", command=convertASCII, bg="medium aquamarine", fg="white")
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

label.place(relx=0.5, rely=0.7, anchor=CENTER)
second_label.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()