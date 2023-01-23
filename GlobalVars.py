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


class Settings():
    SteeringPassThrough = 0
    LFSSteerAngle = 24
    ActualSteerAngle= 20
    CorrectionFactor = 0.9
    AllowedSlip = 0
    NonLinearity = 1.8
    MinimumSpeedSteerCorrect = 5
    Patch_LFS_cfg = 1
    LFS_cfg_location = "D:\LFS\cfg.txt"



class InternalVars():
    FFB = 0
    CurrentSlipAngle = 0
    LFSMaxMeasuredSteeringAngle = -333
    ClosingApp = 0
    NonLinearSteerValue = 0
    CorrectedSteering=0
    InternalConfigFileError = 0

class GamePadData():
    RealGamepadSteer=0
    FakeGamepadFFB=0