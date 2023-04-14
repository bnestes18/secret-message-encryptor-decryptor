from tkinter import *
from tkinter import messagebox
import base64
import os

# import tkinter as tk

def main_screen():

   # Create Widget 
    screen = Tk();
    screen.geometry("375x398")

    # Icon
    # TODO: The statements on lines 16 and 17 do not work on OSX. Figure out another solution!!!
    image_icon = PhotoImage(file='key-lock.gif')
    screen.iconphoto(True, image_icon)

    def reset():
        code.set("")
        textbox1.delete(1.0,END)

    # Title
    screen.title("Secret Message Encryptor/Decryptor")

    # Top Textbox
    Label(text="Enter text for encryption or decryption",fg="black",font=("calibri",13)).place(x=10,y=10)
    textbox1 = Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    textbox1.place(x=10,y=50,width=355,height=100)
    
    # Bottom Textbox
    Label(text="Enter secret key for encryption or decryption",fg="black",font=("calibri",13)).place(x=10,y=170)
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    # Buttons
    Button(text="ENCRYPT",height="2",width=23,highlightbackground="#ed3833",fg="white",bd=0).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,highlightbackground="#00bd56",fg="white",bd=0).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,highlightbackground="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    
    screen.mainloop()

main_screen()


# def main(root):
#     img = tk.PhotoImage(file="key-lock.png")
#     label = tk.Label(image=img)
#     label.pack()

#     label.img = img  # <-- solution for bug 

# if __name__ == "__main__":
#     root = tk.Tk()
#     main(root)
#     root.mainloop()

