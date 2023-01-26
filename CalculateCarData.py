import math
from GlobalVars import *
import time
def CalculateCarDataF():
    global OutsimData
    global InternalVars
    global currentSli
    while True:
        """MEASURE MAX STEER ANGLE"""
        tmpMeasureSteerAngle = (abs(OutsimData.wheel3steer)+abs(OutsimData.wheel2steer))/2
        if tmpMeasureSteerAngle > InternalVars.LFSMaxMeasuredSteeringAngle:
            InternalVars.LFSMaxMeasuredSteeringAngle = tmpMeasureSteerAngle

        """MEASURE REAR SLIP ANGLES"""
        currentSlipAngleTMP = 0
        if (OutsimData().wheelspeed3 + OutsimData().wheelspeed2) / 2 > Settings().Steering.MinimumSpeedSteerCorrect:
            currentSlipAngleTMP = (OutsimData().wheel0slipangle * 57.2958 + OutsimData().wheel1slipangle * 57.2958) / 2
        else:
            currentSlipAngleTMP = 0

        if OutsimData().touchingground0 == 0 and OutsimData().touchingground1 == 0:
            currentSlipAngleTMP = 0
        else:
            if OutsimData().touchingground0 == 0 or OutsimData().touchingground1 == 0:
                currentSlipAngleTMP = (
                            OutsimData().wheel0slipangle * 57.2958 * OutsimData().touchingground0 + OutsimData().wheel1slipangle * 57.2958 * OutsimData().touchingground1)

        """Decrease SLIP ANGLE PER SETTINGS"""
        if abs(currentSlipAngleTMP) - Settings().Steering.AllowedSlip < 0:
            currentSlipAngleTMP = 0
        else:
            currentSlipAngleTMP = math.copysign(abs(currentSlipAngleTMP) - Settings().Steering.AllowedSlip,currentSlipAngleTMP)

        InternalVars.CurrentSlipAngle=currentSlipAngleTMP

        """CALCULATE OUTPUT STEERING"""
        CalcCorrectedSteering = Settings().Steering.CorrectionFactor * (-1 * currentSlipAngleTMP / Settings().Steering.LFSSteerAngle)

        CalcCorrectedSteering = float(
            CalcCorrectedSteering * (not bool(Settings.Steering.SteeringPassThrough)) + InternalVars.NonLinearSteerValue * (Settings.Steering.ActualSteerAngle/Settings.Steering.LFSSteerAngle))* (not bool(Settings.Steering.SteeringPassThrough)) + InternalVars.NonLinearSteerValue * bool(Settings.Steering.SteeringPassThrough)

        if abs(CalcCorrectedSteering) > 1:
            CalcCorrectedSteering = math.copysign(1, CalcCorrectedSteering)

        InternalVars.CorrectedSteering = CalcCorrectedSteering
        time.sleep(0.0001)