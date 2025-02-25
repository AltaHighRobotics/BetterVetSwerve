from photonlibpy.photonCamera import PhotonCamera
from commands2 import Subsystem
# from photonlibpy.photonTrackedTarget import PhotonTrackedTarget
from utils.flag import Flag

from constants import KCAM_NAME

from constants import SWERVE_MAX_SPEED
import constants

class AprilTagSubsystem(Subsystem): # Apriltags with PhotonVision
    def __init__(self) -> None:
        super().__init__()

        self.cam = PhotonCamera(KCAM_NAME)
        self.flagOn = False
        self.flag = None
        self.targets = []

    # def getHighestID(self, targets: list[PhotonTrackedTarget]) -> PhotonTrackedTarget: # get the target with the highest fiducial ID
    #     bestTarget = targets[0]
    #     for target in targets:
    #         if target.getFiducialId() > bestTarget.getFiducialId():
    #             bestTarget = target
    #     return bestTarget

    # def refresh(self) -> list[PhotonTrackedTarget]: # Get latest target data
    #     result = self.cam.getLatestResult()
    #     if result.hasTargets():
    #         self.targets = result.getTargets()
    #         return self.targets
    #     else: return None
    
    def hasTarget(self, id: int = None) -> bool: # See if a target with a given fiducial is visible. Run with no args to see if any targets are visible
        targets = self.targets
        if targets is not None:
            if id is not None: 
                for target in targets:
                    if target.getFiducialId() == id:
                        return True # If target is found
            else: return True # If no id is given and we have targets
        return False # No targets
    
    def getTargetYaw(self, id:int): # Get the angle of the target so we can steer towards it
        targets = self.targets
        if targets is not None:
            for target in targets:
                if target.getFiducialId() == id:
                    return target.getYaw()
        return 0
    
    def setFlag(self, flag: Flag):
        self.flagOn = True
        self.flag = flag

    def isFlagged(self):
        return self.flagOn

    #### MAKE THIS WORK #### source: https://docs.photonvision.org/en/v2025.2.1-rc2/docs/examples/aimingatatarget.html
    def teleopPeriodic(self) -> None:

        xSpeed = -1.0 * self.controller.getLeftY() * constants.KMAX_SPEED
        ySpeed = -1.0 * self.controller.getLeftX() * constants.KMAX_SPEED
        rot = -1.0 * self.controller.getRightX() * constants.KMAX_ANGULAR_SPEED


        # Get information from the camera
        targetYaw = 0.0
        targetVisible = False
        results = self.cam.getAllUnreadResults()
        if len(results) > 0:
            result = results[-1]  # take the most recent result the camera had
            for target in result.getTargets():
                if target.getFiducialId() == 7:
                    # Found tag 7, record its information
                    targetVisible = True
                    targetYaw = target.getYaw()


        if self.controller.getAButton() and targetVisible:

            # Driver wants auto-alignment to tag 7
            # And, tag 7 is in sight, so we can turn toward it.
            # Override the driver's turn command with an automatic one that turns toward the tag.

            rot = -1.0 * targetYaw * constants.KAUTO_ALIGN_P * constants.KMAX_ANGULAR_SPEED


        self.swerve.drive(xSpeed, ySpeed, rot, True, self.getPeriod())