import math
import phoenix5 as ctre

from rev import SparkLowLevel, SparkMax
from wpimath.controller import ProfiledPIDController
from wpimath.trajectory import TrapezoidProfile
from wpimath.geometry import Rotation2d
from wpimath.kinematics import SwerveModuleState

from constants import MODULE_MAX_ANGULAR_VELOCITY 
from constants import MODULE_MAX_ANGULAR_ACCELERATION 
from constants import WHEEL_RADIUS 
from constants import SWERVE_TURN_GEAR_RATIO

class SwerveModule:
    """
    Represents a single module of the swerve drive
    """
    
    def __init__(self, driveid: int, steerid: int, kP: float, kI: float, kD: float):
        self.drive = ctre.WPI_BaseMotorController(driveid, "talonfx")
        self.turn = SparkMax(steerid, SparkLowLevel.MotorType.kBrushless)
        self.turnEncoder = self.turn.getEncoder() # NOTE: this is a relative encoder--wheels must be zeroed BEFORE turning on!
        
        self.turningPIDController = ProfiledPIDController(
            kP, kI, kD,
            TrapezoidProfile.Constraints(
                MODULE_MAX_ANGULAR_VELOCITY,
                MODULE_MAX_ANGULAR_ACCELERATION,
            ),
        ) # Turn PID controller

        self.drive.setNeutralMode(ctre.NeutralMode.Brake) # Brake motors when not moving

        self.maxOut = 0 # Maximum output power

        # Limit input range to -pi to pi with wrap
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)

    def getEncoder(self) -> Rotation2d: # Get the current position of the module
        return Rotation2d(self.turnEncoder.getPosition() * math.tau * SWERVE_TURN_GEAR_RATIO)
    
    def setMaxOut(self, value: float):
        self.maxOut = value

    def setDesiredState(
        self, desiredState: SwerveModuleState
    ) -> None:
        """Sets the desired state for the module.

        :param desiredState: Desired state with speed and angle.
        """

        encoderRotation = self.getEncoder()
        desiredState.angle = -desiredState.angle # invert the desired angle because of how our modules are configured

        # Optimize the reference state to avoid spinning further than 90 degrees
        desiredState.optimize(encoderRotation)
        state = desiredState


        # Scale speed by cosine of angle error. This scales down movement perpendicular to the desired
        # direction of travel that can occur when modules change directions. This results in smoother
        # driving.

        state.speed *= (state.angle - encoderRotation).cos()

        # Calculate the drive output from the drive PID controller.
        driveOutput = state.speed

        # Calculate the turning motor output from the turning PID controller.
        turnOutput = self.turningPIDController.calculate(
            self.turnEncoder.getPosition() * math.tau * SWERVE_TURN_GEAR_RATIO, state.angle.radians()
        )

        # Acutually drive!
        self.drive.set(max(-self.maxOut, min(driveOutput, self.maxOut)))
        self.turn.setVoltage(turnOutput)
