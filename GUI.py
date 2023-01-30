import sys
import os
import tkinter as tk

import GUI
from GlobalVars import *
import FileRoutines
import gc
import time
class GUIVars:
    pass

root = tk.Tk()



class GUIFuncs:
    def GUIReadVars(event=None):
        print(GUIVars.SteeringPassThrough.get())
        Settings.Steering.SteeringPassThrough=int(GUIVars.SteeringPassThrough.get())
        Settings.Steering.LFSSteerAngle=GUIVars.LFSSteerAngle.get()
        Settings.Steering.CorrectionFactor=GUIVars.CorrectionFactor.get()
        Settings.Steering.AllowedSlip=GUIVars.AllowedSlip.get()
        Settings.Steering.ActualSteerAngle = GUIVars.ActualSteeringAngle.get()
        Settings.Steering.NonLinearity = GUIVars.NonLinearity.get()

        Settings.Throttle.EnableTC = int(GUIVars.EnableTC.get())
        Settings.Throttle.TCEngageSpeed = GUIVars.TCEngageSpeed.get()
        Settings.Throttle.TCThreshhold = GUIVars.TCThreshhold.get()
        Settings.Throttle.TCMultiplier = GUIVars.TCMultiplier.get()
        Settings.Throttle.Smoothing = GUIVars.TCSmoothing.get()


        Settings.Brakes.EnableBrakeHelp = int(GUIVars.EnableBrakeHelp.get())
        Settings.Brakes.BrakeHelpEngageSpeed = GUIVars.BrakeHelpEngageSpeed.get()
        Settings.Brakes.BrakeHelpThreshhold = GUIVars.BrakeHelpThreshhold.get()
        Settings.Brakes.BrakeHelpMultiplier = GUIVars.BrakeHelpMultiplier.get()
        Settings.Brakes.Smoothing = GUIVars.BrakeSmoothing.get()



    def GUIWrite(event=None):
        GUIVars.LFSActualMaxAngleText.set("Measured Max Angle = " + str(round(InternalVars.LFSMaxMeasuredSteeringAngle * 57.2958,2)) + "            ")

        GUIVars.SteeringPassThrough.set(int(Settings.Steering.SteeringPassThrough))
        GUIVars.LFSSteerAngle.set(Settings.Steering.LFSSteerAngle)
        GUIVars.CorrectionFactor.set(Settings.Steering.CorrectionFactor)
        GUIVars.AllowedSlip.set(Settings.Steering.AllowedSlip)
        GUIVars.ActualSteeringAngle.set(Settings.Steering.ActualSteerAngle)
        GUIVars.NonLinearity.set(Settings.Steering.NonLinearity)

        GUIVars.EnableTC.set(int(Settings.Throttle.EnableTC))
        GUIVars.TCEngageSpeed.set(Settings.Throttle.TCEngageSpeed)
        GUIVars.TCThreshhold.set(Settings.Throttle.TCThreshhold)
        GUIVars.TCMultiplier.set(Settings.Throttle.TCMultiplier)
        GUIVars.TCSmoothing.set(Settings.Throttle.Smoothing)

        GUIVars.EnableBrakeHelp.set(int(Settings.Brakes.EnableBrakeHelp))
        GUIVars.BrakeHelpEngageSpeed.set(Settings.Brakes.BrakeHelpEngageSpeed)
        GUIVars.BrakeHelpThreshhold.set(Settings.Brakes.BrakeHelpThreshhold)
        GUIVars.BrakeHelpMultiplier.set(Settings.Brakes.BrakeHelpMultiplier)
        GUIVars.BrakeSmoothing.set(Settings.Brakes.Smoothing)

        if InternalVars.SetHandbrakeButton == 0:
            GUIVars.ReadGamepadHandBrakeText.set(Settings.Main.HandBrakeButton)
        if InternalVars.ClosingApp !=1:
            root.after(300, GUIFuncs.GUIWrite)


    def ResetAngleMeasure(event=None):
        InternalVars.LFSMaxMeasuredSteeringAngle=0
        GUIFuncs.GUIWrite()

    def ReadGamepadHandBrake(event=None):
        GUIVars.ReadGamepadHandBrakeText.set("Press Gamepad Button")
        InternalVars.SetHandbrakeButton = 1

    def DeleteProfile(event=None):
        chosen = GUIVars.ConfigChoose.get()
        if chosen != "default.cfg" and chosen != "+":
            InternalVars.cfgFiles.remove(chosen)
            os.remove("configs/" + chosen)
            GUIVars.ConfigChooseDropDown.destroy()
            GUIOtherOptions.ConfigChooseDropDown(InternalVars.cfgFiles[0])
    def ConfigChooseDropDown(*args):
        if GUIVars.ConfigChoose.get() == "+":
            def retrieve_input(event=None):
                input = entry.get()
                input = ''.join(c for c in input if c.isalnum())
                input = input + ".cfg"
                FileRoutines.writeconfig(GUIVars.ConfigChoosePrevious.get())
                InternalVars.cfgFiles.append(input)
                GUIVars.ConfigChooseDropDown.destroy()
                GUIOtherOptions.ConfigChooseDropDown(input)
                entry.destroy()
                GUIVars.ProfileButtonText.set("Delete Profile")
                GUIVars.ProfileButton.config(command=GUI.GUIFuncs.DeleteProfile)
            entry = tk.Entry(GUIVars.ProfilesFrame)
            entry.pack(side="left")
            GUIVars.ConfigChooseDropDown.destroy()
            entry.bind('<Return>', retrieve_input)
            GUIVars.ProfileButtonText.set("Enter")
            GUIVars.ProfileButton.config(command = retrieve_input)
        else:
            FileRoutines.writeconfig(GUIVars.ConfigChoosePrevious.get())
            GUIVars.ConfigChoosePrevious.set(GUIVars.ConfigChoose.get())
            FileRoutines.readconfig(GUIVars.ConfigChoose.get())



from GUIHelpers import GUISteering,GUIThrottle,GUIBrakes,GUIOtherOptions

def RunGUI():





    root.geometry("1200x700")
    for i in range(4):
        root.columnconfigure(i, weight=1)

    GUIVars.steering_options_frame = tk.Frame(root)
    GUISteering.GuiSteeringInit()
    GUIVars.steering_options_frame.configure(width=300)
    GUIVars.steering_options_frame.pack()
    GUIVars.steering_options_frame.place(x=0, y=0)

    GUIVars.ThrottleOptionsFrame = tk.Frame(root)
    GUIThrottle.GuiThrottleInit()
    GUIVars.ThrottleOptionsFrame.pack()
    GUIVars.ThrottleOptionsFrame.place(x=302, y=0)

    GUIVars.BrakeOptionsFrame = tk.Frame(root)
    GUIBrakes.GuiBrakesInit()
    GUIVars.BrakeOptionsFrame.pack()
    GUIVars.BrakeOptionsFrame.place(x=604,y=0)


    GUIVars.ProfilesFrame = tk.Frame(root)
    GUIVars.OtherOptionsFrame = tk.Frame(root)
    GUIOtherOptions.GuiOtherOptionsInit()
    GUIVars.OtherOptionsFrame.pack()

    GUIVars.ProfilesFrame.place(x=906,y=0, width=200,height=50)
    GUIVars.OtherOptionsFrame.place(x=906, y=50)

    root.resizable(False,False)
    root.after(300, GUIFuncs.GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1
    FileRoutines.writeconfig(GUIVars.ConfigChoosePrevious.get())

