import math
import threading
import GlobalVars
from GlobalVars import *
import time
import statistics
from collections import deque

def mean_of_last_time(values: deque,seconds):
    current_time = time.time()
    while values and current_time - values[0][1] > seconds:
        values.popleft()
    last_second_values = [x[0] for x in values]
    return sum(last_second_values)/len(last_second_values) if last_second_values else 0

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

            SlipRatio0 = abs(OutsimData.SlipRatio0)
            SlipRatio1 = abs(OutsimData.SlipRatio1)
            SlipRatio2 = abs(OutsimData.SlipRatio2)
            SlipRatio3 = abs(OutsimData.SlipRatio3)
            ThrottleReduceFactor=0
            ThrottleReduceFactorR =1-Settings.Throttle.TCMultiplier*( ((abs(SlipRatio1) + abs(SlipRatio0))/2) - (Settings.Throttle.TCThreshhold/100))
            ThrottleReduceFactorF = 1 - Settings.Throttle.TCMultiplier * (
                        ((abs(SlipRatio2) + abs(SlipRatio3)) / 2) - Settings.Throttle.TCThreshhold / 100)
            if ThrottleReduceFactorF < ThrottleReduceFactorR:
                ThrottleReduceFactor=ThrottleReduceFactorF
            else:
                ThrottleReduceFactor=ThrottleReduceFactorR
            #print(ThrottleReduceFactor)
           # ThrottleReduceFactor = 1-( (WheelSpeedDifference- Settings.Throttle.TCThreshhold) / Settings.Throttle.TCMax)
            if abs(OutsimData.wheelspeed0 + OutsimData.wheelspeed1 + OutsimData.wheelspeed2 + OutsimData.wheelspeed3) /4 < Settings.Throttle.TCEngageSpeed:
                ThrottleReduceFactor=1

            if ThrottleReduceFactor >1:
                ThrottleReduceFactor = 1
            if ThrottleReduceFactor <0:
                ThrottleReduceFactor=0

            InternalVars.timestamped_CorrectedThrottle.append((ThrottleReduceFactor,time.time()))
            MeanThrottleReduceFactor = mean_of_last_time(InternalVars.timestamped_CorrectedThrottle , Settings.Throttle.Smoothing)
            TMP_CorrectedThrottle = InternalVars.RealThrottle * MeanThrottleReduceFactor
            GlobalVars.InternalVars.CorrectedThrottle = TMP_CorrectedThrottle
        else:
            GlobalVars.InternalVars.CorrectedThrottle = GlobalVars.InternalVars.RealThrottle

           # print (TMP_CorrectedThrottle)
        if bool(Settings.Brakes.EnableBrakeHelp) == True:
            TMP_CorrectedBrake = GlobalVars.InternalVars.RealBrake
            SlipRatio0 = abs(OutsimData.SlipRatio0)
            SlipRatio1 = abs(OutsimData.SlipRatio1)
            SlipRatio2 = abs(OutsimData.SlipRatio2)
            SlipRatio3 = abs(OutsimData.SlipRatio3)
            BrakeReduceFactor = 0
            BrakeReduceFactorF = 1 - Settings.Brakes.BrakeHelpMultiplier * (((abs(SlipRatio2) + abs(SlipRatio3)) / 2) - Settings.Brakes.BrakeHelpThreshhold/100)
            BrakeReduceFactorR = 1 - Settings.Brakes.BrakeHelpMultiplier * (
                        ((abs(SlipRatio0) + abs(SlipRatio1)) / 2) - Settings.Brakes.BrakeHelpThreshhold / 100)
            if BrakeReduceFactorF < BrakeReduceFactorR:
                BrakeReduceFactor = BrakeReduceFactorF
            else:
                BrakeReduceFactor = BrakeReduceFactorR
            print(BrakeReduceFactorR)
            if abs(OutsimData.wheelspeed0 + OutsimData.wheelspeed1 + OutsimData.wheelspeed2 + OutsimData.wheelspeed3) /4 < Settings.Brakes.BrakeHelpEngageSpeed:
                BrakeReduceFactor=1

            if BrakeReduceFactor > 1:
                BrakeReduceFactor = 1
            if BrakeReduceFactor < 0:
                BrakeReduceFactor = 0
            InternalVars.timestamped_CorrectedBrakes.append((BrakeReduceFactor, time.time()))
            MeanBrakeReduceFactor = mean_of_last_time(InternalVars.timestamped_CorrectedBrakes,
                                                         Settings.Brakes.Smoothing)
            TMP_CorrectedBrake= InternalVars.RealBrake * MeanBrakeReduceFactor
            GlobalVars.InternalVars.CorrectedBrake = TMP_CorrectedBrake


        else:
            GlobalVars.InternalVars.CorrectedBrake = GlobalVars.InternalVars.RealBrake

        time.sleep(0.0001)