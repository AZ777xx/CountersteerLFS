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

        Settings.Throttle.EnableTC = int(EnableTC.get())
        Settings.Throttle.TCEngageSpeed = TCEngageSpeed.get()
        Settings.Throttle.TCThreshhold = TCThreshhold.get()
        Settings.Throttle.TCMultiplier = TCMultiplier.get()
        Settings.Throttle.Smoothing = TCSmoothing.get()


        Settings.Brakes.EnableBrakeHelp = int(EnableBrakeHelp.get())
        Settings.Brakes.BrakeHelpEngageSpeed = BrakeHelpEngageSpeed.get()
        Settings.Brakes.BrakeHelpThreshhold = BrakeHelpThreshhold.get()
        Settings.Brakes.BrakeHelpMultiplier = BrakeHelpMultiplier.get()
        Settings.Brakes.Smoothing = BrakeSmoothing.get()



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

    ThrottleOptionsFrame = tk.Frame(root)

    label = tk.Label(ThrottleOptionsFrame, text="Throttle Help:")
    label.pack()

    EnableTC = tk.BooleanVar()
    EnableTC.set(bool(Settings.Throttle.EnableTC))
    EnableTCCheckbox = tk.Checkbutton(ThrottleOptionsFrame, text="Enable TC",
                                                 variable=EnableTC, command=GUIReadVars)
    EnableTCCheckbox.pack()

    label = tk.Label(ThrottleOptionsFrame, text="\nTC Engage Speed (wheel rotation rad/s):")
    label.pack()

    TCEngageSpeed = tk.DoubleVar()
    TCEngageSpeed.set(Settings.Throttle.TCEngageSpeed)
    TCEngageSpeedSlider = tk.Scale(ThrottleOptionsFrame, from_=0, to=150, resolution=1, variable=TCEngageSpeed,
                                  command=GUIReadVars,
                                  orient="horizontal", length=300)
    TCEngageSpeedSlider.pack()

    label = tk.Label(ThrottleOptionsFrame, text="\nTC Threshhold Slip %:")
    label.pack()

    TCThreshhold = tk.DoubleVar()
    TCThreshhold.set(Settings.Throttle.TCThreshhold)
    TCThreshholdSlider = tk.Scale(ThrottleOptionsFrame, from_=0, to=50, resolution=1, variable=TCThreshhold,
                                   command=GUIReadVars,
                                   orient="horizontal", length=300)
    TCThreshholdSlider.pack()

    label = tk.Label(ThrottleOptionsFrame, text="\nTC Multiplier:")
    label.pack()

    TCMultiplier = tk.DoubleVar()
    TCMultiplier.set(Settings.Throttle.TCMultiplier)
    TCMultiplierSlider = tk.Scale(ThrottleOptionsFrame, from_=0, to=50, resolution=1, variable=TCMultiplier,
                                  command=GUIReadVars,
                                  orient="horizontal", length=300)
    TCMultiplierSlider.pack()

    label = tk.Label(ThrottleOptionsFrame, text="\nTC Smoothing:")
    label.pack()

    TCSmoothing = tk.DoubleVar()
    TCSmoothing.set(Settings.Throttle.Smoothing)
    TCSmoothingSlider = tk.Scale(ThrottleOptionsFrame, from_=0, to=0.5, resolution=0.01, variable=TCSmoothing,
                                  command=GUIReadVars,
                                  orient="horizontal", length=300)
    TCSmoothingSlider.pack()

    ThrottleOptionsFrame.pack()
    ThrottleOptionsFrame.place(x=302, y=0)

    BrakeOptionsFrame = tk.Frame(root)

    label = tk.Label(BrakeOptionsFrame, text="Brake Help:")
    label.pack()

    EnableBrakeHelp = tk.BooleanVar()
    EnableBrakeHelp.set(bool(Settings.Brakes.EnableBrakeHelp))
    EnableBrakeHelpCheckbox = tk.Checkbutton(BrakeOptionsFrame, text="Enable Brake Help",
                                      variable=EnableBrakeHelp, command=GUIReadVars)
    EnableBrakeHelpCheckbox.pack()

    label = tk.Label(BrakeOptionsFrame, text="\nBrake Help Engage Speed (wheel rotation rad/s):")
    label.pack()

    BrakeHelpEngageSpeed = tk.DoubleVar()
    BrakeHelpEngageSpeed.set(Settings.Brakes.BrakeHelpEngageSpeed)
    BrakeHelpEngageSpeedSlider = tk.Scale(BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=BrakeHelpEngageSpeed,
                                   command=GUIReadVars,
                                   orient="horizontal", length=300)
    BrakeHelpEngageSpeedSlider.pack()

    label = tk.Label(BrakeOptionsFrame, text="\nBrake Help Threshhold Slip %:")
    label.pack()

    BrakeHelpThreshhold = tk.DoubleVar()
    BrakeHelpThreshhold.set(Settings.Brakes.BrakeHelpThreshhold)
    BrakeHelpThreshholdSlider = tk.Scale(BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=BrakeHelpThreshhold,
                                  command=GUIReadVars,
                                  orient="horizontal", length=300)
    BrakeHelpThreshholdSlider.pack()

    label = tk.Label(BrakeOptionsFrame, text="\nBrake Help Multiplier:")
    label.pack()

    BrakeHelpMultiplier = tk.DoubleVar()
    BrakeHelpMultiplier.set(Settings.Brakes.BrakeHelpMultiplier)
    BrakeHelpBrakeHelpMultiplierSlider = tk.Scale(BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=BrakeHelpMultiplier,
                           command=GUIReadVars,
                           orient="horizontal", length=300)
    BrakeHelpBrakeHelpMultiplierSlider.pack()


    label = tk.Label(BrakeOptionsFrame, text="\nBrakes Smoothing:")
    label.pack()

    BrakeSmoothing = tk.DoubleVar()
    BrakeSmoothing.set(Settings.Brakes.Smoothing)
    BrakeSmoothingSlider = tk.Scale(BrakeOptionsFrame, from_=0, to=1, resolution=0.01, variable=BrakeSmoothing,
                                  command=GUIReadVars,
                                  orient="horizontal", length=300)
    BrakeSmoothingSlider.pack()

    BrakeOptionsFrame.pack()
    BrakeOptionsFrame.place(x=604,y=0)


    root.resizable(False,False)
    root.after(300, GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1

