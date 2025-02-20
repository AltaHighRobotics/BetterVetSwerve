from __future__ import annotations
import ntcore._ntcore
import typing
import wpimath.geometry._geometry
__all__ = ['AHRS']
class AHRS(ntcore._ntcore.NTSendable):
    class BoardAxis:
        """
        Members:
        
          kBoardAxisX
        
          kBoardAxisY
        
          kBoardAxisZ
        """
        __members__: typing.ClassVar[dict[str, AHRS.BoardAxis]]  # value = {'kBoardAxisX': <BoardAxis.kBoardAxisX: 0>, 'kBoardAxisY': <BoardAxis.kBoardAxisY: 1>, 'kBoardAxisZ': <BoardAxis.kBoardAxisZ: 2>}
        kBoardAxisX: typing.ClassVar[AHRS.BoardAxis]  # value = <BoardAxis.kBoardAxisX: 0>
        kBoardAxisY: typing.ClassVar[AHRS.BoardAxis]  # value = <BoardAxis.kBoardAxisY: 1>
        kBoardAxisZ: typing.ClassVar[AHRS.BoardAxis]  # value = <BoardAxis.kBoardAxisZ: 2>
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class BoardYawAxis:
        board_axis: AHRS.BoardAxis
        up: bool
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class NavXComType:
        """
        Members:
        
          kMXP_SPI
        
          kMXP_UART
        
          kUSB1
        
          kUSB2
        
          kI2C
        """
        __members__: typing.ClassVar[dict[str, AHRS.NavXComType]]  # value = {'kMXP_SPI': <NavXComType.kMXP_SPI: 0>, 'kMXP_UART': <NavXComType.kMXP_UART: 1>, 'kUSB1': <NavXComType.kUSB1: 2>, 'kUSB2': <NavXComType.kUSB2: 3>, 'kI2C': <NavXComType.kI2C: 4>}
        kI2C: typing.ClassVar[AHRS.NavXComType]  # value = <NavXComType.kI2C: 4>
        kMXP_SPI: typing.ClassVar[AHRS.NavXComType]  # value = <NavXComType.kMXP_SPI: 0>
        kMXP_UART: typing.ClassVar[AHRS.NavXComType]  # value = <NavXComType.kMXP_UART: 1>
        kUSB1: typing.ClassVar[AHRS.NavXComType]  # value = <NavXComType.kUSB1: 2>
        kUSB2: typing.ClassVar[AHRS.NavXComType]  # value = <NavXComType.kUSB2: 3>
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class NavXUpdateRate:
        """
        Members:
        
          k4Hz
        
          k5Hz
        
          k8Hz
        
          k10Hz
        
          k20Hz
        
          k25Hz
        
          k40Hz
        
          k50Hz
        
          k100Hz
        
          k200Hz
        """
        __members__: typing.ClassVar[dict[str, AHRS.NavXUpdateRate]]  # value = {'k4Hz': <NavXUpdateRate.k4Hz: 4>, 'k5Hz': <NavXUpdateRate.k5Hz: 5>, 'k8Hz': <NavXUpdateRate.k8Hz: 8>, 'k10Hz': <NavXUpdateRate.k10Hz: 10>, 'k20Hz': <NavXUpdateRate.k20Hz: 20>, 'k25Hz': <NavXUpdateRate.k25Hz: 25>, 'k40Hz': <NavXUpdateRate.k40Hz: 40>, 'k50Hz': <NavXUpdateRate.k50Hz: 50>, 'k100Hz': <NavXUpdateRate.k100Hz: 100>, 'k200Hz': <NavXUpdateRate.k200Hz: 200>}
        k100Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k100Hz: 100>
        k10Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k10Hz: 10>
        k200Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k200Hz: 200>
        k20Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k20Hz: 20>
        k25Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k25Hz: 25>
        k40Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k40Hz: 40>
        k4Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k4Hz: 4>
        k50Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k50Hz: 50>
        k5Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k5Hz: 5>
        k8Hz: typing.ClassVar[AHRS.NavXUpdateRate]  # value = <NavXUpdateRate.k8Hz: 8>
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def create_spi() -> AHRS:
        """
        Constructs the AHRS class using SPI communication and default settings.
        Use the constructor if you need more customization.
        """
    @typing.overload
    def __init__(self, comType: AHRS.NavXComType) -> None:
        ...
    @typing.overload
    def __init__(self, comType: AHRS.NavXComType, updateRate: AHRS.NavXUpdateRate) -> None:
        ...
    @typing.overload
    def __init__(self, comType: AHRS.NavXComType, updateRate: int) -> None:
        ...
    def configureVelocity(self, swapAxes: bool, invertX: bool, invertY: bool, invertZ: bool) -> None:
        ...
    def enableBoardlevelYawReset(self, enable: bool) -> None:
        """
        Enables or disables board-level yaw zero (reset) requests.  Board-level
        yaw resets are processed by the sensor board and the resulting yaw
        angle may not be available to the client software until at least
        2 update cycles have occurred.  Board-level yaw resets however do
        maintain synchronization between the yaw angle and the sensor-generated
        Quaternion and Fused Heading values.
        
        Conversely, Software-based yaw resets occur instantaneously; however, Software-
        based yaw resets do not update the yaw angle component of the sensor-generated
        Quaternion values or the Fused Heading values.
        """
    def enableLogging(self, enable: bool) -> None:
        """
        Enables or disables logging (via Console I/O) of AHRS library internal
        behaviors, including events such as transient communication errors.
        """
    def getAccelFullScaleRangeG(self) -> int:
        """
        Returns the sensor full scale range (in G)
        of the X, Y and X-axis accelerometers.
        
        :returns: accelerometer full scale range in G.
        """
    def getActualUpdateRate(self) -> int:
        """
        Returns the navX-Model device's currently configured update
        rate.  Note that the update rate that can actually be realized
        is a value evenly divisible by the navX-Model device's internal
        motion processor sample clock (200Hz).  Therefore, the rate that
        is returned may be lower than the requested sample rate.
        
        The actual sample rate is rounded down to the nearest integer
        that is divisible by the number of Digital Motion Processor clock
        ticks.  For instance, a request for 58 Hertz will result in
        an actual rate of 66Hz (200 / (200 / 58), using integer
        math.
        
        :returns: Returns the current actual update rate in Hz
                  (cycles per second).
        """
    def getAltitude(self) -> float:
        """
        Returns the current altitude, based upon calibrated readings
        from a barometric pressure sensor, and the currently-configured
        sea-level barometric pressure [navX Aero only].  This value is in units of meters.
        
        .. note:: This value is only valid sensors including a pressure
                  sensor.  To determine whether this value is valid, see
                  :meth:`isAltitudeValid`.
        
        :returns: Returns current altitude in meters (as long as the sensor includes
                  an installed on-board pressure sensor).
        """
    def getAngle(self) -> float:
        """
        Returns the total accumulated yaw angle (Z Axis, in degrees)
        reported by the sensor.
        
        .. note:: The angle is continuous, meaning it's range is beyond 360 degrees.
                  This ensures that algorithms that wouldn't want to see a discontinuity
                  in the gyro output as it sweeps past 0 on the second time around.
        
        Note that the returned yaw value will be offset by a user-specified
        offset value this user-specified offset value is set by
        invoking the zeroYaw() method.
        
        :returns: The current total accumulated yaw angle (Z axis) of the robot
                  in degrees. This heading is based on integration of the returned rate
                  from the Z-axis (yaw) gyro.
        """
    def getAngleAdjustment(self) -> float:
        """
        Returns the currently configured adjustment angle.  See
        :meth:`setAngleAdjustment` for more details.
        
        If this method returns 0 degrees, no adjustment to the value returned
        via :meth:`getAngle` will occur.
        :returns: adjustment, in degrees (range:  -360 to 360)
        """
    def getBarometricPressure(self) -> float:
        """
        Returns the current barometric pressure, based upon calibrated readings
        from the onboard pressure sensor.  This value is in units of millibar.
        
        .. note:: This value is only valid for a navX Aero.  To determine
                  whether this value is valid, see :meth:`isAltitudeValid`.
        
        :returns: Returns current barometric pressure (navX Aero only).
        """
    def getBoardYawAxis(self) -> AHRS.BoardYawAxis:
        """
        Returns information regarding which sensor board axis (X,Y or Z) and
        direction (up/down) is currently configured to report Yaw (Z) angle
        values.   NOTE:  If the board firmware supports Omnimount, the board yaw
        axis/direction are configurable.
        
        For more information on Omnimount, please see:
        
        http://navx-mxp.kauailabs.com/navx-mxp/installation/omnimount/
        
        :returns: The currently-configured board yaw axis/direction.
        """
    def getCompassHeading(self) -> float:
        """
        Returns the current tilt-compensated compass heading
        value (in degrees, from 0 to 360) reported by the sensor.
        
        Note that this value is sensed by a magnetometer,
        which can be affected by nearby magnetic fields (e.g., the
        magnetic fields generated by nearby motors).
        
        Before using this value, ensure that (a) the magnetometer
        has been calibrated and (b) that a magnetic disturbance is
        not taking place at the instant when the compass heading
        was generated.
        :returns: The current tilt-compensated compass heading, in degrees (0-360).
        """
    def getDisplacementX(self) -> float:
        """
        Returns the displacement (in meters) of the X axis since resetDisplacement()
        was last invoked [Experimental].
        
        .. note:: This feature is experimental.  Displacement measures rely on double-integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting displacement are not known to be very accurate, and the amount of error
                  increases quickly as time progresses.
        
        :returns: Displacement since last reset (in meters).
        """
    def getDisplacementY(self) -> float:
        """
        Returns the displacement (in meters) of the Y axis since resetDisplacement()
        was last invoked [Experimental].
        
        .. note:: This feature is experimental.  Displacement measures rely on double-integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting displacement are not known to be very accurate, and the amount of error
                  increases quickly as time progresses.
        
        :returns: Displacement since last reset (in meters).
        """
    def getDisplacementZ(self) -> float:
        """
        Returns the displacement (in meters) of the Z axis since resetDisplacement()
        was last invoked [Experimental].
        
        .. note:: This feature is experimental.  Displacement measures rely on double-integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting displacement are not known to be very accurate, and the amount of error
                  increases quickly as time progresses.
        
        :returns: Displacement since last reset (in meters).
        """
    def getFirmwareVersion(self) -> str:
        """
        Returns the version number of the firmware currently executing
        on the sensor.
        
        To update the firmware to the latest version, please see:
        
        http://navx-mxp.kauailabs.com/navx-mxp/support/updating-firmware/
        
        :returns: The firmware version in the format [MajorVersion].[MinorVersion]
        """
    def getFusedHeading(self) -> float:
        """
        Returns the "fused" (9-axis) heading.
        
        The 9-axis heading is the fusion of the yaw angle, the tilt-corrected
        compass heading, and magnetic disturbance detection.  Note that the
        magnetometer calibration procedure is required in order to
        achieve valid 9-axis headings.
        
        The 9-axis Heading represents the sensor's best estimate of current heading,
        based upon the last known valid Compass Angle, and updated by the change in the
        Yaw Angle since the last known valid Compass Angle.  The last known valid Compass
        Angle is updated whenever a Calibrated Compass Angle is read and the sensor
        has recently rotated less than the Compass Noise Bandwidth (~2 degrees).
        
        :returns: Fused Heading in Degrees (range 0-360)
        """
    def getGyroFullScaleRangeDPS(self) -> int:
        """
        Returns the sensor full scale range (in degrees per second)
        of the X, Y and X-axis gyroscopes.
        
        :returns: gyroscope full scale range in degrees/second.
        """
    def getLastSensorTimestamp(self) -> int:
        """
        Returns the sensor timestamp corresponding to the
        last sample retrieved from the sensor.  Note that this
        sensor timestamp is only provided when the Register-based
        IO methods (SPI, I2C) are used; sensor timestamps are not
        provided when Serial-based IO methods (TTL UART, USB)
        are used.
        
        :returns: The sensor timestamp (in ms) corresponding to the
                  current AHRS sensor data.
        :rtype: int
        """
    def getPitch(self) -> float:
        """
        Returns the current pitch value (in degrees, from -180 to 180)
        reported by the sensor.  Pitch is a measure of rotation around
        the X Axis.
        
        :returns: The current pitch value in degrees (-180 to 180).
        """
    def getPort(self) -> int:
        ...
    def getQuaternionW(self) -> float:
        """
        Returns the imaginary portion (W) of the Orientation Quaternion which
        fully describes the current sensor orientation with respect to the
        reference angle defined as the angle at which the yaw was last "zeroed".
        
        Each quaternion value (W,X,Y,Z) is expressed as a value ranging from -2
        to 2.  This total range (4) can be associated with a unit circle, since
        each circle is comprised of 4 PI Radians.
        
        For more information on Quaternions and their use, please see this
        `definition <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`_.
        
        :returns: Returns the imaginary portion (W) of the quaternion.
        """
    def getQuaternionX(self) -> float:
        """
        Returns the real portion (X axis) of the Orientation Quaternion which
        fully describes the current sensor orientation with respect to the
        reference angle defined as the angle at which the yaw was last "zeroed".
        
        Each quaternion value (W,X,Y,Z) is expressed as a value ranging from -2
        to 2.  This total range (4) can be associated with a unit circle, since
        each circle is comprised of 4 PI Radians.
        
        For more information on Quaternions and their use, please see this
        `definition <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`_.
        
        :returns: Returns the real portion (X) of the quaternion.
        """
    def getQuaternionY(self) -> float:
        """
        Returns the real portion (Y axis) of the Orientation Quaternion which
        fully describes the current sensor orientation with respect to the
        reference angle defined as the angle at which the yaw was last "zeroed".
        
        Each quaternion value (W,X,Y,Z) is expressed as a value ranging from -2
        to 2.  This total range (4) can be associated with a unit circle, since
        each circle is comprised of 4 PI Radians.
        
        For more information on Quaternions and their use, please see:
        
        https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        
        :returns: Returns the real portion (X) of the quaternion.
        """
    def getQuaternionZ(self) -> float:
        """
        Returns the real portion (Z axis) of the Orientation Quaternion which
        fully describes the current sensor orientation with respect to the
        reference angle defined as the angle at which the yaw was last "zeroed".
        
        Each quaternion value (W,X,Y,Z) is expressed as a value ranging from -2
        to 2.  This total range (4) can be associated with a unit circle, since
        each circle is comprised of 4 PI Radians.
        
        For more information on Quaternions and their use, please see:
        
        https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        
        :returns: Returns the real portion (X) of the quaternion.
        """
    def getRate(self) -> float:
        """
        Return the rate of rotation of the yaw (Z-axis) gyro, in degrees per second.
        
        The rate is based on the most recent reading of the yaw gyro angle.
        
        :returns: The current rate of change in yaw angle (in degrees per second)
        """
    def getRawAccelX(self) -> float:
        """
        Returns the current raw (unprocessed) X-axis acceleration rate (in G).
        
        .. note:: this value is unprocessed, and should only be accessed by advanced users.  This raw value
                  has not had acceleration due to gravity removed from it, and has not been rotated to
                  the world reference frame.  Gravity-corrected, world reference frame-corrected
                  X axis acceleration data is accessible via the :meth:`getWorldLinearAccelX` method.
        
        :returns: Returns the current acceleration rate (in G).
        """
    def getRawAccelY(self) -> float:
        """
        Returns the current raw (unprocessed) Y-axis acceleration rate (in G).
        
        .. note:: this value is unprocessed, and should only be accessed by advanced users.  This raw value
                  has not had acceleration due to gravity removed from it, and has not been rotated to
                  the world reference frame.  Gravity-corrected, world reference frame-corrected
                  Y axis acceleration data is accessible via the :meth:`getWorldLinearAccelY` method.
        
        :returns: Returns the current acceleration rate (in G).
        """
    def getRawAccelZ(self) -> float:
        """
        Returns the current raw (unprocessed) Z-axis acceleration rate (in G).
        
        .. note:: this value is unprocessed, and should only be accessed by advanced users.  This raw value
                  has not had acceleration due to gravity removed from it, and has not been rotated to
                  the world reference frame.  Gravity-corrected, world reference frame-corrected
                  Z axis acceleration data is accessible via the :meth:`getWorldLinearAccelZ` method.
        
        :returns: Returns the current acceleration rate (in G).
        """
    def getRawGyroX(self) -> float:
        """
        Returns the current raw (unprocessed) X-axis gyro rotation rate (in degrees/sec).
        
        .. note:: This value is un-processed, and should only be accessed by advanced users.
                    Typically, rotation about the X Axis is referred to as "Pitch".  Calibrated
                    and Integrated Pitch data is accessible via the :meth:`getPitch` method.
        
        :returns: Returns the current rotation rate (in degrees/sec).
        """
    def getRawGyroY(self) -> float:
        """
        Returns the current raw (unprocessed) Y-axis gyro rotation rate (in degrees/sec).
        
        .. note:: This value is un-processed, and should only be accessed by advanced users.
                    Typically, rotation about the T Axis is referred to as "Roll".  Calibrated
                    and Integrated Pitch data is accessible via the :meth:`getRoll` method.
        
        :returns: Returns the current rotation rate (in degrees/sec).
        """
    def getRawGyroZ(self) -> float:
        """
        Returns the current raw (unprocessed) Z-axis gyro rotation rate (in degrees/sec).
        
        .. note:: This value is un-processed, and should only be accessed by advanced users.
                  Typically, rotation about the T Axis is referred to as "Yaw".  Calibrated
                  and Integrated Pitch data is accessible via the :meth:`getYaw` method.
        
        :returns: Returns the current rotation rate (in degrees/sec).
        """
    def getRawMagX(self) -> float:
        """
        Returns the current raw (unprocessed) X-axis magnetometer reading (in uTesla).
        
        .. note::  this value is unprocessed, and should only be accessed by advanced users.  This raw value
                    has not been tilt-corrected, and has not been combined with the other magnetometer axis
                    data to yield a compass heading.  Tilt-corrected compass heading data is accessible
                    via the :meth:`getCompassHeading` method.
        
        :returns: Returns the mag field strength (in uTesla).
        """
    def getRawMagY(self) -> float:
        """
        Returns the current raw (unprocessed) Y-axis magnetometer reading (in uTesla).
        
        .. note::  this value is unprocessed, and should only be accessed by advanced users.  This raw value
                    has not been tilt-corrected, and has not been combined with the other magnetometer axis
                    data to yield a compass heading.  Tilt-corrected compass heading data is accessible
                    via the :meth:`getCompassHeading` method.
        
        :returns: Returns the mag field strength (in uTesla).
        """
    def getRawMagZ(self) -> float:
        """
        Returns the current raw (unprocessed) Z-axis magnetometer reading (in uTesla).
        
        .. note::  this value is unprocessed, and should only be accessed by advanced users.  This raw value
                    has not been tilt-corrected, and has not been combined with the other magnetometer axis
                    data to yield a compass heading.  Tilt-corrected compass heading data is accessible
                    via the :meth:`getCompassHeading` method.
        
        :returns: Returns the mag field strength (in uTesla).
        """
    def getRequestedUpdateRate(self) -> int:
        """
        Returns the currently requested update rate.
        rate.  Note that not every update rate can actually be realized,
        since the actual update rate must be a value evenly divisible by
        the navX-Model device's internal motion processor sample clock (200Hz).
        
        To determine the actual update rate, use the
        :meth:`getActualUpdateRate` method.
        
        :returns: Returns the requested update rate in Hz
                  (cycles per second).
        """
    def getRobotCentricVelocityX(self) -> float:
        ...
    def getRobotCentricVelocityY(self) -> float:
        ...
    def getRobotCentricVelocityZ(self) -> float:
        ...
    def getRoll(self) -> float:
        """
        Returns the current roll value (in degrees, from -180 to 180)
        reported by the sensor.  Roll is a measure of rotation around
        the X Axis.
        
        :returns: The current roll value in degrees (-180 to 180).
        """
    def getRotation2d(self) -> wpimath.geometry._geometry.Rotation2d:
        """
        Return the heading of the robot as a Rotation2d.
        
        The angle is continuous, that is it will continue from 360 to 361 degrees.
        This allows algorithms that wouldn't want to see a discontinuity in the
        gyro output as it sweeps past from 360 to 0 on the second time around.
        
        The angle is expected to increase as the gyro turns counterclockwise when
        looked at from the top. It needs to follow the NWU axis convention.
        
        :returns: the current heading of the robot as a Rotation2d. This heading is
                  based on integration of the returned rate from the gyro.
        """
    def getRotation3d(self) -> wpimath.geometry._geometry.Rotation3d:
        """
        Constructs a Rotation3d from the NavX quaternion.
        """
    def getVelocityX(self) -> float:
        """
        Returns the velocity (in meters/sec) of the X axis [Experimental].
        
        .. note:: This feature is experimental.  Velocity measures rely on integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting velocities are not known to be very accurate.
        
        :returns: Current Velocity (in meters/squared).
        """
    def getVelocityY(self) -> float:
        """
        Returns the velocity (in meters/sec) of the Y axis [Experimental].
        
        .. note:: This feature is experimental.  Velocity measures rely on integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting velocities are not known to be very accurate.
        
        :returns: Current Velocity (in meters/squared).
        """
    def getVelocityZ(self) -> float:
        """
        Returns the velocity (in meters/sec) of the X axis [Experimental].
        
        .. note:: This feature is experimental.  Velocity measures rely on integration
                  of acceleration values from MEMS accelerometers which yield "noisy" values.  The
                  resulting velocities are not known to be very accurate.
        
        :returns: Current Velocity (in meters/squared).
        """
    def getWorldLinearAccelX(self) -> float:
        """
        Returns the current linear acceleration in the X-axis (in G).
        
        World linear acceleration refers to raw acceleration data, which
        has had the gravity component removed, and which has been rotated to
        the same reference frame as the current yaw value.  The resulting
        value represents the current acceleration in the x-axis of the
        body (e.g., the robot) on which the sensor is mounted.
        
        :returns: Current world linear acceleration in the X-axis (in G).
        """
    def getWorldLinearAccelY(self) -> float:
        """
        Returns the current linear acceleration in the Y-axis (in G).
        
        World linear acceleration refers to raw acceleration data, which
        has had the gravity component removed, and which has been rotated to
        the same reference frame as the current yaw value.  The resulting
        value represents the current acceleration in the Y-axis of the
        body (e.g., the robot) on which the sensor is mounted.
        
        :returns: Current world linear acceleration in the Y-axis (in G).
        """
    def getWorldLinearAccelZ(self) -> float:
        """
        Returns the current linear acceleration in the Z-axis (in G).
        
        World linear acceleration refers to raw acceleration data, which
        has had the gravity component removed, and which has been rotated to
        the same reference frame as the current yaw value.  The resulting
        value represents the current acceleration in the Z-axis of the
        body (e.g., the robot) on which the sensor is mounted.
        
        :returns: Current world linear acceleration in the Z-axis (in G).
        """
    def getYaw(self) -> float:
        """
        Returns the current yaw value (in degrees, from -180 to 180)
        reported by the sensor.  Yaw is a measure of rotation around
        the Z Axis (which is perpendicular to the earth).
        
        Note that the returned yaw value will be offset by a user-specified
        offset value this user-specified offset value is set by
        invoking the zeroYaw() method.
        
        :returns: The current yaw value in degrees (-180 to 180).
        """
    def initSendable(self, builder: ntcore._ntcore.NTSendableBuilder) -> None:
        ...
    def isAltitudeValid(self) -> bool:
        """
        Indicates whether the current altitude (and barometric pressure) data is
        valid. This value will only be true for a sensor with an onboard
        pressure sensor installed.
        
        If this value is false for a board with an installed pressure sensor,
        this indicates a malfunction of the onboard pressure sensor.
        
        :returns: Returns true if a working pressure sensor is installed.
        """
    def isBoardlevelYawResetEnabled(self) -> bool:
        """
        Returns true if Board-level yaw resets are enabled.  Conversely, returns false
        if Software-based yaw resets are active.
        
        :returns: true if Board-level yaw resets are enabled.
        """
    def isCalibrating(self) -> bool:
        """
        Returns true if the sensor is currently performing automatic
        gyro/accelerometer calibration.  Automatic calibration occurs
        when the sensor is initially powered on, during which time the
        sensor should be held still, with the Z-axis pointing up
        (perpendicular to the earth).
        
        .. note::  During this automatic calibration, the yaw, pitch and roll
                   values returned may not be accurate.
        
        Once calibration is complete, the sensor will automatically remove
        an internal yaw offset value from all reported values.
        
        :returns: Returns true if the sensor is currently automatically
                  calibrating the gyro and accelerometer sensors.
        """
    def isConnected(self) -> bool:
        """
        Indicates whether the sensor is currently connected
        to the host computer.  A connection is considered established
        whenever communication with the sensor has occurred recently.
        
        :returns: Returns true if a valid update has been recently received
                  from the sensor.
        """
    def isMagneticDisturbance(self) -> bool:
        """
        Indicates whether the current magnetic field strength diverges from the
        calibrated value for the earth's magnetic field by more than the currently-
        configured Magnetic Disturbance Ratio.
        
        This function will always return false if the sensor's magnetometer has
        not yet been calibrated (see :meth:`isMagnetometerCalibrated`).
        
        :returns: true if a magnetic disturbance is detected (or the magnetometer is uncalibrated).
        """
    def isMagnetometerCalibrated(self) -> bool:
        """
        Indicates whether the magnetometer has been calibrated.
        
        Magnetometer Calibration must be performed by the user.
        
        Note that if this function does indicate the magnetometer is calibrated,
        this does not necessarily mean that the calibration quality is sufficient
        to yield valid compass headings.
        
        :returns: Returns true if magnetometer calibration has been performed.
        """
    def reset(self) -> None:
        """
        Reset the Yaw gyro.
        
        Resets the Gyro Z (Yaw) axis to a heading of zero. This can be used if
        there is significant drift in the gyro and it needs to be recalibrated
        after it has been running.
        """
    def resetDisplacement(self) -> None:
        """
        Zeros the displacement integration variables.   Invoke this at the moment when
        integration begins.
        """
    def setAngleAdjustment(self, angle: float) -> None:
        """
        Sets an amount of angle to be automatically added before returning a
        angle from the :meth:`getAngle` method.  This allows users of the ``getAngle`` method
        to logically rotate the sensor by a given amount of degrees.
        
        NOTE 1:  The adjustment angle is **only** applied to the value returned
        from ``getAngle`` - it does not adjust the value returned from :meth:`getYaw`, nor
        any of the quaternion values.
        
        NOTE 2:  The adjustment angle is **not** automatically cleared whenever the
        sensor yaw angle is reset.
        
        If not set, the default adjustment angle is 0 degrees (no adjustment).
        
        :param adjustment: Adjustment in degrees (range:  -360 to 360)
        """
    def updateDisplacement(self, accel_x_g: float, accel_y_g: float, update_rate_hz: int, is_moving: bool) -> None:
        ...
    def zeroYaw(self) -> None:
        """
        Sets the user-specified yaw offset to the current
        yaw value reported by the sensor.
        
        This user-specified yaw offset is automatically
        subtracted from subsequent yaw values reported by
        the getYaw() method.
        """
