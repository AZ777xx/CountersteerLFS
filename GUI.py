import sys
import tkinter as tk
from GlobalVars import *
import gc
import time

def RunGUI():
    def GUIReadVars(event=None):
        print(SteeringPassThrough.get())
        Settings.SteeringPassThrough=int(SteeringPassThrough.get())
        Settings.LFSSteerAngle=LFSSteerAngle.get()
        Settings.CorrectionFactor=CorrectionFactor.get()
        Settings.AllowedSlip=AllowedSlip.get()
        Settings.ActualSteerAngle = ActualSteeringAngle.get()
        Settings.NonLinearity = NonLinearity.get()



    def GUIWrite():
        LFSActualMaxAngleText.set("Measured Max Angle = " + str(round(InternalVars.LFSMaxMeasuredSteeringAngle * 57.2958,2)) + "            ")
        LFSSteerAngle.set(Settings.LFSSteerAngle)
        if InternalVars.ClosingApp !=1:
            root.after(300, GUIWrite)


    def ResetAngleMeasure(event=None):
        InternalVars.LFSMaxMeasuredSteeringAngle=0
        GUIWrite()



    root = tk.Tk()
    root.geometry("300x800")

    SteeringPassThrough = tk.BooleanVar()
    SteeringPassThrough.set(bool(Settings.SteeringPassThrough))
    SteeringPassthroughCheckbox = tk.Checkbutton(root, text="Steering Passthrough", variable=SteeringPassThrough,command=GUIReadVars, justify=tk.LEFT)
    SteeringPassthroughCheckbox.pack()

    label=tk.Label(root,text="\n Live For Speed max Steering angle:")
    label.pack()

    LFSSteerAngle = tk.IntVar()
    LFSSteerAngle.set(Settings.LFSSteerAngle)
    LFSSteerAngleSlider = tk.Scale(root, from_= 1, to= 90, variable=LFSSteerAngle, command=GUIReadVars,orient="horizontal", length=300)
    LFSSteerAngleSlider.pack()

    LFSActualMaxAngleText = tk.StringVar()
    LFSActualMaxAngleOutput = tk.Label(root, textvariable=LFSActualMaxAngleText)
    LFSActualMaxAngleOutput.pack()

    ResetMaxAngleMeasureButton = tk.Button(root, text="Reset", width=5, height=1, command=ResetAngleMeasure)
    ResetMaxAngleMeasureButton.pack()
    ResetMaxAngleMeasureButton.place(x=250, y=100)

    label = tk.Label(root, text="\n Actual Steering Angle:")
    label.pack()

    ActualSteeringAngle = tk.IntVar()
    ActualSteeringAngle.set(Settings.ActualSteerAngle)
    ActualSteeringAngleSlider = tk.Scale(root, from_=1, to=90, variable=ActualSteeringAngle,
                                      command=GUIReadVars,
                                      orient="horizontal", length=300)
    ActualSteeringAngleSlider.pack()

    label = tk.Label(root, text="\n NonLinear Steering:")
    label.pack()

    NonLinearity = tk.DoubleVar()
    NonLinearity.set(Settings.NonLinearity)
    NonLinearitySlider = tk.Scale(root, from_=0, to=3,resolution=0.05, variable=NonLinearity,
                                         command=GUIReadVars,
                                         orient="horizontal", length=300)
    NonLinearitySlider.pack()


    label = tk.Label(root, text="\n CorrectionFactor:")
    label.pack()
    CorrectionFactor = tk.DoubleVar()
    CorrectionFactor.set(Settings.CorrectionFactor)
    CorrectionFactorSlider = tk.Scale(root, from_=0.1, to=2, variable=CorrectionFactor,resolution=0.05, command=GUIReadVars,
                                   orient="horizontal", length=300)
    CorrectionFactorSlider.pack()

    label = tk.Label(root, text="\n Allowed Slip Angle:")
    label.pack()

    AllowedSlip = tk.DoubleVar()
    AllowedSlip.set(Settings.AllowedSlip)
    AllowedSlipSlider = tk.Scale(root, from_=0, to=20, variable=AllowedSlip,resolution=0.1, command=GUIReadVars,
                                   orient="horizontal", length=300)
    AllowedSlipSlider.pack()

    root.resizable(False,False)
    root.after(300, GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1

