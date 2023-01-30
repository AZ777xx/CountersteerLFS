from collections import deque

class OutsimData():
    CurrentSlipAngle = 0
    wheelspeed2 = 0
    wheelspeed3 = 0
    wheelspeed0 = 0
    wheelspeed1 = 0
    touchingground0 = 0
    touchingground1 = 0
    wheel0slipangle = 0
    wheel1slipangle = 0
    wheel2slipangle = 0
    wheel3slipangle = 0
    wheel3steer = 0
    wheel2steer = 0
    SlipFraction0=0
    SlipFraction1=0
    SlipFraction2=0
    SlipFraction3=0
    SlipRatio0 = 0
    SlipRatio1 = 0
    SlipRatio2 = 0
    SlipRatio3 = 0

class Settings():
    class Main():
        Patch_LFS_cfg = 1
        LFS_cfg_location = "D:\LFS\cfg.txt"
        HandBrakeButton = "NOT SET"
    class Steering:
        SteeringPassThrough = 0
        LFSSteerAngle = 24
        ActualSteerAngle = 20
        CorrectionFactor = 0.9
        AllowedSlip = 0
        NonLinearity = 1.8
        MinimumSpeedSteerCorrect = 5
    class Throttle:
        EnableTC = 0
        TCEngageSpeed = 15
        TCThreshhold = 5
        TCMultiplier = 20
        Smoothing = 0.01
    class Brakes:
        EnableBrakeHelp = 0
        BrakeHelpEngageSpeed = 15
        BrakeHelpThreshhold=5
        BrakeHelpMultiplier=35
        Smoothing = 0.01


class InternalVars():
    FFB = 0
    cfgFiles = ["default.cfg"]
    CurrentSlipAngle = 0
    LFSMaxMeasuredSteeringAngle = -333
    ClosingApp = 0
    NonLinearSteerValue = 0
    CorrectedSteering=0
    InternalConfigFileError = 0
    RealThrottle = 0
    RealBrake = 0
    CorrectedThrottle = 0
    CorrectedBrake = 0
    timestamped_CorrectedThrottle = deque(maxlen=2500)
    timestamped_CorrectedBrakes = deque(maxlen=2500)
    SetHandbrakeButton = 0
    HandBrakePressed=0

class GamePadData():
    RealGamepadSteer=0
    FakeGamepadFFB=0