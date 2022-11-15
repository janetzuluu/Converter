from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pylint import pyreverse as pr
import os

# Declare root and widgets
root = tk.Tk()
root.geometry("1000x1000")
root.title('Source Code to UML converter')
my_label = tk.Label(root, text="Welcome to Source Code Converter", font=("Arial Bold", 40))
my_label1 = tk.Label(root, text="How would you like to Continue?", font=("Arial Bold", 40))
fileName = []

# 'paste code' textbox
inputtxt = tk.Text(root,
                   height=30,
                   width=45)

# 'upload file instead' textbox
text_box = Text(
    root,
    height=35,
    width=49
)

# Present needed widgets in root
my_label.pack()
my_label1.pack()


# Function for converting code
def converting(file):
    file = file.split('/')[-1]
    print(file)
    print("Hi, im converting your file!")


# OUR ONLY CONVERT BUTTON
# To pass a function with a vairable, you need to call the lambda keyword
# Command variable works properly with functions without any arguments passed to it
# Lambda functions allows python to pass a function with an argument to the command variable
# we put the index so that when we split() we will not get the ending list bracket ']'
btn3 = tk.Button(root, text='Convert', command=lambda:converting(str(fileName[0])))
# if uploading file convert
# TODO create onClick button event; when button clicked -> file gets terminal command


# Function for uploading file
def UploadAction(event=None):
    filename = filedialog.askopenfilename()

    # adds file path to list
    fileName.append(filename)
    file = open(filename, 'r')
    txt = file.read()
    file.close()

    # insert 'convert' button
    btn3.pack(side='left', anchor='nw')

    # TO REMOVE TEXTBOX FROM 'PASTE CODE'
    if inputtxt.winfo_ismapped() == TRUE:
        inputtxt.forget()

    # WIll show contents of uploaded file
    text_box.pack(expand=True, side=LEFT, anchor='nw', padx=5, pady=2)
    text_box.insert('end', txt)
    text_box.config(state='disabled')


# function for pasting your code
def enterr(event=NONE):
    # REMOVE 'UPLOAD A FILE INSTEAD TEXTBOX
    if text_box.winfo_ismapped() == TRUE:
        text_box.forget()
        # clear the textbox before it displays
        inputtxt.delete("1.0", "end")

    inputtxt.pack(padx=5, pady=2, side=tk.LEFT)
    btn3.pack(side='left', anchor='nw')
    # TODO: what do you do with the contents of the box


# MAIN MENU BUTTONS AT THE TOP
btn2 = tk.Button(root, text='Paste My Code', command=enterr)
btn2.pack()

btn1 = tk.Button(root, text='Upload a file instead', command=UploadAction)
btn1.pack(padx=8, pady=8)

os.system("pyreverse main.py")
print("I executed the pyreverse!")
os.system(f"dot -Tpng classes.dot > uml.png")
print("I am creating your uml diagram!")

root.mainloop()

# TODO have user download the file
# TODO store user pasted text input and save as file so it can be called using pyreverse terminal command
