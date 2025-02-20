import commands2
from constants import INTAKE_SPEED, OUTTAKE_SPEED
from subsystems.intakeSubsystem import IntakeSubsystem

class Intake(commands2.Command):
    def __init__(self , intake: IntakeSubsystem) -> None:
        super().__init__()
        self.intake = intake
             
    def initialize(self) -> None:
        self.intake.setSpeed(INTAKE_SPEED)

    def end(self, interrupted: bool) -> None:
        self.intake.setSpeed(0)

class Outtake(commands2.Command):
    def __init__(self , intake: IntakeSubsystem) -> None:
        super().__init__()
        self.intake = intake
             
    def initialize(self) -> None:
        self.intake.setSpeed(-OUTTAKE_SPEED)

    def end(self, interrupted: bool) -> None:
        self.intake.setSpeed(0)
