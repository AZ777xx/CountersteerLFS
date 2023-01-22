import math
from GlobalVars import *
import time
def CalculateCarDataF():
    global OutsimData
    global InternalVars
    global currentSli
    while True:

        tmpMeasureSteerAngle = abs(OutsimData.wheel3steer)
        if tmpMeasureSteerAngle < abs(OutsimData.wheel2steer):
            tmpMeasureSteerAngle = abs(OutsimData.wheel2steer)
        if tmpMeasureSteerAngle > InternalVars.LFSMaxMeasuredSteeringAngle:
            InternalVars.LFSMaxMeasuredSteeringAngle = tmpMeasureSteerAngle

        currentSlipAngleTMP = 0
        if (OutsimData().wheelspeed3 + OutsimData().wheelspeed2) / 2 > Settings().MinimumSpeedSteerCorrect:
            currentSlipAngleTMP = (OutsimData().wheel0slipangle * 57.2958 + OutsimData().wheel1slipangle * 57.2958) / 2
        else:
            currentSlipAngleTMP = 0

        if OutsimData().touchingground0 == 0 and OutsimData().touchingground1 == 0:
            currentSlipAngleTMP = 0
        else:
            if OutsimData().touchingground0 == 0 or OutsimData().touchingground1 == 0:
                currentSlipAngleTMP = (
                            OutsimData().wheel0slipangle * 57.2958 * OutsimData().touchingground0 + OutsimData().wheel1slipangle * 57.2958 * OutsimData().touchingground1)
        # print("updatecontrolchanges",OutsimData().wheelspeed3)
        InternalVars.CurrentSlipAngle = currentSlipAngleTMP
        print("TMP= ", currentSlipAngleTMP, "Intern= ", InternalVars.CurrentSlipAngle)

        calculateSlipAngle = 0
        if abs(InternalVars.CurrentSlipAngle) - Settings().AllowedSlip < 0:
            calculateSlipAngle = 0
        else:
            calculateSlipAngle = math.copysign(abs(InternalVars.CurrentSlipAngle) - Settings().AllowedSlip,
                                               InternalVars.CurrentSlipAngle)

        CalcCorrectedSteering = Settings().CorrectionFactor * (-1 * calculateSlipAngle / Settings().LFSSteerAngle)

        CalcCorrectedSteering = float(
            CalcCorrectedSteering * (not bool(Settings.SteeringPassThrough)) + InternalVars.NonLinearSteerValue)

        if abs(CalcCorrectedSteering) > 1:
            CalcCorrectedSteering = math.copysign(1, CalcCorrectedSteering)

        InternalVars.CorrectedSteering = CalcCorrectedSteering
        time.sleep(0.01)