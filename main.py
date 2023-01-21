# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
OutSim Mode 2
OutSim Delay 5
OutSim IP 127.0.0.1
OutSim Port 30000
OutSim ID 0
OutSim Opts 80
"""
import vgamepad as vg
import XInput
import time
import math
import socket
import struct
import threading
from GlobalVars import *

LFSSteerAngle = 24
CorrectionFactor = 0.9
AllowedSlip = 0
OverSteer = 0.5
UnderSteer = 1.25
NonLinearity = 1.8
MinimumSpeedSteerCorrect=5
def weird_division(n, d):
    return n / d if d else 0
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
FFB = 0
def my_callback(client, target, large_motor, small_motor, led_number, user_data):
    """
    Callback function triggered at each received state change

    :param client: vigem bus ID
    :param target: vigem device ID
    :param large_motor: integer in [0, 255] representing the state of the large motor
    :param small_motor: integer in [0, 255] representing the state of the small motor
    :param led_number: integer in [0, 255] representing the state of the LED ring
    :param user_data: placeholder, do not use
    """
    global FFB
    # Do your things here. For instance:
    FFB = small_motor
   # print(f"Received notification for client {client}, target {target}")
   # print(f"large motor: {large_motor}, small motor: {small_motor}")
 #   print(f"led number: {led_number}")
CurrentSlipAngle = 0
PrevSlipAngle = 0
LastChangeTime = time.time()
def GetOutsimData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 30000))
    sock.settimeout(0.2)
    global OutsimData
    while True:
        try:
            data = sock.recv(280)
        except:
            data = None
        if not data:
           CurrentSlipAngle = 0
        else:
            # print(data)
            outsim_pack = struct.unpack("7f4b2f7f4b2f7f4b2f7f4b2f", data)
            OutsimData.wheel0slipangle = outsim_pack[12]
            OutsimData.wheel1slipangle = outsim_pack[25]
            OutsimData.wheel2slipangle = outsim_pack[38]
            OutsimData.wheel3slipangle = outsim_pack[51]
            OutsimData.wheelspeed2 = outsim_pack[31]
            OutsimData.wheelspeed3 = outsim_pack[44]
            OutsimData.touchingground0 = outsim_pack[9]
            OutsimData.touchingground1 = outsim_pack[22]
            #print("outsimdata", OutsimData.wheelspeed3)

def UpdateControlChanges():
    global OutsimData
    global CurrentSlipAngle
    print(str(OutsimData.wheelspeed3))
    OutsimData().wheelspeed3=333
    while True:
        if (OutsimData().wheelspeed3 + OutsimData().wheelspeed2) / 2 > MinimumSpeedSteerCorrect:
            currentSlipAngleTMP = (OutsimData().wheel0slipangle * 57.2958 + OutsimData().wheel1slipangle * 57.2958) / 2
        else:
            currentSlipAngleTMP = 0

        if OutsimData().touchingground0 == 0 and OutsimData().touchingground1 == 0:
            currentSlipAngleTMP = 0
        else:
            if OutsimData().touchingground0 == 0 or OutsimData().touchingground1 == 0:
                CurrentSlipAngleTMP = (OutsimData().wheel0slipangle * 57.2958 * OutsimData().touchingground0 + OutsimData().wheel1slipangle * 57.2958 * OutsimData().touchingground1)
        print("updatecontrolchanges",OutsimData().wheelspeed3)
        CurrentSlipAngle = currentSlipAngleTMP


if __name__ == '__main__':
    time.sleep(1)
    OutSimThread = threading.Thread(target=GetOutsimData)
    UpdateControlChangesThread = threading.Thread(target=UpdateControlChanges)
    print(777)
    OutSimThread.start()
    UpdateControlChangesThread.start()
    laststeervalue = 0
    NonLinearSteerValue=0
    XInput.set_deadzone(XInput.DEADZONE_LEFT_THUMB, 0)
    print_hi('PyCharm')
    gamepad = vg.VX360Gamepad()
    time.sleep(1)


    gamepad.register_notification(callback_function=my_callback)
    print(XInput.get_connected())
    print(str((XInput.get_state(0))))
    state_0 = XInput.get_state(0)
    #XInput.get_trigger_values(state_0)
    FFBtest = 0
    while True:
       # print(laststeervalue)



        #print("\r", CurrentSlipAngle, end="")
        CalculateSlipAngle=0
        if abs(CurrentSlipAngle) - AllowedSlip <0:
            CalculateSlipAngle = 0
        else:
            CalculateSlipAngle = math.copysign(abs(CurrentSlipAngle)-AllowedSlip,CurrentSlipAngle)

        CalcCorrectedSteering = CorrectionFactor * (-1*CalculateSlipAngle / LFSSteerAngle)
        if math.copysign(1,CalcCorrectedSteering) == math.copysign(1,NonLinearSteerValue):
            CorrectedSteering = CalcCorrectedSteering + NonLinearSteerValue* UnderSteer
        else:
            CorrectedSteering = CalcCorrectedSteering + NonLinearSteerValue * OverSteer

        CorrectedSteering = CalcCorrectedSteering + NonLinearSteerValue
       # print(CorrectedSteering)
      #  print(NonLinearSteerValue)

        if abs(CorrectedSteering) > 1:
            CorrectedSteering = math.copysign(1,CorrectedSteering)

        gamepad.left_joystick_float(x_value_float=CorrectedSteering, y_value_float=0.0) #setting virtual gamepad steer
        gamepad.update()
        BigFFB=0
        SmallFFB = float(clamp(FFB / 127,0,1))
        if SmallFFB >= 0.95:
            BigFFB = SmallFFB
        XInput.set_vibration(0,SmallFFB,0)
        #print(CorrectedSteering," ",CurrentSlipAngle)
        events = XInput.get_events()
        for event in events:
            if event.user_index == 0:
                if event.type == XInput.EVENT_STICK_MOVED:
                    if event.stick == XInput.LEFT:
                        #print("\r",event.x , end = '')
                        laststeervalue = float(event.x)
                        NonLinearSteerValue = math.copysign(pow(abs(laststeervalue),NonLinearity),laststeervalue)

        time.sleep(0.0001)

    input()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/