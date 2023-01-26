"""
OutSim Mode 2
OutSim Delay 5
OutSim IP 127.0.0.1
OutSim Port 30000
OutSim ID 0
OutSim Opts 80
"""
import sys
import socket
import struct
import threading

import FileRoutines
import GUI
from GlobalVars import *
from CalculateCarData import CalculateCarDataF
from GamePads import HandleGamepads


def weird_division(n, d):
    return n / d if d else 0

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
            print("timoeut")
            for key in vars(OutsimData):
                if not key.startswith("__"):
                    setattr(OutsimData, key, 0)
        else:
            # print(data)
            outsim_pack = struct.unpack("7f4b2f7f4b2f7f4b2f7f4b2f", data)
            OutsimData.wheel0slipangle = outsim_pack[12]
            OutsimData.wheel1slipangle = outsim_pack[25]
            OutsimData.wheel2slipangle = outsim_pack[38]
            OutsimData.wheel3slipangle = outsim_pack[51]
            OutsimData.wheelspeed1 = outsim_pack[18]
            OutsimData.wheelspeed0 = outsim_pack[5]
            OutsimData.wheelspeed2 = outsim_pack[31]
            OutsimData.wheelspeed3 = outsim_pack[44]
            OutsimData.touchingground0 = outsim_pack[9]
            OutsimData.touchingground1 = outsim_pack[22]
            OutsimData.wheel3steer = outsim_pack[40]
            OutsimData.wheel2steer = outsim_pack[27]
            OutsimData.SlipFraction0 = outsim_pack[8]
            OutsimData.SlipFraction1 = outsim_pack[21]
            OutsimData.SlipFraction2 = outsim_pack[34]
            OutsimData.SlipFraction3 = outsim_pack[47]
            #print("outsimdata", abs(outsim_pack[34]),outsim_pack[47])

if __name__ == '__main__':
    global InternalVar
    FileRoutines.readconfig()
    FileRoutines.patchLFScfg()

    OutSimThread = threading.Thread(target=GetOutsimData, daemon=True)
    UpdateControlChangesThread = threading.Thread(target=CalculateCarDataF, daemon=True)
    GamepadsThread = threading.Thread(target=HandleGamepads,daemon = True)
    print(777)
    OutSimThread.start()
    UpdateControlChangesThread.start()
    GamepadsThread.start()

    print(Settings.Steering.LFSSteerAngle)
    GUI.RunGUI()
    FileRoutines.writeconfig()
    FileRoutines.patchLFScfg()
    sys.exit(1)

    input()


