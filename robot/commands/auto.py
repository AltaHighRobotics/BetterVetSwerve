import commands2
from subsystems.swerveDrive import SwerveDrive
import time

class AutonomusCommand(commands2.Command):
    def __init__(self, drive: SwerveDrive, lifetimeSeconds: float) -> None:
        self.drive = drive
        self.lifetimeSeconds = lifetimeSeconds
        self.done = False

        # Require the drive subsystem
        self.addRequirements(self.drive)

    # Override
    def initialize(self) -> None:
        self.drive.FOReset()
        self.time = time.time()
        self.done = False
        
    # Override
    def execute(self) -> None:
        """
        Only executes if the robot is still within its lifetime
        """
        
        if time.time() - self.time <= self.lifetimeSeconds:
            self.drive.drive(0, -0.5, 0, 1, True)
        elif time.time() - self.time <= self.lifetimeSeconds + 2: # Give the robot 2 seconds to stop before DONE (For some reason?!)
            self.stopDrive()
        else:
            self.done = True
        
    # Override
    def end(self, interrupted: bool) -> None:
        self.stopDrive()
    
    # Override
    def isFinished(self) -> bool:
        return self.done

    def stopDrive(self) -> None:
        self.drive.drive(0, 0, 0, 0, False)
