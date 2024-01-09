##TUTORIAL: https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
from tkinter import *                       #Connects to whole tkinter library
class Window(Frame):                        #The Frame for the window
    def __init__(self,master= None):        #What parameters we want it to have
        Frame.__init__(self,master)         #Referencing
        self.master=master                  #Master widget (Main frame)

        self.init_window()

    def init_window(self):                  #Intialising the Window
        self.master.title("GUI")            #Window Title
        self.pack(full=BOTH, expand =1)     #Adjust dimensions as need
        
        quitButton=Button(self, text= "Quit", command= self.client_exit )
        quitButton.place (x=0, y=0)         #Where to place the button

    def client_exit(self):                  #Exit function
        exit()


root = Tk()
root.geometry("400x300")                    #Window Size
app = Window(root)
root.mainloop()                             #Generates Window

