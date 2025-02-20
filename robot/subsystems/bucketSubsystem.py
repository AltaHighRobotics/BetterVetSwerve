from commands2 import Subsystem
import constants
import phoenix5 as ctre

class BucketSubsystem(Subsystem):
    """
    Represents a telescoping bucket dump mechanism
    """

    def __init__(self) -> None:
        super().__init__()
        self.motor = ctre.VictorSPX(constants.kBucketID)
        self.motor.setInverted(True)
        

    def setSpeed(self, speed: float): # set the PercentOutput of the motor
        self.motor.set(ctre.ControlMode.PercentOutput, speed)