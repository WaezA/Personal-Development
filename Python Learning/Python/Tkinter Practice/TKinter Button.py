from tkinter import *

from tkinter import  messagebox

top = Tk()

top.geometry("300x300")

def helloCallBack():
    msg = messagebox.showinfo("Hello Python" , "Hello World ")
    # First text is the title of the window
    # Second text is text in the window

B = Button(top, text = "Hello", command = helloCallBack)  #text = name of the button
B.place(x = 50, y = 50)

top.mainloop()
