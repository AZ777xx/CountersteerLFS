import tkinter as tk
from GUI import GUIVars,GUIFuncs
from GUI import root
from GlobalVars import Settings

def GuiOtherOptionsInit():
    label = tk.Label(GUIVars.OtherOptionsFrame, text="Set Handbrake Button:")
    label.pack()

    GUIVars.ReadGamepadHandBrakeText =  tk.StringVar()
    GUIVars.ReadGamepadHandBrakeText.set(Settings.Main.HandBrakeButton)
    GUIVars.ReadGamepadHandBrake = tk.Button(GUIVars.OtherOptionsFrame, textvariable=GUIVars.ReadGamepadHandBrakeText, width=30, height=1,
                                                   command=GUIFuncs.ReadGamepadHandBrake)
    GUIVars.ReadGamepadHandBrake.pack()
    GUIVars.ReadGamepadHandBrake.place()