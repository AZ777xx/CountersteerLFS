import sys
import tkinter as tk
from GlobalVars import *
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
        GUIVars.LFSSteerAngle.set(Settings.Steering.LFSSteerAngle)
        if InternalVars.ClosingApp !=1:
            root.after(300, GUIFuncs.GUIWrite)


    def ResetAngleMeasure(event=None):
        InternalVars.LFSMaxMeasuredSteeringAngle=0
        GUIFuncs.GUIWrite()


from GUIHelpers import GUISteering,GUIThrottle,GUIBrakes

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


    root.resizable(False,False)
    root.after(300, GUIFuncs.GUIWrite)
    root.mainloop()
    root.quit()
    InternalVars.ClosingApp = 1

