from commands2 import Command
from subsystems.swerveDrive import SwerveDrive
import typing
from constants import FIELD_ORIENTED

class FODrive(Command):
    def __init__(self,
                 drive: SwerveDrive,
                 forward_speed: typing.Callable[[], float],
                 strafe_speed: typing.Callable[[], float],
                 rotation_speed: typing.Callable[[], float],
                 speed_scaling: typing.Callable[[], float]
                 ):
        super().__init__()

        self.drive = drive
        self.forward_speed = forward_speed
        self.strafe_speed = strafe_speed
        self.rotation_speed = rotation_speed
        self.speed_scaling = speed_scaling

        self.addRequirements(self.drive)

    def execute(self):
        self.drive.drive(self.forward_speed(), self.strafe_speed(), self.rotation_speed(), self.speed_scaling(), FIELD_ORIENTED)
