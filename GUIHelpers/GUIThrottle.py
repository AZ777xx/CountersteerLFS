import tkinter as tk
from GUI import GUIVars,GUIFuncs
from GUI import root
from GlobalVars import Settings
def GuiThrottleInit():
    label = tk.Label(GUIVars.ThrottleOptionsFrame, text="Throttle Help:")
    label.pack()

    GUIVars.EnableTC = tk.BooleanVar()
    GUIVars.EnableTC.set(bool(Settings.Throttle.EnableTC))
    GUIVars.EnableTCCheckbox = tk.Checkbutton(GUIVars.ThrottleOptionsFrame, text="Enable TC",
                                      variable=GUIVars.EnableTC, command=GUIFuncs.GUIReadVars)
    GUIVars.EnableTCCheckbox.pack()

    label = tk.Label(GUIVars.ThrottleOptionsFrame, text="\nTC Engage Speed (wheel rotation rad/s):")
    label.pack()

    GUIVars.TCEngageSpeed = tk.DoubleVar()
    GUIVars.TCEngageSpeed.set(Settings.Throttle.TCEngageSpeed)
    GUIVars.TCEngageSpeedSlider = tk.Scale(GUIVars.ThrottleOptionsFrame, from_=0, to=150, resolution=1, variable=GUIVars.TCEngageSpeed,
                                   command=GUIFuncs.GUIReadVars,
                                   orient="horizontal", length=300)
    GUIVars.TCEngageSpeedSlider.pack()

    label = tk.Label(GUIVars.ThrottleOptionsFrame, text="\nTC Threshhold Slip %:")
    label.pack()

    GUIVars.TCThreshhold = tk.DoubleVar()
    GUIVars.TCThreshhold.set(Settings.Throttle.TCThreshhold)
    GUIVars.TCThreshholdSlider = tk.Scale(GUIVars.ThrottleOptionsFrame, from_=0, to=50, resolution=1, variable=GUIVars.TCThreshhold,
                                  command=GUIFuncs.GUIReadVars,
                                  orient="horizontal", length=300)
    GUIVars.TCThreshholdSlider.pack()

    label = tk.Label(GUIVars.ThrottleOptionsFrame, text="\nTC Multiplier:")
    label.pack()

    GUIVars.TCMultiplier = tk.DoubleVar()
    GUIVars.TCMultiplier.set(Settings.Throttle.TCMultiplier)
    GUIVars.TCMultiplierSlider = tk.Scale(GUIVars.ThrottleOptionsFrame, from_=0, to=50, resolution=1, variable=GUIVars.TCMultiplier,
                                  command=GUIFuncs.GUIReadVars,
                                  orient="horizontal", length=300)
    GUIVars.TCMultiplierSlider.pack()

    label = tk.Label(GUIVars.ThrottleOptionsFrame, text="\nTC Smoothing:")
    label.pack()

    GUIVars.TCSmoothing = tk.DoubleVar()
    GUIVars.TCSmoothing.set(Settings.Throttle.Smoothing)
    GUIVars.TCSmoothingSlider = tk.Scale(GUIVars.ThrottleOptionsFrame, from_=0, to=0.5, resolution=0.01, variable=GUIVars.TCSmoothing,
                                 command=GUIFuncs.GUIReadVars,
                                 orient="horizontal", length=300)
    GUIVars.TCSmoothingSlider.pack()