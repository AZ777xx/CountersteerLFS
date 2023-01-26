import sys
import tkinter as tk
from GlobalVars import *
import gc
import time

def RunGUI():
    def GUIReadVars(event=None):
        print(SteeringPassThrough.get())
        Settings.Steering.SteeringPassThrough=int(SteeringPassThrough.get())
        Settings.Steering.LFSSteerAngle=LFSSteerAngle.get()
        Settings.Steering.CorrectionFactor=CorrectionFactor.get()
        Settings.Steering.AllowedSlip=AllowedSlip.get()
        Settings.Steering.ActualSteerAngle = ActualSteeringAngle.get()
        Settings.Steering.NonLinearity = NonLinearity.get()



    def GUIWrite():
        LFSActualMaxAngleText.set("Measured Max Angle = " + str(round(InternalVars.LFSMaxMeasuredSteeringAngle * 57.2958,2)) + "            ")
        LFSSteerAngle.set(Settings.Steering.LFSSteerAngle)
        if InternalVars.ClosingApp !=1:
            root.after(300, GUIWrite)


    def ResetAngleMeasure(event=None):
        InternalVars.LFSMaxMeasuredSteeringAngle=0
        GUIWrite()



    root = tk.Tk()
    root.geometry("1200x700")
    for i in range(4):
        root.columnconfigure(i, weight=1)

    steering_options_frame =tk.Frame(root)

    SteeringPassThrough = tk.BooleanVar()
    SteeringPassThrough.set(bool(Settings.Steering.SteeringPassThrough))
    SteeringPassthroughCheckbox = tk.Checkbutton(steering_options_frame, text="Steering Passthrough", variable=SteeringPassThrough,command=GUIReadVars, justify=tk.LEFT)
    SteeringPassthroughCheckbox.pack()

    label=tk.Label(steering_options_frame,text="\n Live For Speed max Steering angle:")
    label.pack()

    LFSSteerAngle = tk.IntVar()
    LFSSteerAngle.set(Settings.Steering.LFSSteerAngle)
    LFSSteerAngleSlider = tk.Scale(steering_options_frame, from_= 1, to= 90, variable=LFSSteerAngle, command=GUIReadVars,orient="horizontal", length=300)
    LFSSteerAngleSlider.pack()

    LFSActualMaxAngleText = tk.StringVar()
    LFSActualMaxAngleOutput = tk.Label(steering_options_frame, textvariable=LFSActualMaxAngleText)
    LFSActualMaxAngleOutput.pack()

    ResetMaxAngleMeasureButton = tk.Button(steering_options_frame, text="Reset", width=5, height=1, command=ResetAngleMeasure)
    ResetMaxAngleMeasureButton.pack()
    ResetMaxAngleMeasureButton.place(x=250, y=100)

    label = tk.Label(steering_options_frame, text="\n Actual Steering Angle:")
    label.pack()

    ActualSteeringAngle = tk.IntVar()
    ActualSteeringAngle.set(Settings.Steering.ActualSteerAngle)
    ActualSteeringAngleSlider = tk.Scale(steering_options_frame, from_=1, to=90, variable=ActualSteeringAngle,
                                      command=GUIReadVars,
                                      orient="horizontal", length=300)
    ActualSteeringAngleSlider.pack()

    label = tk.Label(steering_options_frame, text="\n NonLinear Steering:")
    label.pack()

    NonLinearity = tk.DoubleVar()
    NonLinearity.set(Settings.Steering.NonLinearity)
    NonLinearitySlider = tk.Scale(steering_options_frame, from_=0, to=3,resolution=0.05, variable=NonLinearity,
                                         command=GUIReadVars,
                                         orient="horizontal", length=300)
    NonLinearitySlider.pack()


    label = tk.Label(steering_options_frame, text="\n CorrectionFactor:")
    label.pack()
    CorrectionFactor = tk.DoubleVar()
    CorrectionFactor.set(Settings.Steering.CorrectionFactor)
    CorrectionFactorSlider = tk.Scale(steering_options_frame, from_=0.1, to=2, variable=CorrectionFactor,resolution=0.05, command=GUIReadVars,
                                   orient="horizontal", length=300)
    CorrectionFactorSlider.pack()

    label = tk.Label(steering_options_frame, text="\n Allowed Slip Angle:")
    label.pack()

    AllowedSlip = tk.DoubleVar()
    AllowedSlip.set(Settings.Steering.AllowedSlip)
    AllowedSlipSlider = tk.Scale(steering_options_frame, from_=0, to=20, variable=AllowedSlip,resolution=0.1, command=GUIReadVars,
                                   orient="horizontal", length=300)
    AllowedSlipSlider.pack()
    steering_options_frame.configure(width=300)
    steering_options_frame.pack()
    steering_options_frame.place(x=0, y=0)

    root.resizable(False,False)
    root.after(300, GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1

