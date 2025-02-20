# BetterVetSwerve

## Progress
- [ ] constants.py
- [ ] robot.py
- [ ] robotcontainer.py
- Commands
  - [ ] FCDrive.py
  - [ ] auto.py
  - [ ] bucketCommand.py
  - [ ] halveDriveSpeed.py
  - [ ] intakeCommand.py
- Subsystems
  - [ ] bucketSubsystem.py
  - [ ] intakeSubystem.py
  - [ ] state.py
  - [ ] swerveDrive.py
  - [ ] swerveModule.py

## Git
* The main branch is only for 100% tested, working code
* Merging dev to main should require at least one other programmer to agree
* Don't make commits directly to dev either, make a branch (ex: eh_cleaning_up_subsystems) and then PULL FROM DEV and deal with CONFLICTS ON YOUR END
* Please use ruff (for now only on needed files until things are cleaned up) before making a pull request to merge your branch to dev
* After merge delete your branch

## Ruff
https://github.com/astral-sh/ruff

Should be as easy as `ruff check file.py`

Example output
```
[ethanscharlie@ethanscharlie subsystems]$ ruff check swerveModule.py 
swerveModule.py:2:8: F401 [*] `wpilib` imported but unused
  |
1 | import math
2 | import wpilib
  |        ^^^^^^ F401
3 | import wpimath.kinematics
4 | import wpimath.geometry
  |
  = help: Remove unused import: `wpilib`

swerveModule.py:60:9: F841 Local variable `optimizedState` is assigned to but never used
   |
58 |         # Optimize the reference state to avoid spinning further than 90 degrees
59 |         state = desiredState
60 |         optimizedState = wpimath.kinematics.SwerveModuleState.optimize(
   |         ^^^^^^^^^^^^^^ F841
61 |             desiredState, encoderRotation
62 |         )
   |
   = help: Remove assignment to unused variable `optimizedState`

swerveModule.py:77:9: F841 Local variable `driveOutput` is assigned to but never used
   |
76 |         # Calculate the drive output from the drive PID controller.
77 |         driveOutput = state.speed
   |         ^^^^^^^^^^^ F841
78 | 
79 |         # # Calculate the turning motor output from the turning PID controller.
   |
   = help: Remove assignment to unused variable `driveOutput`

Found 3 errors.
[*] 1 fixable with the `--fix` option (2 hidden fixes can be enabled with the `--unsafe-fixes` option).

```
