import tkinter as tk

import GlobalVars
from GUI import GUIVars,GUIFuncs
from GUI import root
from GlobalVars import Settings
def ConfigChooseDropDown(CurrentConfig):
    GUIVars.ConfigChoose = tk.StringVar()
    GUIVars.ConfigChoosePrevious = tk.StringVar()
    GUIVars.ConfigChoose.set(CurrentConfig)
    GUIVars.ConfigChoosePrevious.set(CurrentConfig)
    GUIVars.ConfigChoose.trace("w", GUIFuncs.ConfigChooseDropDown)
    GUIVars.ConfigChooseDropDown = tk.OptionMenu(GUIVars.ProfilesFrame, GUIVars.ConfigChoose,
                                                 *GlobalVars.InternalVars.cfgFiles, "+")
    GUIVars.ConfigChooseDropDown.configure(width=10)
    GUIVars.ConfigChooseDropDown.pack(side="left")
def GuiOtherOptionsInit():
    label = tk.Label(GUIVars.ProfilesFrame, text="Profile:")
    label.pack()
    ConfigChooseDropDown(GlobalVars.InternalVars.cfgFiles[0])

    GUIVars.ProfileButtonText = tk.StringVar()
    GUIVars.ProfileButtonText.set("Delete Profile")
    GUIVars.ProfileButton = tk.Button(GUIVars.ProfilesFrame, textvariable=GUIVars.ProfileButtonText,
                                             height=1,
                                             command=GUIFuncs.DeleteProfile)
    GUIVars.ProfileButton.pack(side="right")
   # GUIVars.DeleteProfileButton.configure(width=10)

    label = tk.Label(GUIVars.OtherOptionsFrame, text="Set Handbrake Button:")
    label.pack()



    GUIVars.ReadGamepadHandBrakeText =  tk.StringVar()
    GUIVars.ReadGamepadHandBrakeText.set(Settings.Main.HandBrakeButton)
    GUIVars.ReadGamepadHandBrake = tk.Button(GUIVars.OtherOptionsFrame, textvariable=GUIVars.ReadGamepadHandBrakeText, width=30, height=1,
                                                   command=GUIFuncs.ReadGamepadHandBrake)
    GUIVars.ReadGamepadHandBrake.pack()
    GUIVars.ReadGamepadHandBrake.place()