import tkinter as tk
from GUI import GUIVars,GUIFuncs
from GUI import root
from GlobalVars import Settings
def GuiBrakesInit():

    label = tk.Label(GUIVars.BrakeOptionsFrame, text="Brake Help:")
    label.pack()

    GUIVars.EnableBrakeHelp = tk.BooleanVar()
    GUIVars.EnableBrakeHelp.set(bool(Settings.Brakes.EnableBrakeHelp))
    GUIVars.EnableBrakeHelpCheckbox = tk.Checkbutton(GUIVars.BrakeOptionsFrame, text="Enable Brake Help",
                                      variable=GUIVars.EnableBrakeHelp, command=GUIFuncs.GUIReadVars)
    GUIVars.EnableBrakeHelpCheckbox.pack()

    label = tk.Label(GUIVars.BrakeOptionsFrame, text="\nBrake Help Engage Speed (wheel rotation rad/s):")
    label.pack()

    GUIVars.BrakeHelpEngageSpeed = tk.DoubleVar()
    GUIVars.BrakeHelpEngageSpeed.set(Settings.Brakes.BrakeHelpEngageSpeed)
    GUIVars.BrakeHelpEngageSpeedSlider = tk.Scale(GUIVars.BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=GUIVars.BrakeHelpEngageSpeed,
                                   command=GUIFuncs.GUIReadVars,
                                   orient="horizontal", length=300)
    GUIVars.BrakeHelpEngageSpeedSlider.pack()

    label = tk.Label(GUIVars.BrakeOptionsFrame, text="\nBrake Help Threshhold Slip %:")
    label.pack()

    GUIVars.BrakeHelpThreshhold = tk.DoubleVar()
    GUIVars.BrakeHelpThreshhold.set(Settings.Brakes.BrakeHelpThreshhold)
    GUIVars.BrakeHelpThreshholdSlider = tk.Scale(GUIVars.BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=GUIVars.BrakeHelpThreshhold,
                                  command=GUIFuncs.GUIReadVars,
                                  orient="horizontal", length=300)
    GUIVars.BrakeHelpThreshholdSlider.pack()

    label = tk.Label(GUIVars.BrakeOptionsFrame, text="\nBrake Help Multiplier:")
    label.pack()

    GUIVars.BrakeHelpMultiplier = tk.DoubleVar()
    GUIVars.BrakeHelpMultiplier.set(Settings.Brakes.BrakeHelpMultiplier)
    GUIVars.BrakeHelpBrakeHelpMultiplierSlider = tk.Scale(GUIVars.BrakeOptionsFrame, from_=0, to=50, resolution=1, variable=GUIVars.BrakeHelpMultiplier,
                           command=GUIFuncs.GUIReadVars,
                           orient="horizontal", length=300)
    GUIVars.BrakeHelpBrakeHelpMultiplierSlider.pack()


    label = tk.Label(GUIVars.BrakeOptionsFrame, text="\nBrakes Smoothing:")
    label.pack()

    GUIVars.BrakeSmoothing = tk.DoubleVar()
    GUIVars.BrakeSmoothing.set(Settings.Brakes.Smoothing)
    GUIVars.BrakeSmoothingSlider = tk.Scale(GUIVars.BrakeOptionsFrame, from_=0, to=1, resolution=0.01, variable=GUIVars.BrakeSmoothing,
                                  command=GUIFuncs.GUIReadVars,
                                  orient="horizontal", length=300)
    GUIVars.BrakeSmoothingSlider.pack()