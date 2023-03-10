import XInput
import vgamepad as vg
import time
import math

import vgamepad.win.virtual_gamepad

import GlobalVars
from GlobalVars import *

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

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
    global InternalVars
    # Do your things here. For instance:
    InternalVars.FFB = small_motor
   # print(f"Received notification for client {client}, target {target}")
   # print(f"large motor: {large_motor}, small motor: {small_motor}")
 #   print(f"led number: {led_number}")

def HandleGamepads():
    XInput.set_deadzone(XInput.DEADZONE_LEFT_THUMB, 0)
    XInput.set_deadzone(XInput.DEADZONE_RIGHT_THUMB, 0)
    XInput.set_deadzone(XInput.DEADZONE_TRIGGER, 0)
    gamepad = vg.VX360Gamepad()

    gamepad.register_notification(callback_function=my_callback)
    print(XInput.get_connected())
    print(str((XInput.get_state(0))))
    state_0 = XInput.get_state(0)
    while True:
        gamepad.left_joystick_float(x_value_float=InternalVars.CorrectedSteering, y_value_float=InternalVars.CorrectedThrottle) #setting virtual gamepad steer
        gamepad.right_joystick_float(x_value_float=InternalVars.CorrectedHandbrake,
                                    y_value_float=InternalVars.CorrectedBrake)
        gamepad.update()

        SmallFFB = float(clamp(InternalVars.FFB / 127, 0, 1))

        XInput.set_vibration(0, SmallFFB, 0)
        # print(CorrectedSteering," ",CurrentSlipAngle)
        events = XInput.get_events()
        for event in events:
            if event.user_index == 0:
                if event.type == XInput.EVENT_STICK_MOVED:
                    if event.stick == XInput.LEFT:
                        # print("\r",event.x , end = '')
                        laststeervalue = float(event.x)
                        InternalVars.NonLinearSteerValue = math.copysign(
                            pow(abs(laststeervalue), Settings().Steering.NonLinearity), laststeervalue)
                if event.type == XInput.EVENT_TRIGGER_MOVED:
                    if event.trigger == XInput.RIGHT:
                        InternalVars.RealThrottle = float(event.value)
                    if event.trigger == XInput.LEFT:
                        InternalVars.RealBrake = float(event.value)
                if event.type == XInput.EVENT_BUTTON_PRESSED:
                    if InternalVars.SetHandbrakeButton == 1:
                        Settings.Main.HandBrakeButton = event.button
                        InternalVars.SetHandbrakeButton = 0
                        time.sleep(0.3)
                    elif event.button == Settings.Main.HandBrakeButton:
                        InternalVars.HandBrakePressed = 1
                if event.type == XInput.EVENT_BUTTON_RELEASED:
                    if event.button == Settings.Main.HandBrakeButton:
                        InternalVars.HandBrakePressed = 0
                        print("depressed")

        if GlobalVars.InternalVars.ClosingApp ==1:
            del gamepad
            #print(gamepad)
            #time.sleep(5)
            return

        time.sleep(0.0001)