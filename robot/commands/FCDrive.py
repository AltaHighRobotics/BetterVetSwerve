from commands2 import Command
from subsystems.swerveDrive import SwerveDrive
import typing
class FODrive(Command):
    def __init__(self,
                 drive: SwerveDrive,
                 Xt: typing.Callable[[], float],
                 Yt: typing.Callable[[], float],
                 Zr: typing.Callable[[], float],
                 Sp: typing.Callable[[], float]
                 ):
        super().__init__()

        self.drive = drive
        self.Xt = Xt
        self.Yt = Yt
        self.Zr = Zr
        self.Sp = Sp

        self.addRequirements(self.drive)

    def execute(self):
        self.drive.drive(self.Xt(), self.Yt(), self.Zr(), self.Sp(),  True)
