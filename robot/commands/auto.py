import commands2
from subsystems.swerveDrive import SwerveDrive
import time

class AutonomusCommand(commands2.Command):
    def __init__(self, drive: SwerveDrive, seconds: float):
        self.drive = drive
        self.secs = seconds
        self.done = False

        # Require the drive subsystem
        self.addRequirements(self.drive)

    def initialize(self):
        self.drive.FOReset()
        self.time = time.time()
        self.done = False
        
    def execute(self):
        if time.time() - self.time <= self.secs:
            self.drive.drive(0, -.5, 0, 1, True)
        elif time.time() - self.time <= self.secs + 2:
            self.drive.drive(0, 0, 0, 0, False)
        else:
            self.done = True
        
    def end(self, interrupted: bool):
        self.drive.drive(0, 0, 0, 0, False)
    
    def isFinished(self) -> bool:
        return self.done