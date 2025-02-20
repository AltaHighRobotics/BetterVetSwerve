from commands2 import Subsystem
from constants import INTAKE_LEFT_ID, INTAKE_RIGHT_ID
import phoenix5 as ctre
import wpilib
class IntakeSubsystem(Subsystem):
    """
    Represents a 2 motor flywheel intake system
    """

    def __init__(self) -> None:
        super().__init__()
        self.motorLeft = ctre.WPI_TalonSRX(INTAKE_LEFT_ID)
        self.motorRight = ctre.WPI_TalonSRX(INTAKE_RIGHT_ID)
        self.motorRight.setInverted(True)
        self.motors = wpilib.MotorControllerGroup(self.motorLeft, self.motorRight)

    def setSpeed(self, speed): # Sets speed and runs intake. 
        self.motors.set(speed)
