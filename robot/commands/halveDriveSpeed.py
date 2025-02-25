#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2

from subsystems.swerveDrive import SwerveDrive

from constants import SWERVE_MAX_OUTPUT

class HalveDriveSpeed(commands2.Command):
    def __init__(self, drive: SwerveDrive) -> None:
        super().__init__()
        self.drive = drive

    def initialize(self) -> None:
        self.drive.setMaxOutput(0.5)

    def end(self, interrupted: bool) -> None:
        self.drive.setMaxOutput(SWERVE_MAX_OUTPUT)
