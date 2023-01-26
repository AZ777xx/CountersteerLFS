import math

import GlobalVars
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

        if bool(Settings.Throttle.EnableTC) == True:
            TMP_CorrectedThrottle = GlobalVars.InternalVars.RealThrottle
            MeanWheelSpeed = (OutsimData.wheelspeed0 +OutsimData.wheelspeed1 +OutsimData.wheelspeed2 +OutsimData.wheelspeed3 )/4
            if MeanWheelSpeed > Settings.Throttle.TCEngageSpeed:
                WheelSpeedArray = [OutsimData.wheelspeed0, OutsimData.wheelspeed1, OutsimData.wheelspeed2, OutsimData.wheelspeed3]
                WheelSpeedArraySorted = sorted(WheelSpeedArray)
                WheelSpeedDifference = abs(WheelSpeedArraySorted[0]-WheelSpeedArraySorted[3])
                #print(WheelSpeedDifference)
                if WheelSpeedDifference > Settings.Throttle.TCThreshhold:
                    ThrottleReduceFactor = 1-( (WheelSpeedDifference- Settings.Throttle.TCThreshhold) / Settings.Throttle.TCMax)
                    if ThrottleReduceFactor >1:
                        ThrottleReduceFactor = 1
                    if ThrottleReduceFactor <0:
                        ThrottleReduceFactor=0
                    TMP_CorrectedThrottle = InternalVars.RealThrottle * ThrottleReduceFactor
            GlobalVars.InternalVars.CorrectedThrottle = TMP_CorrectedThrottle
        else:
            GlobalVars.InternalVars.CorrectedThrottle = GlobalVars.InternalVars.RealThrottle

           # print (TMP_CorrectedThrottle)
        if bool(Settings.Brakes.EnableBrakeHelp) == True:
            TMP_CorrectedBrake = GlobalVars.InternalVars.RealBrake
            MeanWheelSpeed = (OutsimData.wheelspeed0 + OutsimData.wheelspeed1 + OutsimData.wheelspeed2 + OutsimData.wheelspeed3) / 4
            if MeanWheelSpeed > Settings.Brakes.BrakeHelpEngageSpeed:
                WheelSpeedArray = [OutsimData.wheelspeed0, OutsimData.wheelspeed1, OutsimData.wheelspeed2,
                                   OutsimData.wheelspeed3]
                WheelSpeedArraySorted = sorted(WheelSpeedArray)
                WheelSpeedDifference = abs(WheelSpeedArraySorted[0] - WheelSpeedArraySorted[3])
                #print(WheelSpeedDifference)
                if WheelSpeedDifference > Settings.Brakes.BrakeHelpThreshhold:
                    BrakeReduceFactor = 1 - (
                                (WheelSpeedDifference - Settings.Brakes.BrakeHelpThreshhold) / Settings.Brakes.BrakeHelpMax)
                    if BrakeReduceFactor > 1:
                        BrakeReduceFactor = 1
                    if BrakeReduceFactor < 0:
                        BrakeReduceFactor = 0
                    TMP_CorrectedBrake = InternalVars.RealBrake * BrakeReduceFactor
            GlobalVars.InternalVars.CorrectedBrake = TMP_CorrectedBrake


        else:
            GlobalVars.InternalVars.CorrectedBrake = GlobalVars.InternalVars.RealBrake

        time.sleep(0.0001)