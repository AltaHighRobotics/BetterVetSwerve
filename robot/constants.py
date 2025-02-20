import math

# Input
kDriverControllerPort = 0
kDeadband = .2
kTurnDeadband = .5

# States
kDefaultObjective = "I"
kDefaultBucket = 0
kDefaultIntake = 0
kDefaultEndStop = -1
kDefaultEndStopOverride = 0

# Swerve
kModuleMaxAngularVelocity = math.tau # Keep as it
kModuleMaxAngularAcceleration = 2*math.tau # Keep as is
kSwerveTurnGearRatio = 1/180#1 / 250 # (1/160) how many times the wheel rotates for every revolution of the turn motor
# Dimensions for kinematics
kSwerveModCtrToCtr = .635 # How far apart the modules are, not diagnol
kWheelRadius = 0.0508 # Meter


# Enstops
kOutEndstopPort = 3
kInEndstopPort = 2
kEndstopInversion = True
# Speeds
kBucketSpeed = .9
kIntakeSpeed = .8
kOuttakeSpeed = .4
kSwerveMinSpeed = .3
kSwerveMaxSpeed = .8 # 1
kSwerveMaxOutput = .6 # .8
# MotorIDs
# Bucket
kBucketID = 9

#Intake
kIntakeLID = 10
kIntakeRID = 11

# Front Left
kFLDriveID = 3
kFLTurnID = 33

# Front Right
kFRDriveID = 4
kFRTurnID = 44

# Back Left
kBLDriveID = 2
kBLTurnID = 22

# Back Right
kBRDriveID = 5
kBRTurnID = 55

# Turn PID
# Front Left
kTurnFLP = 10#13
kTurnFLI = 0#0
kTurnFLD = .3#.3

# Front Right
kTurnFRP = kTurnFLP + 0
kTurnFRI = kTurnFLI + 0
kTurnFRD = kTurnFLD + 0

# Back Left
kTurnBLP = kTurnFLP + 0
kTurnBLI = kTurnFLI + 0
kTurnBLD = kTurnFLD + 0

# Back Right
kTurnBRP = kTurnFLP + 0
kTurnBRI = kTurnFLI + 0
kTurnBRD = kTurnFLD + 0

