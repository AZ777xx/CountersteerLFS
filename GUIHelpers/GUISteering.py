import tkinter as tk
from GUI import GUIVars,GUIFuncs
from GUI import root
from GlobalVars import Settings

def GuiSteeringInit():

    GUIVars.SteeringPassThrough = tk.BooleanVar()
    GUIVars.SteeringPassThrough.set(bool(Settings.Steering.SteeringPassThrough))
    GUIVars.SteeringPassthroughCheckbox = tk.Checkbutton(GUIVars.steering_options_frame, text="Steering Passthrough", variable=GUIVars.SteeringPassThrough,command=GUIFuncs.GUIReadVars, justify=tk.LEFT)
    GUIVars.SteeringPassthroughCheckbox.pack()

    label=tk.Label(GUIVars.steering_options_frame,text="\n Live For Speed max Steering angle:")
    label.pack()

    GUIVars.LFSSteerAngle = tk.IntVar()
    GUIVars.LFSSteerAngle.set(Settings.Steering.LFSSteerAngle)
    GUIVars.LFSSteerAngleSlider = tk.Scale(GUIVars.steering_options_frame, from_= 1, to= 90, variable=GUIVars.LFSSteerAngle, command=GUIFuncs.GUIReadVars,orient="horizontal", length=300)
    GUIVars.LFSSteerAngleSlider.pack()

    GUIVars.LFSActualMaxAngleText = tk.StringVar()
    GUIVars.LFSActualMaxAngleOutput = tk.Label(GUIVars.steering_options_frame, textvariable=GUIVars.LFSActualMaxAngleText)
    GUIVars.LFSActualMaxAngleOutput.pack()

    GUIVars.ResetMaxAngleMeasureButton = tk.Button(GUIVars.steering_options_frame, text="Reset", width=5, height=1, command=GUIFuncs.ResetAngleMeasure)
    GUIVars.ResetMaxAngleMeasureButton.pack()
    GUIVars.ResetMaxAngleMeasureButton.place(x=250, y=100)

    GUIVars.label = tk.Label(GUIVars.steering_options_frame, text="\n Actual Steering Angle:")
    GUIVars.label.pack()

    GUIVars.ActualSteeringAngle = tk.IntVar()
    GUIVars.ActualSteeringAngle.set(Settings.Steering.ActualSteerAngle)
    GUIVars.ActualSteeringAngleSlider = tk.Scale(GUIVars.steering_options_frame, from_=1, to=90, variable=GUIVars.ActualSteeringAngle,
                                      command=GUIFuncs.GUIReadVars,
                                      orient="horizontal", length=300)
    GUIVars.ActualSteeringAngleSlider.pack()

    GUIVars.label = tk.Label(GUIVars.steering_options_frame, text="\n NonLinear Steering:")
    GUIVars.label.pack()

    GUIVars.NonLinearity = tk.DoubleVar()
    GUIVars.NonLinearity.set(Settings.Steering.NonLinearity)
    GUIVars.NonLinearitySlider = tk.Scale(GUIVars.steering_options_frame, from_=0, to=3,resolution=0.05, variable=GUIVars.NonLinearity,
                                         command=GUIFuncs.GUIReadVars,
                                         orient="horizontal", length=300)
    GUIVars.NonLinearitySlider.pack()


    GUIVars.label = tk.Label(GUIVars.steering_options_frame, text="\n CorrectionFactor:")
    GUIVars.label.pack()
    GUIVars.CorrectionFactor = tk.DoubleVar()
    GUIVars.CorrectionFactor.set(Settings.Steering.CorrectionFactor)
    GUIVars.CorrectionFactorSlider = tk.Scale(GUIVars.steering_options_frame, from_=0.1, to=2, variable=GUIVars.CorrectionFactor,resolution=0.05, command=GUIFuncs.GUIReadVars,
                                   orient="horizontal", length=300)
    GUIVars.CorrectionFactorSlider.pack()

    label = tk.Label(GUIVars.steering_options_frame, text="\n Allowed Slip Angle:")
    label.pack()

    GUIVars.AllowedSlip = tk.DoubleVar()
    GUIVars.AllowedSlip.set(Settings.Steering.AllowedSlip)
    GUIVars.AllowedSlipSlider = tk.Scale(GUIVars.steering_options_frame, from_=0, to=20, variable=GUIVars.AllowedSlip,resolution=0.1, command=GUIFuncs.GUIReadVars,
                                   orient="horizontal", length=300)
    GUIVars.AllowedSlipSlider.pack()