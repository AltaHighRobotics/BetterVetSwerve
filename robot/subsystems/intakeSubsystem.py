from commands2 import Subsystem
import constants
import phoenix5 as ctre
import wpilib
class IntakeSubsystem(Subsystem):
    """
    Represents a 2 motor flywheel intake system
    """

    def __init__(self) -> None:
        super().__init__()
        self.motorLeft = ctre.WPI_TalonSRX(constants.kIntakeLID)
        self.motorRight = ctre.WPI_TalonSRX(constants.kIntakeRID)
        self.motorRight.setInverted(True)
        self.motors = wpilib.MotorControllerGroup(self.motorLeft, self.motorRight)

    def setSpeed(self, speed): # Sets speed and runs intake. 
        self.motors.set(speed)