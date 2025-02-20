
from math import tau

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Input
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DRIVER_CONTROLLER_PORT = 0
DEADBAND = 0.2
TURN_DEADBAND = 0.5

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Default States
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEFAULT_OBJECTIVE = "I"
DEFAULT_BUCKET = 0
DEFAULT_INTAKE = 0
DEFAULT_END_STOP = -1
DEFAULT_END_STOP_OVERRIDE = 0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Swerve math
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MODULE_MAX_ANGULAR_VELOCITY = tau
MODULE_MAX_ANGULAR_ACCELERATION = 2 * tau
SWERVE_TURN_GEAR_RATIO = 1/180 # Rotations from motor to wheel
SWERVE_MOD_CENTER_TO_CENTER = 0.635 # How far apart the modules are, not diagnol
WHEEL_RADIUS = 0.0508 # In Meters

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Endstops
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
OUT_ENDSTOP_PORT = 3
IN_ENDSTOP_PORT = 2
ENDSTOP_INVERSION = True

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Speeds
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BUCKET_SPEED = 0.9
INTAKE_SPEED = 0.8
OUTTAKE_SPEED = 0.4
SWERVE_MIN_SPEED = 0.3
SWERVE_MAX_SPEED = 0.8
SWERVE_MAX_OUTPUT = 0.6

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Motor IDS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BUCKET_ID = 9

INTAKE_LEFT_ID = 10
INTAKE_RIGHT_ID = 11

FRONT_LEFT_DRIVE_ID = 3
FRONT_LEFT_TURN_ID = 33

FRONT_RIGHT_DRIVE_ID = 4
FRONT_RIGHT_TURN_ID = 44

BACK_LEFT_DRIVE_ID = 2
BACK_LEFT_TURN_ID = 22

BACK_RIGHT_DRIVE_ID = 5
BACK_RIGHT_TURN_ID = 55

TURN_P = 10
TURN_I = 0
TURN_D = 0.3

