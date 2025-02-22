from pickle import FALSE
from commands2 import Subsystem
import constants

import wpimath.geometry
import wpimath.kinematics
from subsystems.swerveModule import SwerveModule
import navx
import ntcore
import math

from constants import FRONT_LEFT_DRIVE_ID
from constants import FRONT_LEFT_TURN_ID
from constants import FRONT_RIGHT_DRIVE_ID
from constants import FRONT_RIGHT_TURN_ID
from constants import BACK_LEFT_DRIVE_ID
from constants import BACK_LEFT_TURN_ID
from constants import BACK_RIGHT_DRIVE_ID
from constants import BACK_RIGHT_TURN_ID
from constants import TURN_P
from constants import TURN_I
from constants import TURN_D
from constants import SWERVE_MOD_CENTER_TO_CENTER
from constants import DEADBAND
from constants import TURN_DEADBAND
from constants import SWERVE_MIN_SPEED
from constants import SWERVE_MAX_SPEED
from constants import SWERVE_MAX_OUTPUT


class SwerveDrive(Subsystem):
    """
    Represents a swerve drive style drivetrain.
    """

    def __init__(self) -> None:
        super().__init__()

        ctrToCtrOverTwo = SWERVE_MOD_CENTER_TO_CENTER / 2

        self.frontLeftLocation = wpimath.geometry.Translation2d(
            ctrToCtrOverTwo, ctrToCtrOverTwo
        )
        self.frontRightLocation = wpimath.geometry.Translation2d(
            ctrToCtrOverTwo, -ctrToCtrOverTwo
        )
        self.backLeftLocation = wpimath.geometry.Translation2d(
            -ctrToCtrOverTwo, ctrToCtrOverTwo
        )
        self.backRightLocation = wpimath.geometry.Translation2d(
            -ctrToCtrOverTwo, -ctrToCtrOverTwo
        )

        self.frontLeftModule = SwerveModule(
            FRONT_LEFT_DRIVE_ID,
            FRONT_LEFT_TURN_ID,
            TURN_P,
            TURN_I,
            TURN_D,
        )
        self.frontRightModule = SwerveModule(
            FRONT_RIGHT_DRIVE_ID,
            FRONT_RIGHT_TURN_ID,
            TURN_P,
            TURN_I,
            TURN_D,
        )
        self.backLeftModule = SwerveModule(
            BACK_LEFT_DRIVE_ID,
            BACK_LEFT_TURN_ID,
            TURN_P,
            TURN_I,
            TURN_D,
        )
        self.backRightModule = SwerveModule(
            BACK_RIGHT_DRIVE_ID,
            BACK_RIGHT_TURN_ID,
            TURN_P,
            TURN_I,
            TURN_D,
        )

        self.turnLock = False

        self.setMaxOutput(SWERVE_MAX_OUTPUT)

        self.gyro = navx.AHRS.create_spi()  # NavX

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
        fieldRelative: bool,
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
        if abs(xSpeed) < DEADBAND:
            xSpeed = 0
            axes0 += 1
        if abs(ySpeed) < DEADBAND:
            ySpeed = 0
            axes0 += 1
        if abs(rot) < TURN_DEADBAND or self.turnLock:
            rot = 0
            axes0 += 1
        else:
            rot -= math.copysign(TURN_DEADBAND, rot)

        speed = max(
            SWERVE_MIN_SPEED, min(speed, SWERVE_MAX_SPEED)
        )  # Change the drive speed based on the position of the slider

        swerveModuleStates = self.kinematics.toSwerveModuleStates(  # Kinematics
            wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                -xSpeed * speed,
                -ySpeed * speed,
                -rot * speed * math.pi,
                self.gyro.getRotation2d(),
            )
            if fieldRelative
            else wpimath.kinematics.ChassisSpeeds(-xSpeed, -ySpeed, -rot)
        )

        # self.pub.set([swerveModuleStates[0],swerveModuleStates[1],swerveModuleStates[2],swerveModuleStates[3]]) # AdvantageScope
        # print(axes0)
        if axes0 == 3:
            swerveModuleStates[0].angle = wpimath.geometry.Rotation2d(math.pi / 4)
            swerveModuleStates[1].angle = wpimath.geometry.Rotation2d(-math.pi / 4)
            swerveModuleStates[2].angle = wpimath.geometry.Rotation2d(-math.pi / 4)
            swerveModuleStates[3].angle = wpimath.geometry.Rotation2d(math.pi / 4)
        # Set each swerve module to the state produced by the kinematics
        self.frontLeftModule.setDesiredState(swerveModuleStates[0])
        self.frontRightModule.setDesiredState(swerveModuleStates[1])
        self.backLeftModule.setDesiredState(swerveModuleStates[2])
        self.backRightModule.setDesiredState(swerveModuleStates[3])

    def setMaxOutput(
        self, maxOutput
    ):  # Maximum PercentOutput the drive motors can be driven at
        self.maxOut = maxOutput
        self.frontLeftModule.setMaxOut(self.maxOut)
        self.frontRightModule.setMaxOut(self.maxOut)
        self.backLeftModule.setMaxOut(self.maxOut)
        self.backRightModule.setMaxOut(self.maxOut)

    def FOReset(self):  # Set FO forward to the direction the plow is facing
        self.gyro.zeroYaw()

    def lockTurn(self):
        self.turnLock = True

    def unlockTurn(self):
        self.turnLock = False
