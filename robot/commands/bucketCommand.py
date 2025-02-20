from asyncio import constants
import commands2
import constants

from subsystems.bucketSubsystem import BucketSubsystem

class Extend(commands2.Command):
    def __init__(self , bucket: BucketSubsystem) -> None:
        super().__init__()
        self.bucket = bucket
             
    def initialize(self) -> None:
        self.bucket.setSpeed(constants.kBucketSpeed)

    def end(self, interrupted: bool) -> None:
        self.bucket.setSpeed(0)

class Retract(commands2.Command):
    def __init__(self , bucket: BucketSubsystem) -> None:
        super().__init__()
        self.bucket = bucket
             
    def initialize(self) -> None:
        self.bucket.setSpeed(-constants.kBucketSpeed)

    def end(self, interrupted: bool) -> None:
        self.bucket.setSpeed(0)