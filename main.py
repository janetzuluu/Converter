from tkinter import *
import tkinter as tk
from tkinter import filedialog

# Declare root and widgets
root = tk.Tk()
root.geometry("1000x1000")
root.title('Source Code to UML converter')
my_label = tk.Label(root, text="Welcome to Source Code Converter", font=("Arial Bold", 40))
my_label1 = tk.Label(root, text="How would you like to Continue?", font=("Arial Bold", 40))

# OUR ONLY CONVERT BUTTON
btn3 = tk.Button(root, text='Convert')

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


# Function for uploading file
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    file = open(filename, 'r')
    txt = file.read()
    # my_label5 = tk.Label(root, text=txt, font=("Arial Bold", 20))
    # my_label5.pack()
    file.close()

    # TO REMOVE TEXTBOX FROM 'PASTE CODE'
    if inputtxt.winfo_ismapped() == TRUE:
        inputtxt.forget()


    # WIll show contents of uploaded file
    text_box.pack(expand=True, side=LEFT, anchor='nw', padx=5, pady=2)
    text_box.insert('end', txt)
    text_box.config(state='disabled')


# function for pasting your code
def enterr(event=NONE):
    # Input box to paste code
    # if inputtxt.winfo_ismapped() == TRUE:
    #     inputtxt.forget()
    #     btn3.forget()
    # else:
    # REMOVE 'UPLOAD A FILE INSTEAD TEXTBOX
    if text_box.winfo_ismapped() == TRUE:
        text_box.forget()
        # clear the textbox before it displays
        inputtxt.delete("1.0", "end")

    inputtxt.pack(padx=5, pady=2, side=tk.LEFT)
    btn3.pack(side='left', anchor='nw')




# MAIN MENU BUTTONS AT THE TOP
btn2 = tk.Button(root, text='Paste My Code', command=enterr)
btn2.pack()

btn1 = tk.Button(root, text='Upload a file instead', command=UploadAction)
btn1.pack(padx=8, pady=8)

root.mainloop()
