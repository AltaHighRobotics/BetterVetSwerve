import commands2
import wpilib.shuffleboard
import constants
from wpilib.shuffleboard import Shuffleboard
from subsystems.swerveDrive import SwerveDrive
from wpilib import SmartDashboard
import wpilib

class State(commands2.Subsystem):
    """
    A virtural machine for controlling command-based FRC robots
    Created by Shayden Jennings in 2024, team 4598. Version 1.0
    
    Usage:
        All buttons are mapped to virtual buttons. By doing this, we can
    perform persistent logic on button presses. This means that a button
    can trigger logic that can have effect even after the button is
    released, for example putting the robot into shoot mode by pressing 
    button 3, which will change the trigger on the controller from running
    the intake to running the shooter

        All mappings are contained in the handleButton function. This function
    can also handle endstops or other abitrary events. When the button is 
    pressed, feed into this function that button's name (can be anything) and
    True ( e.g. handleButton("Trigger", True) ). You can also do this for when 
    the button is released (e.g. stopping the intake when you release the 
    trigger)

         You must put bindings into robotcontainer to run the handleButton
    function when buttons are pressed. Use a Trigger object and .onTrue to
    run a lambda (because a command can't run a function with arguments) 
    containing the handleButton function for the desired button. To detect
    when the button is released use a similar method but with .onFalse
    Below is a function to map a button (for both press and release):

def mapButton(self, button, stateTrigger): # Maps a physical button to trigger a state change
     commands2.button.JoystickButton(self.driverController, button).onTrue(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, True))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, False)))

        You can put this fuction in robotcontainer and use it given the
    following are defined:

        self.driverController = <controller used for drving>
        self.state = State()

            Now the the buttons have been set up, you need to construct
        functions to control the robot based off of it's state. These MUST
        return a boolean: if you have a state with more than 2 possible
        values, you will need multiple functions for that state. Example:

        in constants:
        
        kDefaultIntakeState = 0

        in __init__:
        self.intakeState = constants.kDefaultIntakeState # can be 1 (intake), 0 (idle), -1 (outtake)

        in the class:
        def isIntaking(self):
            return self.intakeState == 1

        def isOuttaking(self):
            return self.intakeState == -1

        in robotcontainer.configureBindings:
        commands2.button.Trigger(self.state.isIntaking).whileTrue(<intake command>)
        commands2.button.Trigger(self.state.isOutaking).whileTrue(<outtake command>)

            NOTE that there must be a defined default state. This is because the bindings
        only trigger things when their values CHANGE (e.g. a button is pressed or a state changes),
        so you need to set a default command for things you want to run when the robot is 
        started in teleop (e.g. drivetrain)

            Also, it is highly recommended that you set a subsystem's idle state as it's default
        command (e.g. set the intake's default command to the motors not moving). This
        avoids needing an extra function in state or binding in robotcontainer and also 
        theoretically serves as a failsafe is you mess something up in state.

            Finally, if you want to display certain states, create an updateWidgets
        function that refreshes the widgets and put it in the handleButton function
    """
    def __init__(self, drive: SwerveDrive):
        super().__init__()

        self.drive = drive

        self.objective = constants.kDefaultObjective # "P": plow, "I": intake, "B": bucket
        self.bucket = constants.kDefaultBucket # 1: moving out, 0: idle, -1: moving in
        self.intake = constants.kDefaultIntake # Desired state of intake (intake can't run if the bucket is out) 1: intaking, 0: idle, -1: outtake
        self.endstop = constants.kDefaultEndStop # 1: fully out, 0: middle, -1: fully in
        self.intaking = self.intake # 1: intaking, 0: idle, -1: outtake
        self.endstopOverride = constants.kDefaultEndStopOverride # User can overide the endstops if they are not working 0: not overridden, 1 overridden

        # Shuffleboard widgets
        self.tab = Shuffleboard.getTab("State")
        self.objectiveWidget = self.tab.add("Objective", "Default").getEntry()
        self.endstopOverrideWidget = wpilib.SendableChooser()
        self.endstopOverrideWidget.setDefaultOption("OFF", False)
        self.endstopOverrideWidget.addOption("ON", True)
        self.tab.add("Endstop Override", self.endstopOverrideWidget)

    def isEndstopOverride(self):
        self.endstopOverride = self.endstopOverrideWidget.getSelected()
        return self.endstopOverride
    
    def isExtending(self):
        return self.bucket == 1

    def isRetracting(self):
        return self.bucket == -1
    
    def isIntaking(self):
        return self.intaking == 1

    def isOutaking(self):
        return self.intaking == -1
    
    def updateWidgets(self):
        self.objectiveWidget.setString({"I": "Intake", "P": "Plow", "B": "Bucket"}[self.objective])

    def handleButton(self, button, pressed):
        if button == "Forward": # Run score subsytems to accomplish objective
            if pressed:
                if self.objective == "B": # Extend bucket
                    if self.endstop != 1 or self.endstopOverride: # As long as the button hasn't hit the endstop, we can extend it
                        self.bucket = 1
                    else:
                        self.bucket = 0 # Don't move the bucket it we're at the stop
                
                else: # Intake/Plow
                    self.intake = 1 # Tell State we want to intake (if the bucket needs to RTH, the endstops will trigger
                    #                  actual intaking when the bucket is back)
                    self.bucket = -1
                    if self.endstop == -1 or self.endstopOverride: # We can only intake if the bucket is all the way back
                        self.bucket = 0 # Stop the bucket
                        self.intaking = 1 # Actually run the intake
                    
            else:
                self.bucket = 0
                self.intake = 0
                self.intaking = 0

        elif button  == "Bucket" and pressed:
            self.objective = "B"
            self.drive.unlockTurn()

        elif button == "Plow" and pressed:
            self.objective = "P"
            self.drive.lockTurn()

        elif button == "Intake" and pressed:
            self.objective = "I"
            self.drive.unlockTurn()

        elif button == "Back": # Run score subsystems to accomplish objective
            if pressed:
                if self.objective == "B": # Retract Bucket
                 if self.endstop != -1 or self.endstopOverride: # Bottom endstop
                    self.bucket = -1
                 else:
                    self.bucket = 0
            
                else: # Intake/Plow
                 self.intake = -1
                 self.intaking = -1 # Run the intake backwards (useful if the bot jams)
            else:
                self.bucket = 0
                self.intake = 0
                self.intaking = 0 
        
        elif button == "Out":
            if pressed:
                self.bucket = 0 # Stop the bucket
                self.endstop = 1 # Tell State the bucket is fully out

            else:
                self.endstop = 0 # Tell State we're somewhere in the middle

        elif button =="In":
            if pressed:
                self.bucket = 0 # Stop the bucket
                self.endstop = -1 # Tell State that the bucket is fully in
                if self.intake == 1:
                    self.intaking = 1
            
            else:
                self.endstop = 0 # Tell State we're somewhere in the middle
                

        self.updateWidgets() # Update Shuffleboard to match the new state(s)