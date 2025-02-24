from commands2 import Subsystem
import wpilib.shuffleboard
import constants
from wpilib.shuffleboard import Shuffleboard
from wpilib import SmartDashboard
import wpilib

class StateManager(Subsystem):
    """
    A class for more advanced control over command-based FRC robots
    Created by Shayden Jennings in 2024, team 4598. Version 1.1
    
    Usage:
        All events are mapped to virtual states. By doing this, we can
    perform persistent logic on button presses/arbitrary triggers. This means that a event
    can trigger logic that can have effect even after the event is
    over, for example putting the robot into shoot mode by pressing 
    button 3, which will change the trigger on the controller from running
    the intake to running the shooter

        To use StateManager, create a class that inherets from it and define the following:
            - __init__(): set up default states and (optional) widgets and subsystem
                Must have super().__init__ in it
            - handleEvent(event, isOn): handle input such as button presses and enstops

        All mappings are contained in the handleEvent function. This function
    can also handle endstops or other abitrary events. When the event happens,
    feed into this function that event's name (can be anything) and
    True ( e.g. handleEvent("Trigger", True) ). You can also do this for when 
    the event is over (e.g. stopping the intake when you release the 
    trigger)

         You must put bindings into robotcontainer to run the handleEvent
    function when events happen. Use a Trigger object and .onTrue to
    run a lambda (because a command can't run a function with arguments) 
    containing the handleEvent function for the desired event. To detect
    when the event is over use a similar method but with .onFalse
    Below is a function to map a button (for both press and release):

def mapButton(self, button, stateTrigger): # Maps a physical button to trigger a state change
     commands2.button.JoystickButton(self.driverController, button).onTrue(commands2.cmd.runOnce(lambda: self.state.handleEvent(stateTrigger, True))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleEvent(stateTrigger, False)))

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
        function that refreshes the widgets and put it in the handleEvent function
    """
    def __init__(self):
        super().__init__()
        """
            In this function, you must set all states to their default values. It 
        is reccommended that you set these values in constants.
        
            You may need to feed subsystems into State. If so, put them as arguments into
        this function. (example use cases: need to set the drive speed when a button is 
        pressed, reading AprilTags, etc.)
        
            If you plan to use widgets, also intialize them here.
        Here's an example of what you could put here:

        # States
        self.objective = constants.kDefaultObjective
              
        # Shuffleboard widgets
        self.tab = Shuffleboard.getTab("State")
        self.objectiveWidget = self.tab.add("Objective", "Default").getEntry()"""
    
    def updateWidgets(self):
        print("""
This function has not been implemented. Here's an example of what you could put here:
        self.objectiveWidget.setString({"I": "Intake", "P": "Plow", "B": "Bucket"}[self.objective])""")

    def handleEvent(self, event, isOn):
        print("""
This function has not been implemented. Here's an example of what you could put here:
              
        if event == "Forward": # Run score subsytems to accomplish objective
            if isOn:
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

        self.updateWidgets() # Update Shuffleboard to match the new state(s)
        """)