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
    CorrectionFactor = 0.9
    AllowedSlip = 0
    NonLinearity = 1.8
    MinimumSpeedSteerCorrect = 5


class InternalVars():
    FFB = 0
    CurrentSlipAngle = 0
    LFSMaxMeasuredSteeringAngle = -333
    ClosingApp = 0