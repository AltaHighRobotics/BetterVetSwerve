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
