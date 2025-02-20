#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

from typing import Any
from subsystems.intakeSubsystem import IntakeSubsystem
from commands.bucketCommand import Extend 
from commands.bucketCommand import Retract
from commands.intakeCommand import Intake, Outtake 
from commands.auto import AutonomusCommand
import wpilib
import wpilib.shuffleboard
from wpilib.interfaces import GenericHID

import commands2
import commands2.button

from subsystems.state import State
from subsystems.swerveDrive import SwerveDrive
from subsystems.bucketSubsystem import BucketSubsystem
from commands.FCDrive import FODrive

from constants import DRIVER_CONTROLLER_PORT, ENDSTOP_INVERSION, IN_ENDSTOP_PORT, OUT_ENDSTOP_PORT

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The driver's controller
        # self.driverController = wpilib.XboxController(DRIVER_CONTROLLER_PORT)
        self.driverController = wpilib.Joystick(DRIVER_CONTROLLER_PORT)

        # The robot's subsystems                
        # Drive
        self.drive = SwerveDrive()

        # Bucket
        self.bucket = BucketSubsystem()

        # Intake
        self.intake = IntakeSubsystem()

        # State
        self.state = State(self.drive)

        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.setDefaultOption("ON", AutonomusCommand(self.drive, 2))
        self.autoChooser.addOption("OFF", None)
        wpilib.shuffleboard.Shuffleboard.getTab("State").add("Auto", self.autoChooser)

        self.configureButtonBindings()
        self.drive.setDefaultCommand(
            FODrive(self.drive,
                self.driverController.getX, 
                self.driverController.getY, 
                self.driverController.getZ,
                lambda: (-(self.driverController.getRawAxis(3))+1)/2
                )
        )
        # set up default drive command

    def mapButton(self, button, stateTrigger): # Maps a physical button to trigger a state change
        commands2.button.JoystickButton(self.driverController, button).onTrue(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, True))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, False)))

    def mapPOV(self, angle, stateTrigger): # Maps a physical button to trigger a state change
        commands2.button.POVButton(self.driverController, angle).onTrue(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, True))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, False)))
    
    def mapEndstop(self, port, stateTrigger, isInverted = False):
        commands2.button.Trigger(wpilib.DigitalInput(port).get).onTrue(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, not isInverted))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, isInverted)))

    def configureButtonBindings(self):
       
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        
        # BUTTONS - Buttons trigger states or commands
        self.mapButton(1, 'Forward')
        self.mapButton(2, 'Back')
        self.mapButton(12, 'Drive Mode')
        # self.mapButton(3, 'Out')
        # self.mapButton(4, 'In')

        # POV's
        self.mapPOV(0, 'Bucket')
        self.mapPOV(90, 'Plow')
        self.mapPOV(180, 'Intake')

        # Shuffleboard
        commands2.button.Trigger(self.state.isEndstopOverride).onTrue(commands2.cmd.runOnce(lambda: print("!!!ENDSTOPS OVERRIDDEN!!!")))

        # Endstops
        self.mapEndstop(OUT_ENDSTOP_PORT, "Out", not ENDSTOP_INVERSION)
        self.mapEndstop(IN_ENDSTOP_PORT, "In", ENDSTOP_INVERSION)

        # STATES - States trigger commands
        commands2.button.Trigger(self.state.isExtending).whileTrue(Extend(self.bucket))
        commands2.button.Trigger(self.state.isRetracting).whileTrue(Retract(self.bucket))
        commands2.button.Trigger(self.state.isIntaking).whileTrue(Intake(self.intake))
        commands2.button.Trigger(self.state.isOutaking).whileTrue(Outtake(self.intake))
        commands2.button.JoystickButton(self.driverController, 5).onTrue(commands2.cmd.runOnce(lambda: self.drive.FOReset(), self.drive))
        
        
    def getAutonomousCommand(self):
        return self.autoChooser.getSelected()
