import tkinter as tk
from GlobalVars import *
import time

def RunGUI():
    def GUIUpdate(event=None):
        print(SteeringPassThrough.get())
        Settings.SteeringPassThrough=not bool(SteeringPassThrough.get())




    root = tk.Tk()
    root.geometry("200x800")

    SteeringPassThrough = tk.IntVar()
    SteeringPassthroughCheckbox = tk.Checkbutton(root, text="Steering Passthrough", variable=SteeringPassThrough,command=GUIUpdate)
    SteeringPassthroughCheckbox.pack()



    root.mainloop()