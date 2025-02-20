from pickle import FALSE
from commands2 import Subsystem
import constants

import wpimath.geometry
import wpimath.kinematics
from subsystems.swerveModule import SwerveModule
import navx
import ntcore
import math

class SwerveDrive(Subsystem):
    """
    Represents a swerve drive style drivetrain.
    """

    def __init__(self) -> None:
        super().__init__()

        self.frontLeftLocation = wpimath.geometry.Translation2d(constants.kSwerveModCtrToCtr/2, constants.kSwerveModCtrToCtr/2)
        self.frontRightLocation = wpimath.geometry.Translation2d(constants.kSwerveModCtrToCtr/2, -constants.kSwerveModCtrToCtr/2)
        self.backLeftLocation = wpimath.geometry.Translation2d(-constants.kSwerveModCtrToCtr/2, constants.kSwerveModCtrToCtr/2)
        self.backRightLocation = wpimath.geometry.Translation2d(-constants.kSwerveModCtrToCtr/2, -constants.kSwerveModCtrToCtr/2)

        self.frontLeft = SwerveModule(constants.kFLDriveID, constants.kFLTurnID,
                                      constants.kTurnFLP, constants.kTurnFLI, constants.kTurnFLD)
        self.frontRight = SwerveModule(constants.kFRDriveID, constants.kFRTurnID,
                                       constants.kTurnFRP, constants.kTurnFRI, constants.kTurnFRD)
        self.backLeft = SwerveModule(constants.kBLDriveID, constants.kBLTurnID,
                                     constants.kTurnBLP, constants.kTurnBLI, constants.kTurnBLD)
        self.backRight = SwerveModule(constants.kBRDriveID, constants.kBRTurnID,
                                      constants.kTurnBRP, constants.kTurnBRI, constants.kTurnBRD)
        
        self.turnLock = False
        
        self.setMaxOutput(constants.kSwerveMaxOutput)

        self.gyro = navx.AHRS.create_spi() # NavX

        self.kinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.frontLeftLocation,
            self.frontRightLocation,
            self.backLeftLocation,
            self.backRightLocation,
        )

        self.gyro.reset()

        """nt = ntcore.NetworkTableInstance.getDefault()

        # Start publishing an array of module states with the "/SwerveStates" key
        topic = nt.getStructArrayTopic("/SwerveStates", wpimath.kinematics.SwerveModuleState)
        self.pub = topic.publish()"""

    def drive(
        self,
        ySpeed: float,
        xSpeed: float,
        rot: float,
        speed: float,
        fieldRelative: bool
    ) -> None:
        """
        Method to drive the robot using joystick info.
        :param xSpeed: Speed of the robot in the x direction (forward).
        :param ySpeed: Speed of the robot in the y direction (sideways).
        :param rot: Angular rate of the robot.
        :param speed: Speed scaler
        :param fieldRelative: Whether the provided x and y speeds are relative to the field.
        """
        axes0 = 0
        if abs(xSpeed) < constants.kDeadband:
            xSpeed = 0
            axes0 += 1
        if abs(ySpeed) < constants.kDeadband:
            ySpeed = 0
            axes0 += 1
        if abs(rot) < constants.kTurnDeadband or self.turnLock:
            rot = 0
            axes0 += 1 
        else: rot -= math.copysign(constants.kTurnDeadband,rot) 
        
        speed = max(constants.kSwerveMinSpeed, min(speed, constants.kSwerveMaxSpeed)) # Change the drive speed based on the position of the slider

        swerveModuleStates = self.kinematics.toSwerveModuleStates(   # Kinematics
            wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                -xSpeed*speed, -ySpeed*speed, -rot*speed*math.pi, self.gyro.getRotation2d()
            )
            if fieldRelative
            else wpimath.kinematics.ChassisSpeeds(-xSpeed, -ySpeed, -rot)
        )

        # self.pub.set([swerveModuleStates[0],swerveModuleStates[1],swerveModuleStates[2],swerveModuleStates[3]]) # AdvantageScope
        #print(axes0)
        if axes0 == 3:
            swerveModuleStates[0].angle = wpimath.geometry.Rotation2d(math.pi/4)
            swerveModuleStates[1].angle = wpimath.geometry.Rotation2d(-math.pi/4)
            swerveModuleStates[2].angle = wpimath.geometry.Rotation2d(-math.pi/4)
            swerveModuleStates[3].angle = wpimath.geometry.Rotation2d(math.pi/4)
        # Set each swerve module to the state produced by the kinematics
        self.frontLeft.setDesiredState(swerveModuleStates[0])
        self.frontRight.setDesiredState(swerveModuleStates[1])
        self.backLeft.setDesiredState(swerveModuleStates[2])
        self.backRight.setDesiredState(swerveModuleStates[3])

    def setMaxOutput(self, maxOutput): # Maximum PercentOutput the drive motors can be driven at
        self.maxOut = maxOutput
        self.frontLeft.setMaxOut(self.maxOut)
        self.frontRight.setMaxOut(self.maxOut)
        self.backLeft.setMaxOut(self.maxOut)
        self.backRight.setMaxOut(self.maxOut)
    
    def FOReset(self): # Set FO forward to the direction the plow is facing
        self.gyro.zeroYaw()

    def lockTurn(self):
        self.turnLock = True

    def unlockTurn(self):
        self.turnLock = False