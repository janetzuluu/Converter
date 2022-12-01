from io import StringIO
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pylint import pyreverse as pr
from PIL import Image
from tkinter.filedialog import asksaveasfile, askdirectory
import os

from pylint.lint import Run

import text

# Declare root and widgets
root = tk.Tk()

root.geometry("1000x1000")
root.title('Source Code to UML converter')
my_label = tk.Label(root, text="Welcome to Source Code Converter", font=("Arial Bold", 40))
my_label1 = tk.Label(root, text="How would you like to Continue?", font=("Arial Bold", 40))

fileName = []

# 'paste code' textbox
inputtxt = tk.Text(root,
                   height=40,
                   width=85)

#convert to file
text_box = tk.Text(
    root,
    height=35,
    width=49
)


def test():


    f = open("test.py", "w")
    text_box_string = str(inputtxt.get(1.0, END))
    print(text_box_string)
    f.write(text_box_string)
    f.close()
    converting("test.py")
    scoring("test.py")



def test2():
    f = open("text.py", "w")
    text_box_string2 = str(text_box.get(1.0, END))
    print(text_box_string2)
    f.write(text_box_string2)
    f.close()
    converting2("text.py")
    scoring("text.py")


# 'upload file instead' textbox


# Present needed widgets in root
my_label.pack()
my_label1.pack()



# Function for converting code
def converting(file):
    # terminal commands
    os.system(f"pyreverse {file}")
    os.system(f" pyreverse -o png -f ALL {file}")
    print("I executed the pyreverse!")

    # converting into an image
    imageName = file.split('.')[0]
    currentDir = os.getcwd()
    os.chdir(currentDir)
    os.system(f"pyreverse -o png test.py")
    print("I am creating your uml diagram!")

    img()
def scoring (file):
    os.system(f"pylint {file}")

    print("I am scoring your code")

def converting2(file):
    # terminal commands
    os.system(f" pyreverse -o png -f ALL {file}")
    print("I executed the pyreverse!")
    # converting into an image
    imageName = file.split('.')[0]
    currentDir = os.getcwd()
    os.chdir(currentDir)
    os.system(f"dot -Tpng classes.dot > {imageName}_uml.png")
    os.system(f"pyreverse -o png text.py")
    print("I am creating your uml diagram!")
    img()
def img():
    global img
    img = PhotoImage(file="classes.png")
    position=my_text.index(INSERT)
    my_text.image_create(position,image=img)
    print("Hi, im converting your file!")

btn3 = tk.Button(root, text='Convert', command=lambda:converting(str(fileName[0])))

def onCLick(args):

    if args==1:
        text_box.forget()
        my_text.pack(pady=28,padx=10)
        btn4.forget()
    if args==2:
        inputtxt.forget()
        my_text.pack(pady=28, padx=10 )
        btn3.forget()
def save():
    # creating a image object (main image)
    im1 = Image.open("classes.png")
    # save a image using extension
    im1 = im1.save("Geek9.png")
    my_label4 = tk.Label(root, text="Your UML Diagram has been downloaded to the same "
                                    "directory as this project", font=("Arial", 20))
    my_label4.pack()
# Function for uploading file
def UploadAction(event=None):

    filename = filedialog.askopenfilename()

    # adds file path to list
    fileName.append(filename)
    file = open(filename, 'r')
    txt = file.read()
    file.close()
    global btn4
    # insert 'convert' button command=lambda: [fun1(), fun2()])
    btn4 = tk.Button(root, text='Convert upload', command=lambda:[test2(), onCLick(1)])

    btn4.pack(side='left', anchor='nw')

    # TO REMOVE TEXTBOX FROM 'PASTE CODE'
    if inputtxt.winfo_ismapped() == TRUE:
        inputtxt.forget()
        btn3.forget()


    # WIll show contents of uploaded file
    text_box.pack(expand=True, anchor='nw', padx=5, pady=2)
    text_box.insert('end', txt)
    text_box.config(state='disabled')

# function for pasting your code
def enterr(event=NONE):
    # REMOVE 'UPLOAD A FILE INSTEAD TEXTBOX
    global btn3
    btn3 = tk.Button(root, text='Convert',command=lambda : [test(), onCLick(2)])
    btn3.pack()
    if text_box.winfo_ismapped() == TRUE:
        text_box.forget()
        btn4.forget()
        my_text.forget()


        # clear the textbox before it displays
        inputtxt.delete("1.0", "end")

    inputtxt.pack(padx=5, pady=3)
    btn3.pack(side='left', anchor='nw')


    # TODO: what do you do with the contents of the box


# MAIN MENU BUTTONS AT THE TOP
btn2 = tk.Button(root, text='Paste My Code', command=enterr)
btn2.pack()

btn1 = tk.Button(root, text='Upload a file instead', command=UploadAction)
btn1.pack(padx=4, pady=9)

btn5 = tk.Button(root, text='download', command=lambda: save())
btn5.pack()

my_text=Text(root, width=205, height=60)
#my_text.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
root.mainloop()