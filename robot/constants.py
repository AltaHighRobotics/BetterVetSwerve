from math import tau, pi

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Driver Controller Configuration ***
    These constants control the driver controller's inputs and behavior.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DRIVER_CONTROLLER_PORT = 0  # The port number for the driver controller
DEADBAND = 0.2  # The deadband range for joystick movement, where small inputs are ignored
TURN_DEADBAND = 0.5  # The deadband range specifically for turning inputs on the joystick
FIELD_ORIENTED = True # NOT RECOMMENDED TO CHANGE

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Default States and Settings ***
    These constants define the default state values for the robot's various mechanisms.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DEFAULT_OBJECTIVE = "I"  # Default objective (could be a mode or mission, for example)
DEFAULT_BUCKET = 0  # Default position for the bucket mechanism (0 could mean neutral or idle position)
DEFAULT_INTAKE = 0  # Default state for the intake mechanism (0 could mean off)
DEFAULT_END_STOP = -1  # Default position for the endstop sensor (could represent a limit or neutral position)
DEFAULT_END_STOP_OVERRIDE = 0  # Default override for the endstop mechanism (0 could mean no override)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Swerve Drive Configuration ***
    These constants define the swerve drive parameters, including gear ratios and speeds for movement.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
SWERVE_TURN_GEAR_RATIO = 1/170 #1/180  # Gear ratio for turning the swerve modules (rotations of the motor per wheel rotation)
SWERVE_MOD_CENTER_TO_CENTER = 0.5715 #0.635  # The distance between the centers of the swerve modules (in meters)
MODULE_MAX_ANGULAR_VELOCITY = pi  # The maximum angular velocity (speed of rotation) of the swerve module (in radians per second)
MODULE_MAX_ANGULAR_ACCELERATION = tau  # The maximum angular acceleration (rate of change of angular velocity) for the swerve module
WHEEL_RADIUS = 0.0508  # The radius of the swerve drive wheels (in meters)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Endstop Configuration ***
    These constants define the ports and behavior of the robot's endstop sensors.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
OUT_ENDSTOP_PORT = 3  # The port number for the external endstop sensor
IN_ENDSTOP_PORT = 2  # The port number for the internal endstop sensor
ENDSTOP_INVERSION = True  # Inversion flag for the endstop behavior (True means the sensor is inverted)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Speed Settings ***
    These constants define the speed settings for various mechanisms, from the intake to swerve drive.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BUCKET_SPEED = 0.9  # Speed for the bucket mechanism (0 to 1 range)
INTAKE_SPEED = 0.8  # Speed for the intake mechanism (0 to 1 range)
OUTTAKE_SPEED = 0.4  # Speed for the outtake mechanism (0 to 1 range)
SWERVE_MIN_SPEED = 0.3  # Minimum speed for swerve drive (used for fine control)
SWERVE_MAX_SPEED = 0.8  # Maximum speed for swerve drive (used for full-speed movement)
SWERVE_MAX_OUTPUT = 0.6  # Maximum output (could be motor voltage or current) for swerve drive

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** Motor IDs ***
    These constants define the motor IDs for each component, allowing the program to control the motors.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BUCKET_ID = 9  # Motor ID for the bucket mechanism

INTAKE_LEFT_ID = 10  # Motor ID for the left intake motor
INTAKE_RIGHT_ID = 11  # Motor ID for the right intake motor

FRONT_LEFT_DRIVE_ID = 3  # Motor ID for the front left swerve drive motor
FRONT_LEFT_TURN_ID = 33  # Motor ID for the front left swerve turn motor

FRONT_RIGHT_DRIVE_ID = 4  # Motor ID for the front right swerve drive motor
FRONT_RIGHT_TURN_ID = 44  # Motor ID for the front right swerve turn motor

BACK_LEFT_DRIVE_ID = 2  # Motor ID for the back left swerve drive motor
BACK_LEFT_TURN_ID = 22  # Motor ID for the back left swerve turn motor

BACK_RIGHT_DRIVE_ID = 5  # Motor ID for the back right swerve drive motor
BACK_RIGHT_TURN_ID = 55  # Motor ID for the back right swerve turn motor

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    *** PID Constants for Turning ***
    These constants define the PID control values for turning the swerve modules.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TURN_P = 10  # Proportional constant for the turning PID controller
TURN_I = 0  # Integral constant for the turning PID controller
TURN_D = 0.3  # Derivative constant for the turning PID controller
