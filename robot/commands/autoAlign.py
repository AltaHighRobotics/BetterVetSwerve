from commands2 import Command
from wpimath.controller import PIDController
from typing import Callable

from subsystems.swerveDrive import SwerveDrive
from subsystems.aprilTagSubsystem import AprilTagSubsystem

import constants

class AutoAlign(Command):
    def __init__(self, drive: SwerveDrive, vision: AprilTagSubsystem, fwd: Callable[[],float], rot: Callable[[],float], tagID = 1):
        super().__init__()

        self.drive = drive
        self.vision = vision
        self.fwd = fwd
        self.rot = rot
        self.tagnID = tagID

        self.PID = PIDController(constants.kAutoAlignP, constants.kAutoAlignI, constants.kAutoAlignD)
        self.PID.disableContinuousInput()
        self.PID.setSetpoint(0)

    def execute(self):
        if self.vision.hasTarget(self.tagnID) and (abs(self.rot()) <= .1) :
            yaw = self.vision.getTargetYaw(self.tagnID)
            
            steerPID = self.PID.calculate(yaw)
            
            self.drive.arcadeDrive(self.fwd(), steerPID)
        
        else:
            self.drive.arcadeDrive(self.fwd(), self.rot())