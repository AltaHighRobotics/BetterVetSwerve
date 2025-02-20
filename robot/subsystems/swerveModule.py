import math
import wpilib
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory
import rev
import phoenix5 as ctre
import constants


kWheelRadius = 0.0508 # In meters
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau

class SwerveModule:
    """
    Represents a single module of the swerve drive
    """
    
    def __init__(self, driveid: int, steerid: int, kP: float, kI: float, kD: float):
        self.drive = ctre.WPI_BaseMotorController(driveid, "talonfx")
        self.turn = rev.SparkMax(steerid, rev.SparkLowLevel.MotorType.kBrushless)
        self.turnEncoder = self.turn.getEncoder() # NOTE: this is a relative encoder--wheels must be zeroed BEFORE turning on!
        
        self.turningPIDController = wpimath.controller.ProfiledPIDController(
            kP, kI, kD,
            wpimath.trajectory.TrapezoidProfile.Constraints(
                kModuleMaxAngularVelocity,
                kModuleMaxAngularAcceleration,
            ),
        ) # Turn PID controller

        self.drive.setNeutralMode(ctre.NeutralMode.Brake) # Brake motors when not moving

        self.maxOut = 0 # Maximum output power

        # Limit input range to -pi to pi with wrap
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)

    def getEncoder(self): # Get the current position of the module
        return wpimath.geometry.Rotation2d(self.turnEncoder.getPosition() * math.tau * constants.kSwerveTurnGearRatio)
    
    def setMaxOut(self, value: float):
        self.maxOut = value

    def setDesiredState(
        self, desiredState: wpimath.kinematics.SwerveModuleState
    ) -> None:
        """Sets the desired state for the module.

        :param desiredState: Desired state with speed and angle.
        """

        encoderRotation = self.getEncoder()
        desiredState.angle = -desiredState.angle # invert the desired angle because of how our modules are configured

        # Optimize the reference state to avoid spinning further than 90 degrees
        state = desiredState
        # optimizedState = wpimath.kinematics.SwerveModuleState.optimize(
        #     desiredState, encoderRotation
        # )


#### THIS IS EDITED OUT
        # Scale speed by cosine of angle error. This scales down movement perpendicular to the desired
        # direction of travel that can occur when modules change directions. This results in smoother
        # driving.

        # CRASH optimizedState.speed *= math.cos(optimizedState.angle - encoderRotation)
        # CRASH math.cos(optimizedState.angle - encoderRotation)
        # CRASH optimizedState.angle - encoderRotation
        # CRASH optimizedState.angle <- FUCK YOU
        # NOCRASH encoderRotation
        # CRASH state.speed *= math.cos(state.angle - encoderRotation)
        # CRASH math.cos(state.angle - encoderRotation)
        # NOCRASH state.angle
        # NOCRASH state.angle - encoderRotation
        # NOCRASH math.cos(3)
        # CRASH math.cos(state.angle)
        # CRASH raise Exception(type(state.angle))
        # NOCRASH print(type(state.angle))
        state.speed *= (state.angle - encoderRotation).cos()

        # Calculate the drive output from the drive PID controller.
        driveOutput = state.speed

        # Calculate the turning motor output from the turning PID controller.
        turnOutput = self.turningPIDController.calculate(
            self.turnEncoder.getPosition() * math.tau * constants.kSwerveTurnGearRatio, state.angle.radians()
        )

        # Acutually drive!
        self.drive.set(max(-self.maxOut, min(driveOutput, self.maxOut)))
        self.turn.setVoltage(turnOutput)