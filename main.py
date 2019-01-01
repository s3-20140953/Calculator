from graphic import *
from cal import *
from Tkinter import *

class Main:

    def __init__(self,master):

        self.calc = Calculator()

root = Tk()
root.title = ("Calculator")
Main(root)
root.mainloop()
