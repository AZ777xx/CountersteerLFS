# CountersteerLFS
![image](https://user-images.githubusercontent.com/57565244/218261599-913dfad7-dcd2-4cc8-8451-630f3793790c.png)

This is a work-in-progress script, that implements GTA or BeamNG-like Steering Correction to LFS by adding a Virtual XInput gamepad, reading a real gamepad input and correcting its output based on slide angles. Also features a rudimentary TC and Brake Help (ABS-like) feature.

#### How does it work?
1. Reads XInput Gamepad in slot 1
2. Creates Virtual XIput Gamepad in slot 2
3. Reads car information through LFS OutSim
4. Gets input from Gamepad 1 and outputs corrected Steering through Gamepad 2

#### Requirments:
+ VigemBus
+ Any Xinput gamepad in Slot 1
+ Written and tested on Python 3.9, requires XInput and vgamepad libraries

#### How to set up:
+ Either set LFS_cfg_location in default.cfg and to your LFS cfg.txt loctation or manually set the LFS cfg.txt Outsim section to the following:
```
OutSim Mode 2
OutSim Delay 5
OutSim IP 127.0.0.1
OutSim Port 30000
OutSim ID 0
OutSim Opts 80
```
+ Make sure you have VigemBus installed and a gamepad in slot 1
+ Launch CountersteerLFS before LFS
+ In controls, bind Steering, Gas, Brakes and Handbrake to XInput Gamepad 2
+ Currently, Gas and Brakes are hardcoded to the Triggers, and Steering to the left Joystick

#### Planned Features:
+ Error Handling
+ Better LFS cfg patching
+ Standalone EXE release
+ Better profile handling
+ More configurable options

