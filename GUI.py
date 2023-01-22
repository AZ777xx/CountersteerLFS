import sys
import tkinter as tk
from GlobalVars import *
import gc
import time

def RunGUI():
    def GUIReadVars(event=None):
        print(SteeringPassThrough.get())
        Settings.SteeringPassThrough=SteeringPassThrough.get()



    def GUIWrite():
        LFSActualMaxAngleText.set("Measured Max Angle = " + str(round(InternalVars.LFSMaxMeasuredSteeringAngle * 57.2958,2)) + "            ")
        if InternalVars.ClosingApp !=1:
            root.after(300, GUIWrite)


    def ResetAngleMeasure(event=None):
        InternalVars.LFSMaxMeasuredSteeringAngle=0
        GUIWrite()

    def OnExit():
        root.destroy()

    root = tk.Tk()
    root.geometry("300x800")

    SteeringPassThrough = tk.IntVar()
    SteeringPassthroughCheckbox = tk.Checkbutton(root, text="Steering Passthrough", variable=SteeringPassThrough,command=GUIReadVars, justify=tk.LEFT)
    SteeringPassthroughCheckbox.pack()

    label=tk.Label(root,text="\n Live For Speed max Steering angle:")
    label.pack()

    LFSSteerAngle = tk.IntVar()
    LFSSteerAngleSlider = tk.Scale(root, from_= 1, to= 90, variable=LFSSteerAngle, command=GUIReadVars,orient="horizontal", length=300)
    LFSSteerAngleSlider.pack()

    LFSActualMaxAngleText = tk.StringVar()
    LFSActualMaxAngleOutput = tk.Label(root, textvariable=LFSActualMaxAngleText)
    LFSActualMaxAngleOutput.pack()

    ResetMaxAngleMeasureButton = tk.Button(root, text="Reset", width=5, height=1, command=ResetAngleMeasure)
    ResetMaxAngleMeasureButton.pack()
    ResetMaxAngleMeasureButton.place(x=250, y=100)

    root.resizable(False,False)
    root.after(300, GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1

