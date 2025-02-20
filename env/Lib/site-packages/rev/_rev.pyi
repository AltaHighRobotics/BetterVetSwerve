from __future__ import annotations
import typing
import wpilib._wpilib
import wpilib.interfaces._interfaces
import wpimath._controls._controls.plant
import wpimath.units
__all__ = ['AbsoluteEncoder', 'AbsoluteEncoderConfig', 'AbsoluteEncoderConfigAccessor', 'AlternateEncoderConfig', 'AlternateEncoderConfigAccessor', 'AnalogInput', 'AnalogSensorConfig', 'AnalogSensorConfigAccessor', 'BaseConfig', 'CIEColor', 'ClosedLoopConfig', 'ClosedLoopConfigAccessor', 'ClosedLoopSlot', 'ColorMatch', 'ColorSensorV3', 'EncoderConfig', 'EncoderConfigAccessor', 'ExternalEncoderConfig', 'ExternalEncoderConfigAccessor', 'LimitSwitchConfig', 'LimitSwitchConfigAccessor', 'MAXMotionConfig', 'MAXMotionConfigAccessor', 'MovingAverageFilterSim', 'NoiseGenerator', 'REVLibError', 'RelativeEncoder', 'SignalsConfig', 'SignalsConfigAccessor', 'SmartMotionConfig', 'SmartMotionConfigAccessor', 'SoftLimitConfig', 'SoftLimitConfigAccessor', 'SparkAbsoluteEncoder', 'SparkAbsoluteEncoderSim', 'SparkAnalogSensor', 'SparkAnalogSensorSim', 'SparkBase', 'SparkBaseConfig', 'SparkBaseConfigAccessor', 'SparkClosedLoopController', 'SparkExternalEncoderSim', 'SparkFlex', 'SparkFlexConfig', 'SparkFlexConfigAccessor', 'SparkFlexExternalEncoder', 'SparkFlexSim', 'SparkLimitSwitch', 'SparkLimitSwitchSim', 'SparkLowLevel', 'SparkMax', 'SparkMaxAlternateEncoder', 'SparkMaxAlternateEncoderSim', 'SparkMaxConfig', 'SparkMaxConfigAccessor', 'SparkMaxSim', 'SparkParameter', 'SparkRelativeEncoder', 'SparkRelativeEncoderSim', 'SparkSim', 'SparkSimFaultManager']
class AbsoluteEncoder:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'rotations per minute' by default, and can be changed by a scale
        factor using setVelocityConversionFactor().
        
        :returns: Number of rotations per minute of the motor
        """
class AbsoluteEncoderConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: AbsoluteEncoderConfig) -> AbsoluteEncoderConfig:
        """
        Applies settings from another AbsoluteEncoderConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The AbsoluteEncoderConfig to copy settings from
        
        :returns: The updated AbsoluteEncoderConfig for method chaining
        """
    def averageDepth(self, depth: int) -> AbsoluteEncoderConfig:
        """
        Set the average sampling depth of the absolute encoder. This is a bit
        size and should be either 1, 2, 4, 8, 16, 32, 64, or 128 (default).
        
        :param depth: The average sampling depth of 1, 2, 4, 8, 16, 32, 64, or 128
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def endPulseUs(self, endPulseUs: float) -> AbsoluteEncoderConfig:
        """
        Set the length of the end pulse for this encoder. This pulse will be
        treated as the 1.0 position.
        
        :param endPulseUs: The minimum low pulse in microseconds
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def inverted(self, inverted: bool) -> AbsoluteEncoderConfig:
        """
        Set the phase of the absolute encoder so that it is in phase with the
        motor itself.
        
        :param inverted: The phase of the encoder
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def positionConversionFactor(self, factor: float) -> AbsoluteEncoderConfig:
        """
        Set the conversion factor for the position of the absolute encoder.
        Position is returned in native units of rotations and will be multiplied
        by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def setSparkMaxDataPortConfig(self) -> AbsoluteEncoderConfig:
        """
        Configures the data port to use the absolute encoder, which is
        specifically required for SPARK MAX.
        
        NOTE: This method is only necessary when using an absolute encoder
        with a SPARK MAX without configuring any of its settings
        
        IMPORTANT: SPARK MAX does not support using an absolute encoder in
        conjunction with an alternate encoder.
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def startPulseUs(self, startPulseUs: float) -> AbsoluteEncoderConfig:
        """
        Set the length of the start pulse for this encoder. This pulse will be
        treated as the 0.0 position.
        
        :param startPulseUs: The minimum high pulse in microseconds
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def velocityConversionFactor(self, factor: float) -> AbsoluteEncoderConfig:
        """
        Set the conversion factor for the velocity of the absolute encoder.
        Velocity is returned in native units of rotations per minute and will be
        multiplied by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def zeroCentered(self, zeroCentered: bool) -> AbsoluteEncoderConfig:
        """
        Set whether to enable zero-centering for the absolute encoder. If
        enabled, the position will be reported in the range (-0.5, 0.5], instead
        of the default range [0, 1), assuming the default units of rotations.
        
        :param zeroCentered: Whether to enable zero centering
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
    def zeroOffset(self, offset: float) -> AbsoluteEncoderConfig:
        """
        Set the zero offset of the absolute encoder, the position that is
        reported as zero.
        
        The zero offset is specified as the reported position of the encoder
        in the desired zero position as if the zero offset was set to 0, the
        position conversion factor was set to 1, and inverted was set to false.
        
        :param offset: The zero offset in the range [0, 1)
        
        :returns: The modified AbsoluteEncoderConfig object for method
                  chaining
        """
class AbsoluteEncoderConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getAverageDepth(self) -> int:
        ...
    def getEndPulseUs(self) -> float:
        ...
    def getInverted(self) -> bool:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getStartPulseUs(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getZeroOffset(self) -> float:
        ...
class AlternateEncoderConfig(BaseConfig):
    class Type:
        """
        Members:
        
          kQuadrature
        """
        __members__: typing.ClassVar[dict[str, AlternateEncoderConfig.Type]]  # value = {'kQuadrature': <Type.kQuadrature: 0>}
        kQuadrature: typing.ClassVar[AlternateEncoderConfig.Type]  # value = <Type.kQuadrature: 0>
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
    def fromId(id: int) -> AlternateEncoderConfig.Type:
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: AlternateEncoderConfig) -> AlternateEncoderConfig:
        """
        Applies settings from another AlternateEncoderConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The AlternateEncoderConfig to copy settings from
        
        :returns: The updated AlternateEncoderConfig for method chaining
        """
    def averageDepth(self, depth: int) -> AlternateEncoderConfig:
        """
        Set the sampling depth of the velocity calculation process of the
        alternate encoder. This value sets the number of samples in the average
        for velocity readings. For a quadrature encoder, this can be any value
        from 1 to 64 (default).
        
        :param depth: The velocity calculation process's sampling depth
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def countsPerRevolution(self, cpr: int) -> AlternateEncoderConfig:
        """
        Set the counts per revolutions of the alternate encoder.
        
        :param cpr: The counts per rotation
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def inverted(self, inverted: bool) -> AlternateEncoderConfig:
        """
        Set the phase of the alternate encoder so that it is in phase with the
        motor itself.
        
        :param inverted: The phase of the encoder
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def measurementPeriod(self, periodMs: int) -> AlternateEncoderConfig:
        """
        Set the position measurement period used to calculate the velocity of the
        alternate encoder. For a quadrature encoder, this number may be between 1
        and 100 (default).
        
        The basic formula to calculate velocity is change in position / change
        in time. This parameter sets the change in time for measurement.
        
        :param periodMs: Measurement period in milliseconds
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def positionConversionFactor(self, factor: float) -> AlternateEncoderConfig:
        """
        Set the conversion factor for the position of the alternate encoder.
        Position is returned in native units of rotations and will be multiplied
        by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def setSparkMaxDataPortConfig(self) -> AlternateEncoderConfig:
        """
        Configures the data port to use the alternate encoder, which is
        specifically required for SPARK MAX.
        
        NOTE: This method is only necessary when using an alternate encoder
        with a SPARK MAX without configuring any of its settings
        
        IMPORTANT: SPARK MAX does not support using an alternate encoder in
        conjunction with an absolute encoder and/or limit switches.
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
    def velocityConversionFactor(self, factor: float) -> AlternateEncoderConfig:
        """
        Set the conversion factor for the velocity of the alternate encoder.
        Velocity is returned in native units of rotations per minute and will be
        multiplied by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AlternateEncoderConfig object for method
                  chaining
        """
class AlternateEncoderConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getCountsPerRevolution(self) -> int:
        ...
    def getInverted(self) -> bool:
        ...
    def getMeasurementPeriod(self) -> int:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
class AnalogInput:
    """
    Get an instance of AnalogInput by using
    SparkBase::GetAnalog(SparkAnalogSensor::Mode)}.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. Returns value in the native unit
        of 'volt' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Position of the sensor in volts
        """
    def getVoltage(self) -> float:
        """
        Get the voltage of the analog sensor.
        
        :returns: Voltage of the sensor
        """
class AnalogSensorConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: AnalogSensorConfig) -> AnalogSensorConfig:
        """
        Applies settings from another AnalogSensorConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The AnalogSensorConfig to copy settings from
        
        :returns: The updated AnalogSensorConfig for method chaining
        """
    def inverted(self, inverted: bool) -> AnalogSensorConfig:
        """
        Set the phase of the analog sensor so that it is in phase with the motor
        itself.
        
        :param inverted: The phase of the analog sensor
        
        :returns: The modified AnalogSensorConfig object for method
                  chaining
        """
    def positionConversionFactor(self, factor: float) -> AnalogSensorConfig:
        """
        Set the conversion factor for the position of the analog sensor. Position
        is returned in native units of volts and will be multiplied by this
        conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AnalogSensorConfig object for method
                  chaining
        """
    def velocityConversionFactor(self, factor: float) -> AnalogSensorConfig:
        """
        Set the conversion factor for the velocity of the analog sensor. Velocity
        is returned in native units of volts per second and will be multiplied by
        this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified AnalogSensorConfig object for method
                  chaining
        """
class AnalogSensorConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getInverted(self) -> bool:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
class BaseConfig:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def flatten(self) -> str:
        ...
class CIEColor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, X: float, Y: float, Z: float) -> None:
        ...
    def getX(self) -> float:
        """
        Get the X component of the color
        
        :returns: CIE X
        """
    def getY(self) -> float:
        """
        Get the Y component of the color
        
        :returns: CIE Y
        """
    def getYx(self) -> float:
        """
        Get the x calculated coordinate
        of the CIE 19313 color space
        
        https://en.wikipedia.org/wiki/CIE_1931_color_space
        
        :returns: CIE Yx
        """
    def getYy(self) -> float:
        """
        Get the y calculated coordinate
        of the CIE 19313 color space
        
        https://en.wikipedia.org/wiki/CIE_1931_color_space
        
        :returns: CIE Yy
        """
    def getZ(self) -> float:
        """
        Get the Z component of the color
        
        :returns: CIE Z
        """
class ClosedLoopConfig(BaseConfig):
    class FeedbackSensor:
        """
        Members:
        
          kNoSensor
        
          kPrimaryEncoder
        
          kAnalogSensor
        
          kAlternateOrExternalEncoder
        
          kAbsoluteEncoder
        """
        __members__: typing.ClassVar[dict[str, ClosedLoopConfig.FeedbackSensor]]  # value = {'kNoSensor': <FeedbackSensor.kNoSensor: 0>, 'kPrimaryEncoder': <FeedbackSensor.kPrimaryEncoder: 1>, 'kAnalogSensor': <FeedbackSensor.kAnalogSensor: 2>, 'kAlternateOrExternalEncoder': <FeedbackSensor.kAlternateOrExternalEncoder: 3>, 'kAbsoluteEncoder': <FeedbackSensor.kAbsoluteEncoder: 4>}
        kAbsoluteEncoder: typing.ClassVar[ClosedLoopConfig.FeedbackSensor]  # value = <FeedbackSensor.kAbsoluteEncoder: 4>
        kAlternateOrExternalEncoder: typing.ClassVar[ClosedLoopConfig.FeedbackSensor]  # value = <FeedbackSensor.kAlternateOrExternalEncoder: 3>
        kAnalogSensor: typing.ClassVar[ClosedLoopConfig.FeedbackSensor]  # value = <FeedbackSensor.kAnalogSensor: 2>
        kNoSensor: typing.ClassVar[ClosedLoopConfig.FeedbackSensor]  # value = <FeedbackSensor.kNoSensor: 0>
        kPrimaryEncoder: typing.ClassVar[ClosedLoopConfig.FeedbackSensor]  # value = <FeedbackSensor.kPrimaryEncoder: 1>
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
    def D(self, d: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the derivative gain of the controller for a specific closed loop
        slot.
        
        :param d:    The derivative gain value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def DFilter(self, dFilter: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the derivative filter of the controller for a specific closed loop
        slot.
        
        :param dFilter: The derivative filter value
        :param slot:    The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def I(self, i: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the integral gain of the controller for a specific closed loop slot.
        
        :param i:    The integral gain value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def IMaxAccum(self, iMaxAccum: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the maximum I accumulator of the controller for a specific closed
        loop slot. This value is used to constrain the I accumulator to help
        manage integral wind-up.
        
        :param iMaxAccum: The max value to constrain the I accumulator to
        :param slot:      The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def IZone(self, iZone: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the integral zone of the controller for a specific closed loop slot.
        
        :param iZone: The integral zone value
        :param slot:  The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def P(self, p: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the proportional gain of the controller for a specific closed loop
        slot.
        
        :param p:    The proportional gain value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def __init__(self) -> None:
        ...
    @typing.overload
    def apply(self, config: ClosedLoopConfig) -> ClosedLoopConfig:
        """
        Applies settings from another ClosedLoopConfig to this one,
        including all of its nested configurations.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The ClosedLoopConfig to copy settings from
        
        :returns: The updated ClosedLoopConfig for method chaining
        """
    @typing.overload
    def apply(self, config: SmartMotionConfig) -> ClosedLoopConfig:
        """
        Applies settings from a SmartMotionConfig to this ClosedLoopConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SmartMotionConfig to copy settings from
        
        :returns: The updated ClosedLoopConfig for method chaining
        """
    @typing.overload
    def apply(self, config: MAXMotionConfig) -> ClosedLoopConfig:
        """
        Applies settings from a MAXMotionConfig to this {@link
        ClosedLoopConfig}.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The MAXMotionConfig to copy settings from
        
        :returns: The updated ClosedLoopConfig for method chaining
        """
    def flatten(self) -> str:
        ...
    def maxOutput(self, maxOutput: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the maximum output of the controller for a specific closed loop slot.
        
        :param maxOutput: The maximum output value in the range [-1, 1]
        :param slot:      The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def minOutput(self, minOutput: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the minimum output of the controller for a specific closed loop slot.
        
        :param minOutput: The minimum output value in the range [-1, 1]
        :param slot:      The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def outputRange(self, minOutput: float, maxOutput: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the output range of the controller for a specific closed loop slot.
        
        :param minOutput: The minimum output value in the range [-1, 1]
        :param maxOutput: The maximum output value in the range [-1, 1]
        :param slot:      The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def pid(self, p: float, i: float, d: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the PID gains of the controller for a specific closed loop slot.
        
        :param p:    The proportional gain value
        :param i:    The integral gain value
        :param d:    The derivative gain value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def pidf(self, p: float, i: float, d: float, ff: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the PIDF gains of the controller for a specific closed loop slot.
        
        :param p:    The proportional gain value
        :param i:    The integral gain value
        :param d:    The derivative gain value
        :param ff:   The velocity feedforward value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def positionWrappingEnabled(self, enabled: bool) -> ClosedLoopConfig:
        """
        Enable or disable PID wrapping for position closed loop control.
        
        :param enabled: True to enable position PID wrapping
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def positionWrappingInputRange(self, minInput: float, maxInput: float) -> ClosedLoopConfig:
        """
        Set the input range for PID wrapping with position closed loop control
        
        :param minInput: The value of min input for the position
        :param maxInput: The value of max input for the position
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def positionWrappingMaxInput(self, maxInput: float) -> ClosedLoopConfig:
        """
        Set the maximum input value for PID wrapping with position closed loop
        control
        
        :param maxInput: The value of max input for the position
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def positionWrappingMinInput(self, minInput: float) -> ClosedLoopConfig:
        """
        Set the minimum input value for PID wrapping with position closed loop
        control.
        
        :param minInput: The value of min input for the position
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def setFeedbackSensor(self, sensor: ClosedLoopConfig.FeedbackSensor) -> ClosedLoopConfig:
        """
        Set the feedback sensor of the controller. The controller will use this
        sensor as the source of feedback for its closed loop control.
        
        The default feedback sensor is assumed to be the primary encoder for
        either brushless or brushed mode. This can be changed to another feedback
        sensor for the controller such as an analog sensor, absolute encoder, or
        alternate/external encoder.
        
        :param sensor: The feedback sensor
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    def velocityFF(self, ff: float, slot: ClosedLoopSlot = ...) -> ClosedLoopConfig:
        """
        Set the velocity feedforward gain of the controller for a specific closed
        loop slot.
        
        :param ff:   The velocity feedforward gain value
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified ClosedLoopConfig object for method chaining
        """
    @property
    def maxMotion(self) -> MAXMotionConfig:
        ...
    @property
    def smartMotion(self) -> SmartMotionConfig:
        ...
class ClosedLoopConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getD(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getDFilter(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getFF(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getFeedbackSensor(self) -> ClosedLoopConfig.FeedbackSensor:
        ...
    def getI(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getIZone(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxIAccumulation(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxOutput(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMinOutput(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getP(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getPositionWrappingEnabled(self) -> bool:
        ...
    def getPositionWrappingMaxInput(self) -> float:
        ...
    def getPositionWrappingMinInput(self) -> float:
        ...
    @property
    def maxMotion(self) -> MAXMotionConfigAccessor:
        ...
    @property
    def smartMotion(self) -> SmartMotionConfigAccessor:
        ...
class ClosedLoopSlot:
    """
    Members:
    
      kSlot0
    
      kSlot1
    
      kSlot2
    
      kSlot3
    """
    __members__: typing.ClassVar[dict[str, ClosedLoopSlot]]  # value = {'kSlot0': <ClosedLoopSlot.kSlot0: 0>, 'kSlot1': <ClosedLoopSlot.kSlot1: 1>, 'kSlot2': <ClosedLoopSlot.kSlot2: 2>, 'kSlot3': <ClosedLoopSlot.kSlot3: 3>}
    kSlot0: typing.ClassVar[ClosedLoopSlot]  # value = <ClosedLoopSlot.kSlot0: 0>
    kSlot1: typing.ClassVar[ClosedLoopSlot]  # value = <ClosedLoopSlot.kSlot1: 1>
    kSlot2: typing.ClassVar[ClosedLoopSlot]  # value = <ClosedLoopSlot.kSlot2: 2>
    kSlot3: typing.ClassVar[ClosedLoopSlot]  # value = <ClosedLoopSlot.kSlot3: 3>
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
class ColorMatch:
    """
    REV Robotics Color Sensor V3.
    
    This class allows access to a REV Robotics color sensor V3 on an I2C bus.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def addColorMatch(self, color: wpilib._wpilib.Color) -> None:
        """
        Add color to match object
        
        :param color: color to add to matching
        """
    def matchClosestColor(self, colorToMatch: wpilib._wpilib.Color) -> tuple[wpilib._wpilib.Color, float]:
        """
        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values
        
        :param colorToMatch: color to compare against stored colors
        :param confidence:   The confidence value for this match, this is
                             simply 1 - euclidean distance of the two color vectors
        
        :returns: Closest matching color
        """
    @typing.overload
    def matchColor(self, colorToMatch: wpilib._wpilib.Color) -> wpilib._wpilib.Color | None:
        """
        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values
        
        :param colorToMatch: color to compare against stored colors
        
        :returns: Matched color if detected
        """
    @typing.overload
    def matchColor(self, colorToMatch: wpilib._wpilib.Color) -> tuple[wpilib._wpilib.Color | None, float]:
        """
        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values
        
        :param colorToMatch: color to compare against stored colors
        :param confidence:   The confidence value for this match, this is
                             simply 1 - euclidean distance of the two color vectors
        
        :returns: Matched color if detected
        """
    def setConfidenceThreshold(self, confidence: float) -> None:
        """
        Set the confidence interval for determining color. Defaults to 0.95
        
        :param confidence: A value between 0 and 1
        """
class ColorSensorV3:
    """
    REV Robotics Color Sensor V3.
    
    This class allows access to a REV Robotics color sensor V3 on an I2C bus.
    """
    class ColorMeasurementRate:
        """
        Members:
        
          k25ms
        
          k50ms
        
          k100ms
        
          k200ms
        
          k500ms
        
          k1000ms
        
          k2000ms
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.ColorMeasurementRate]]  # value = {'k25ms': <ColorMeasurementRate.k25ms: 0>, 'k50ms': <ColorMeasurementRate.k50ms: 1>, 'k100ms': <ColorMeasurementRate.k100ms: 2>, 'k200ms': <ColorMeasurementRate.k200ms: 3>, 'k500ms': <ColorMeasurementRate.k500ms: 4>, 'k1000ms': <ColorMeasurementRate.k1000ms: 5>, 'k2000ms': <ColorMeasurementRate.k2000ms: 7>}
        k1000ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k1000ms: 5>
        k100ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k100ms: 2>
        k2000ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k2000ms: 7>
        k200ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k200ms: 3>
        k25ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k25ms: 0>
        k500ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k500ms: 4>
        k50ms: typing.ClassVar[ColorSensorV3.ColorMeasurementRate]  # value = <ColorMeasurementRate.k50ms: 1>
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
    class ColorResolution:
        """
        Members:
        
          k20bit
        
          k19bit
        
          k18bit
        
          k17bit
        
          k16bit
        
          k13bit
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.ColorResolution]]  # value = {'k20bit': <ColorResolution.k20bit: 0>, 'k19bit': <ColorResolution.k19bit: 16>, 'k18bit': <ColorResolution.k18bit: 32>, 'k17bit': <ColorResolution.k17bit: 48>, 'k16bit': <ColorResolution.k16bit: 64>, 'k13bit': <ColorResolution.k13bit: 80>}
        k13bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k13bit: 80>
        k16bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k16bit: 64>
        k17bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k17bit: 48>
        k18bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k18bit: 32>
        k19bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k19bit: 16>
        k20bit: typing.ClassVar[ColorSensorV3.ColorResolution]  # value = <ColorResolution.k20bit: 0>
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
    class GainFactor:
        """
        Members:
        
          k1x
        
          k3x
        
          k6x
        
          k9x
        
          k18x
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.GainFactor]]  # value = {'k1x': <GainFactor.k1x: 0>, 'k3x': <GainFactor.k3x: 1>, 'k6x': <GainFactor.k6x: 2>, 'k9x': <GainFactor.k9x: 3>, 'k18x': <GainFactor.k18x: 4>}
        k18x: typing.ClassVar[ColorSensorV3.GainFactor]  # value = <GainFactor.k18x: 4>
        k1x: typing.ClassVar[ColorSensorV3.GainFactor]  # value = <GainFactor.k1x: 0>
        k3x: typing.ClassVar[ColorSensorV3.GainFactor]  # value = <GainFactor.k3x: 1>
        k6x: typing.ClassVar[ColorSensorV3.GainFactor]  # value = <GainFactor.k6x: 2>
        k9x: typing.ClassVar[ColorSensorV3.GainFactor]  # value = <GainFactor.k9x: 3>
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
    class LEDCurrent:
        """
        Members:
        
          kPulse2mA
        
          kPulse5mA
        
          kPulse10mA
        
          kPulse25mA
        
          kPulse50mA
        
          kPulse75mA
        
          kPulse100mA
        
          kPulse125mA
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.LEDCurrent]]  # value = {'kPulse2mA': <LEDCurrent.kPulse2mA: 0>, 'kPulse5mA': <LEDCurrent.kPulse5mA: 1>, 'kPulse10mA': <LEDCurrent.kPulse10mA: 2>, 'kPulse25mA': <LEDCurrent.kPulse25mA: 3>, 'kPulse50mA': <LEDCurrent.kPulse50mA: 4>, 'kPulse75mA': <LEDCurrent.kPulse75mA: 5>, 'kPulse100mA': <LEDCurrent.kPulse100mA: 6>, 'kPulse125mA': <LEDCurrent.kPulse125mA: 7>}
        kPulse100mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse100mA: 6>
        kPulse10mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse10mA: 2>
        kPulse125mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse125mA: 7>
        kPulse25mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse25mA: 3>
        kPulse2mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse2mA: 0>
        kPulse50mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse50mA: 4>
        kPulse5mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse5mA: 1>
        kPulse75mA: typing.ClassVar[ColorSensorV3.LEDCurrent]  # value = <LEDCurrent.kPulse75mA: 5>
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
    class LEDPulseFrequency:
        """
        Members:
        
          k60kHz
        
          k70kHz
        
          k80kHz
        
          k90kHz
        
          k100kHz
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.LEDPulseFrequency]]  # value = {'k60kHz': <LEDPulseFrequency.k60kHz: 24>, 'k70kHz': <LEDPulseFrequency.k70kHz: 64>, 'k80kHz': <LEDPulseFrequency.k80kHz: 40>, 'k90kHz': <LEDPulseFrequency.k90kHz: 48>, 'k100kHz': <LEDPulseFrequency.k100kHz: 56>}
        k100kHz: typing.ClassVar[ColorSensorV3.LEDPulseFrequency]  # value = <LEDPulseFrequency.k100kHz: 56>
        k60kHz: typing.ClassVar[ColorSensorV3.LEDPulseFrequency]  # value = <LEDPulseFrequency.k60kHz: 24>
        k70kHz: typing.ClassVar[ColorSensorV3.LEDPulseFrequency]  # value = <LEDPulseFrequency.k70kHz: 64>
        k80kHz: typing.ClassVar[ColorSensorV3.LEDPulseFrequency]  # value = <LEDPulseFrequency.k80kHz: 40>
        k90kHz: typing.ClassVar[ColorSensorV3.LEDPulseFrequency]  # value = <LEDPulseFrequency.k90kHz: 48>
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
    class ProximityMeasurementRate:
        """
        Members:
        
          k6ms
        
          k12ms
        
          k25ms
        
          k50ms
        
          k100ms
        
          k200ms
        
          k400ms
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.ProximityMeasurementRate]]  # value = {'k6ms': <ProximityMeasurementRate.k6ms: 1>, 'k12ms': <ProximityMeasurementRate.k12ms: 2>, 'k25ms': <ProximityMeasurementRate.k25ms: 3>, 'k50ms': <ProximityMeasurementRate.k50ms: 4>, 'k100ms': <ProximityMeasurementRate.k100ms: 5>, 'k200ms': <ProximityMeasurementRate.k200ms: 6>, 'k400ms': <ProximityMeasurementRate.k400ms: 7>}
        k100ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k100ms: 5>
        k12ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k12ms: 2>
        k200ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k200ms: 6>
        k25ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k25ms: 3>
        k400ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k400ms: 7>
        k50ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k50ms: 4>
        k6ms: typing.ClassVar[ColorSensorV3.ProximityMeasurementRate]  # value = <ProximityMeasurementRate.k6ms: 1>
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
    class ProximityResolution:
        """
        Members:
        
          k8bit
        
          k9bit
        
          k10bit
        
          k11bit
        """
        __members__: typing.ClassVar[dict[str, ColorSensorV3.ProximityResolution]]  # value = {'k8bit': <ProximityResolution.k8bit: 0>, 'k9bit': <ProximityResolution.k9bit: 8>, 'k10bit': <ProximityResolution.k10bit: 16>, 'k11bit': <ProximityResolution.k11bit: 24>}
        k10bit: typing.ClassVar[ColorSensorV3.ProximityResolution]  # value = <ProximityResolution.k10bit: 16>
        k11bit: typing.ClassVar[ColorSensorV3.ProximityResolution]  # value = <ProximityResolution.k11bit: 24>
        k8bit: typing.ClassVar[ColorSensorV3.ProximityResolution]  # value = <ProximityResolution.k8bit: 0>
        k9bit: typing.ClassVar[ColorSensorV3.ProximityResolution]  # value = <ProximityResolution.k9bit: 8>
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
    class RawColor:
        blue: int
        green: int
        ir: int
        red: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self, r: int, g: int, b: int, _ir: int) -> None:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, port: wpilib._wpilib.I2C.Port) -> None:
        """
        Constructs a ColorSensorV3.
        
        Note that the REV Color Sensor is really two devices in one package:
        a color sensor providing red, green, blue and IR values, and a proximity
        sensor.
        
        :param port: The I2C port the color sensor is attached to
        """
    def configureColorSensor(self, res: ColorSensorV3.ColorResolution, rate: ColorSensorV3.ColorMeasurementRate) -> None:
        """
        Configure the color sensor.
        
        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        color sensor measurements.
        
        :param res:  Bit resolution output by the respective light sensor ADCs
        :param rate: Measurement rate of the light sensor
        """
    def configureProximitySensor(self, res: ColorSensorV3.ProximityResolution, rate: ColorSensorV3.ProximityMeasurementRate) -> None:
        """
        Configure the proximity sensor.
        
        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        proximity sensor measurements.
        
        :param res:  Bit resolution output by the proximity sensor ADC.
        :param rate: Measurement rate of the proximity sensor
        """
    def configureProximitySensorLED(self, freq: ColorSensorV3.LEDPulseFrequency, current: ColorSensorV3.LEDCurrent, pulses: int) -> None:
        """
        Configure the the IR LED used by the proximity sensor.
        
        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        proximity sensor measurements.
        
        :param freq:    The pulse modulation frequency for the proximity
                        sensor LED
        :param current: The pulse current for the proximity sensor LED
        :param pulses:  The number of pulses per measurement of the
                        proximity sensor LED
        """
    def getCIEColor(self) -> CIEColor:
        """
        Get the color converted to CIE XYZ color space using factory
        calibrated constants.
        
        https://en.wikipedia.org/wiki/CIE_1931_color_space
        
        :returns: CIEColor value from sensor
        """
    def getColor(self) -> wpilib._wpilib.Color:
        """
        Get the normalized RGB color from the sensor (normalized based on
        total R + G + B)
        
        :returns: frc::Color class with normalized sRGB values
        """
    def getIR(self) -> float:
        """
        Get the normalzied IR value from the sensor. Works best when within 2
        inches and perpendicular to surface of interest.
        
        :returns: Color class with normalized values
        """
    def getProximity(self) -> int:
        """
        Get the raw proximity value from the sensor ADC. This value is largest
        when an object is close to the sensor and smallest when
        far away.
        
        :returns: Proximity measurement value, ranging from 0 to 2047 in
                  default configuration
        """
    def getRawColor(self) -> ColorSensorV3.RawColor:
        """
        Get the raw color value from the sensor.
        
        :returns: Raw color values from sensopr
        """
    def hasReset(self) -> bool:
        """
        Indicates if the device reset. Based on the power on status flag in the
        status register. Per the datasheet:
        
        Part went through a power-up event, either because the part was turned
        on or because there was power supply voltage disturbance (default at
        first register read).
        
        This flag is self clearing
        
        :returns: true if the device was reset
        """
    def isConnected(self) -> bool:
        """
        Indicates if the device can currently be communicated with.
        
        :returns: true if the device is currently connected and responsive
        """
    def setGain(self, gain: ColorSensorV3.GainFactor) -> None:
        """
        Set the gain factor applied to color ADC measurements.
        
        By default, the gain is set to 3x.
        
        :param gain: Gain factor applied to color ADC measurements
                     measurements
        """
class EncoderConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: EncoderConfig) -> EncoderConfig:
        """
        Applies settings from another EncoderConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The EncoderConfig to copy settings from
        
        :returns: The updated EncoderConfig for method chaining
        """
    def countsPerRevolution(self, cpr: int) -> EncoderConfig:
        """
        Set the counts per revolutions of the encoder.
        
        NOTE: This only applies to an encoder used in brushed mode.
        
        :param cpr: The counts per rotation
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def inverted(self, inverted: bool) -> EncoderConfig:
        """
        Set the phase of the encoder so that it is in phase with the motor
        itself.
        
        NOTE: This only applies to an encoder used in brushed mode.
        
        :param inverted: The phase of the encoder
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def positionConversionFactor(self, factor: float) -> EncoderConfig:
        """
        Set the conversion factor for the position of the encoder. Position is
        returned in native units of rotations and will be multiplied by this
        conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def quadratureAverageDepth(self, depth: int) -> EncoderConfig:
        """
        Set the sampling depth of the velocity calculation process of the
        encoder. This value sets the number of samples in the average for
        velocity readings. This value must be in the range [1, 64]. The default
        value is 64.
        
        :param depth: The velocity calculation process's sampling depth
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def quadratureMeasurementPeriod(self, periodMs: int) -> EncoderConfig:
        """
        Set the position measurement period used to calculate the velocity of the
        encoder. This value is in units of milliseconds and must be in a range
        [1, 100]. The default value is 100ms
        
        The basic formula to calculate velocity is change in position / change
        in time. This parameter sets the change in time for measurement.
        
        :param periodMs: Measurement period in milliseconds
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def uvwAverageDepth(self, depth: int) -> EncoderConfig:
        """
        Set the sampling depth of the velocity calculation process of the
        encoder. This value sets the number of samples in the average for
        velocity readings. This value must be either 1, 2, 4, or 8 (default).
        
        :param depth: The velocity calculation process's sampling depth
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def uvwMeasurementPeriod(self, periodMs: int) -> EncoderConfig:
        """
        Set the position measurement period used to calculate the velocity of the
        encoder. This value is in units of milliseconds and must be in a range
        [8, 64]. The default value is 32ms.
        
        The basic formula to calculate velocity is change in position / change
        in time. This parameter sets the change in time for measurement.
        
        :param periodMs: Measurement period in milliseconds
        
        :returns: The modified EncoderConfig object for method chaining
        """
    def velocityConversionFactor(self, factor: float) -> EncoderConfig:
        """
        Set the conversion factor for the velocity of the encoder. Velocity is
        returned in native units of rotations per minute and will be multiplied
        by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified EncoderConfig object for method chaining
        """
class EncoderConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getCountsPerRevolution(self) -> int:
        ...
    def getInverted(self) -> bool:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getQuadratureAverageDepth(self) -> int:
        ...
    def getQuadratureMeasurementPeriod(self) -> int:
        ...
    def getUvwAverageDepth(self) -> int:
        ...
    def getUvwMeasurementPeriod(self) -> int:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
class ExternalEncoderConfig(BaseConfig):
    class Type:
        """
        Members:
        
          kQuadrature
        """
        __members__: typing.ClassVar[dict[str, ExternalEncoderConfig.Type]]  # value = {'kQuadrature': <Type.kQuadrature: 0>}
        kQuadrature: typing.ClassVar[ExternalEncoderConfig.Type]  # value = <Type.kQuadrature: 0>
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
    def fromId(id: int) -> ExternalEncoderConfig.Type:
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: ExternalEncoderConfig) -> ExternalEncoderConfig:
        """
        Applies settings from another ExternalEncoderConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The ExternalEncoderConfig to copy settings from
        
        :returns: The updated ExternalEncoderConfig for method chaining
        """
    def averageDepth(self, depth: int) -> ExternalEncoderConfig:
        """
        Set the sampling depth of the velocity calculation process of the
        External encoder. This value sets the number of samples in the average
        for velocity readings. For a quadrature encoder, this can be any value
        from 1 to 64 (default).
        
        :param depth: The velocity calculation process's sampling depth
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
    def countsPerRevolution(self, cpr: int) -> ExternalEncoderConfig:
        """
        Set the counts per revolutions of the External encoder.
        
        :param cpr: The counts per rotation
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
    def inverted(self, inverted: bool) -> ExternalEncoderConfig:
        """
        Set the phase of the External encoder so that it is in phase with the
        motor itself.
        
        :param inverted: The phase of the encoder
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
    def measurementPeriod(self, periodMs: int) -> ExternalEncoderConfig:
        """
        Set the position measurement period used to calculate the velocity of the
        External encoder. For a quadrature encoder, this number may be between 1
        and 100 (default).
        
        The basic formula to calculate velocity is change in position / change
        in time. This parameter sets the change in time for measurement.
        
        :param periodMs: Measurement period in milliseconds
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
    def positionConversionFactor(self, factor: float) -> ExternalEncoderConfig:
        """
        Set the conversion factor for the position of the External encoder.
        Position is returned in native units of rotations and will be multiplied
        by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
    def velocityConversionFactor(self, factor: float) -> ExternalEncoderConfig:
        """
        Set the conversion factor for the velocity of the External encoder.
        Velocity is returned in native units of rotations per minute and will be
        multiplied by this conversion factor.
        
        :param factor: The conversion factor to multiply the native units by
        
        :returns: The modified ExternalEncoderConfig object for method
                  chaining
        """
class ExternalEncoderConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getAverageDepth(self) -> int:
        ...
    def getCountsPerRevolution(self) -> int:
        ...
    def getInverted(self) -> bool:
        ...
    def getMeasurementPeriod(self) -> int:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
class LimitSwitchConfig(BaseConfig):
    class Type:
        """
        Members:
        
          kNormallyOpen
        
          kNormallyClosed
        """
        __members__: typing.ClassVar[dict[str, LimitSwitchConfig.Type]]  # value = {'kNormallyOpen': <Type.kNormallyOpen: 0>, 'kNormallyClosed': <Type.kNormallyClosed: 1>}
        kNormallyClosed: typing.ClassVar[LimitSwitchConfig.Type]  # value = <Type.kNormallyClosed: 1>
        kNormallyOpen: typing.ClassVar[LimitSwitchConfig.Type]  # value = <Type.kNormallyOpen: 0>
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
    def __init__(self) -> None:
        ...
    def apply(self, config: LimitSwitchConfig) -> LimitSwitchConfig:
        """
        Applies settings from another LimitSwitchConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The LimitSwitchConfig to copy settings from
        
        :returns: The updated LimitSwitchConfig for method chaining
        """
    def forwardLimitSwitchEnabled(self, enabled: bool) -> LimitSwitchConfig:
        """
        Set whether to enable or disable motor shutdown based on the forward
        limit switch state. This does not not affect the result of the
        isPressed() command.
        
        :param enabled: True to enable motor shutdown behavior
        
        :returns: The modified LimitSwitchConfig object for method chaining
        """
    def forwardLimitSwitchType(self, type: LimitSwitchConfig.Type) -> LimitSwitchConfig:
        """
        Set the normal state of the forward limit switch.
        
        :param type: kNormallyOpen or kNormallyClosed
        
        :returns: The modified LimitSwitchConfig object for method chaining
        """
    def reverseLimitSwitchEnabled(self, enabled: bool) -> LimitSwitchConfig:
        """
        Set whether to enable or disable motor shutdown based on the reverse
        limit switch state. This does not not affect the result of the
        isPressed() command.
        
        :param enabled: True to enable motor shutdown behavior
        
        :returns: The modified LimitSwitchConfig object for method chaining
        """
    def reverseLimitSwitchType(self, type: LimitSwitchConfig.Type) -> LimitSwitchConfig:
        """
        Set the normal state of the reverse limit switch.
        
        :param type: kNormallyOpen or kNormallyClosed
        
        :returns: The modified LimitSwitchConfig object for method chaining
        """
    def setSparkMaxDataPortConfig(self) -> LimitSwitchConfig:
        """
        Configures the data port to use limit switches, which is specifically
        required for SPARK MAX.
        
        NOTE: This method is only necessary when using limit switches with a
        SPARK MAX without configuring any of its settings
        
        IMPORTANT: SPARK MAX does not support using limit switches in
        conjunction with an alternate encoder.
        
        :returns: The modified LimitSwitchConfig object for method chaining
        """
class LimitSwitchConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getForwardLimitSwitchEnabled(self) -> bool:
        ...
    def getForwardSwitchType(self) -> LimitSwitchConfig.Type:
        ...
    def getReverseLimitSwitchEnabled(self) -> bool:
        ...
    def getReverseSwitchType(self) -> LimitSwitchConfig.Type:
        ...
class MAXMotionConfig(BaseConfig):
    class MAXMotionPositionMode:
        """
        Members:
        
          kMAXMotionTrapezoidal
        """
        __members__: typing.ClassVar[dict[str, MAXMotionConfig.MAXMotionPositionMode]]  # value = {'kMAXMotionTrapezoidal': <MAXMotionPositionMode.kMAXMotionTrapezoidal: 0>}
        kMAXMotionTrapezoidal: typing.ClassVar[MAXMotionConfig.MAXMotionPositionMode]  # value = <MAXMotionPositionMode.kMAXMotionTrapezoidal: 0>
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
    def __init__(self) -> None:
        ...
    def allowedClosedLoopError(self, allowedError: float, slot: ClosedLoopSlot = ...) -> MAXMotionConfig:
        """
        Set the allowed closed loop error for the MAXMotion mode of the
        controller for a specific PID slot. This value is how much deviation from
        the setpoint is tolerated and is useful in preventing oscillation around
        the setpoint. Natively, the units are in rotations but will be affected
        by the position conversion factor.
        
        :param allowedError: The allowed error with the position conversion factor
                             applied
        :param slot:         The closed loop slot to set the values for
        
        :returns: The modified MAXMotionConfig object for method chaining
        """
    def apply(self, config: MAXMotionConfig) -> MAXMotionConfig:
        """
        Applies settings from another MAXMotionConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The MAXMotionConfig to copy settings from
        
        :returns: The updated MAXMotionConfig for method chaining
        """
    def maxAcceleration(self, maxAcceleration: float, slot: ClosedLoopSlot = ...) -> MAXMotionConfig:
        """
        Set the maximum acceleration for the MAXMotion mode of the controller for
        a specific closed loop slot. This is the rate at which the velocity will
        increase until the max velocity is reached. Natively, the units are in
        RPM per second but will be affected by the velocity conversion factor.
        
        :param maxAcceleration: The maximum acceleration with the velocity
                                conversion factor applied
        :param slot:            The closed loop slot to set the values for
        
        :returns: The modified MAXMotionConfig object for method chaining
        """
    def maxVelocity(self, maxVelocity: float, slot: ClosedLoopSlot = ...) -> MAXMotionConfig:
        """
        Set the maximum velocity for the MAXMotion mode of the controller for a
        specific closed loop slot. This is the cruising velocity of the profile.
        Natively, the units are in RPM but will be affected by the velocity
        conversion factor.
        
        :param maxVelocity: The maximum velocity with the velocity conversion
                            factor applied
        :param slot:        The closed loop slot to set the values for
        
        :returns: The modified MAXMotionConfig object for method chaining
        """
    def positionMode(self, mode: MAXMotionConfig.MAXMotionPositionMode, slot: ClosedLoopSlot = ...) -> MAXMotionConfig:
        """
        Set the MAXMotion position control mode of the controller for a specific
        closed loop slot.
        
        :param mode: The MAXmotion position mode
        :param slot: The closed loop slot to set the values for
        
        :returns: The modified MAXMotionConfig object for method chaining
        """
class MAXMotionConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getAllowedClosedLoopError(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxAcceleration(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxVelocity(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getPositionMode(self, slot: ClosedLoopSlot = ...) -> MAXMotionConfig.MAXMotionPositionMode:
        ...
class MovingAverageFilterSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, taps: int, sampleRate: float) -> None:
        ...
    def get(self) -> float:
        ...
    def put(self, value: float, delta: float) -> None:
        ...
class NoiseGenerator:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def hallSensorVelocity(speedRPM: float) -> float:
        ...
    @staticmethod
    def whiteNoise(input: float, variance: float) -> float:
        ...
    def __init__(self) -> None:
        ...
class REVLibError:
    """
    Members:
    
      kOk
    
      kError
    
      kTimeout
    
      kNotImplemented
    
      kHALError
    
      kCantFindFirmware
    
      kFirmwareTooOld
    
      kFirmwareTooNew
    
      kParamInvalidID
    
      kParamMismatchType
    
      kParamAccessMode
    
      kParamInvalid
    
      kParamNotImplementedDeprecated
    
      kFollowConfigMismatch
    
      kInvalid
    
      kSetpointOutOfRange
    
      kUnknown
    
      kCANDisconnected
    
      kDuplicateCANId
    
      kInvalidCANId
    
      kSparkMaxDataPortAlreadyConfiguredDifferently
    
      kSparkFlexBrushedWithoutDock
    
      kInvalidBrushlessEncoderConfiguration
    
      kFeedbackSensorIncompatibleWithDataPortConfig
    
      kParamInvalidChannel
    
      kParamInvalidValue
    
      kCannotPersistParametersWhileEnabled
    """
    __members__: typing.ClassVar[dict[str, REVLibError]]  # value = {'kOk': <REVLibError.kOk: 0>, 'kError': <REVLibError.kError: 1>, 'kTimeout': <REVLibError.kTimeout: 2>, 'kNotImplemented': <REVLibError.kNotImplemented: 3>, 'kHALError': <REVLibError.kHALError: 4>, 'kCantFindFirmware': <REVLibError.kCantFindFirmware: 5>, 'kFirmwareTooOld': <REVLibError.kFirmwareTooOld: 6>, 'kFirmwareTooNew': <REVLibError.kFirmwareTooNew: 7>, 'kParamInvalidID': <REVLibError.kParamInvalidID: 8>, 'kParamMismatchType': <REVLibError.kParamMismatchType: 9>, 'kParamAccessMode': <REVLibError.kParamAccessMode: 10>, 'kParamInvalid': <REVLibError.kParamInvalid: 11>, 'kParamNotImplementedDeprecated': <REVLibError.kParamNotImplementedDeprecated: 12>, 'kFollowConfigMismatch': <REVLibError.kFollowConfigMismatch: 13>, 'kInvalid': <REVLibError.kInvalid: 14>, 'kSetpointOutOfRange': <REVLibError.kSetpointOutOfRange: 15>, 'kUnknown': <REVLibError.kUnknown: 16>, 'kCANDisconnected': <REVLibError.kCANDisconnected: 17>, 'kDuplicateCANId': <REVLibError.kDuplicateCANId: 18>, 'kInvalidCANId': <REVLibError.kInvalidCANId: 19>, 'kSparkMaxDataPortAlreadyConfiguredDifferently': <REVLibError.kSparkMaxDataPortAlreadyConfiguredDifferently: 20>, 'kSparkFlexBrushedWithoutDock': <REVLibError.kSparkFlexBrushedWithoutDock: 21>, 'kInvalidBrushlessEncoderConfiguration': <REVLibError.kInvalidBrushlessEncoderConfiguration: 22>, 'kFeedbackSensorIncompatibleWithDataPortConfig': <REVLibError.kFeedbackSensorIncompatibleWithDataPortConfig: 23>, 'kParamInvalidChannel': <REVLibError.kParamInvalidChannel: 24>, 'kParamInvalidValue': <REVLibError.kParamInvalidValue: 25>, 'kCannotPersistParametersWhileEnabled': <REVLibError.kCannotPersistParametersWhileEnabled: 26>}
    kCANDisconnected: typing.ClassVar[REVLibError]  # value = <REVLibError.kCANDisconnected: 17>
    kCannotPersistParametersWhileEnabled: typing.ClassVar[REVLibError]  # value = <REVLibError.kCannotPersistParametersWhileEnabled: 26>
    kCantFindFirmware: typing.ClassVar[REVLibError]  # value = <REVLibError.kCantFindFirmware: 5>
    kDuplicateCANId: typing.ClassVar[REVLibError]  # value = <REVLibError.kDuplicateCANId: 18>
    kError: typing.ClassVar[REVLibError]  # value = <REVLibError.kError: 1>
    kFeedbackSensorIncompatibleWithDataPortConfig: typing.ClassVar[REVLibError]  # value = <REVLibError.kFeedbackSensorIncompatibleWithDataPortConfig: 23>
    kFirmwareTooNew: typing.ClassVar[REVLibError]  # value = <REVLibError.kFirmwareTooNew: 7>
    kFirmwareTooOld: typing.ClassVar[REVLibError]  # value = <REVLibError.kFirmwareTooOld: 6>
    kFollowConfigMismatch: typing.ClassVar[REVLibError]  # value = <REVLibError.kFollowConfigMismatch: 13>
    kHALError: typing.ClassVar[REVLibError]  # value = <REVLibError.kHALError: 4>
    kInvalid: typing.ClassVar[REVLibError]  # value = <REVLibError.kInvalid: 14>
    kInvalidBrushlessEncoderConfiguration: typing.ClassVar[REVLibError]  # value = <REVLibError.kInvalidBrushlessEncoderConfiguration: 22>
    kInvalidCANId: typing.ClassVar[REVLibError]  # value = <REVLibError.kInvalidCANId: 19>
    kNotImplemented: typing.ClassVar[REVLibError]  # value = <REVLibError.kNotImplemented: 3>
    kOk: typing.ClassVar[REVLibError]  # value = <REVLibError.kOk: 0>
    kParamAccessMode: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamAccessMode: 10>
    kParamInvalid: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamInvalid: 11>
    kParamInvalidChannel: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamInvalidChannel: 24>
    kParamInvalidID: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamInvalidID: 8>
    kParamInvalidValue: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamInvalidValue: 25>
    kParamMismatchType: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamMismatchType: 9>
    kParamNotImplementedDeprecated: typing.ClassVar[REVLibError]  # value = <REVLibError.kParamNotImplementedDeprecated: 12>
    kSetpointOutOfRange: typing.ClassVar[REVLibError]  # value = <REVLibError.kSetpointOutOfRange: 15>
    kSparkFlexBrushedWithoutDock: typing.ClassVar[REVLibError]  # value = <REVLibError.kSparkFlexBrushedWithoutDock: 21>
    kSparkMaxDataPortAlreadyConfiguredDifferently: typing.ClassVar[REVLibError]  # value = <REVLibError.kSparkMaxDataPortAlreadyConfiguredDifferently: 20>
    kTimeout: typing.ClassVar[REVLibError]  # value = <REVLibError.kTimeout: 2>
    kUnknown: typing.ClassVar[REVLibError]  # value = <REVLibError.kUnknown: 16>
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
class RelativeEncoder:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().
        
        :returns: Number the RPM of the motor
        """
    def setPosition(self, position: float) -> REVLibError:
        """
        Set the position of the encoder.
        
        :param position: Number of rotations of the motor
        
        :returns: REVLibError::kOk if successful
        """
class SignalsConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def IAccumulationAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkClosedLoopController::GetIAccum().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def IAccumulationPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkClosedLoopController::GetIAccum(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def __init__(self) -> None:
        ...
    def absoluteEncoderPositionAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkAbsoluteEncoder::GetPosition().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def absoluteEncoderPositionPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkAbsoluteEncoder::GetPosition(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def absoluteEncoderVelocityAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkAbsoluteEncoder::GetVelocity().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def absoluteEncoderVelocityPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkAbsoluteEncoder::GetVelocity(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogPositionAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkAnalogSensor::GetPosition().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogPositionPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkAnalogSensor::GetPosition(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogVelocityAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkAnalogSensor::GetVelocity().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogVelocityPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkAnalogSensor::GetVelocity(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogVoltageAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkAnalogSensor::GetVoltage().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def analogVoltagePeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkAnalogSensor::GetVoltage(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def appliedOutputAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::GetAppliedOutput().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :deprecated: Calling this method will have no effect, as status 0 cannot
                     be disabled.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def appliedOutputPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::GetAppliedOutput(). The default period is 10ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        **NOTE:** Applied output is used by other SPARK devices in follower
        mode. Setting too long of a period should be avoided if this SPARK device
        is the leader, as it can degrade follower mode performance.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def apply(self, config: SignalsConfig) -> SignalsConfig:
        """
        Applies settings from another SignalsConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SignalsConfig to copy settings from
        
        :returns: The updated SignalsConfig for method chaining
        """
    def busVoltageAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::getBusVoltage().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :deprecated: Calling this method will have no effect, as status 0 cannot
                     be disabled.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def busVoltagePeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::getBusVoltage(). The default period is 10ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        **NOTE:** This signal shares a status frame with applied output
        which is used by other SPARK devices in follower mode. Setting too long
        of a period should be avoided if this SPARK device is the leader, as it
        can degrade follower mode performance.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def externalOrAltEncoderPosition(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkFlexExternalEncoder::GetPosition() or
        SparkMaxAlternateEncoder::GetPosition(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def externalOrAltEncoderPositionAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkFlexExternalEncoder::GetPosition() or
        SparkMaxAlternateEncoder::GetPosition().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def externalOrAltEncoderVelocity(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkFlexExternalEncoder::GetVelocity() or
        SparkMaxAlternateEncoder::GetVelocity(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def externalOrAltEncoderVelocityAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkFlexExternalEncoder::GetVelocity() or
        SparkMaxAlternateEncoder::GetVelocity().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def faultsAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::GetFaults() and
        SparkBase::GetStickyFaults().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def faultsPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::GetFaults() and SparkBase::GetStickyFaults().
        The default period is 250ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def limitsAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkLimitSwitch::IsPressed().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :deprecated: Calling this method will have no effect, as status 0 cannot
                     be disabled.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def limitsPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkLimitSwitch::IsPressed(). The default period is 10ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        **NOTE:** This signal shares a status frame with applied output
        which is used by other SPARK devices in follower mode. Setting too long
        of a period should be avoided if this SPARK device is the leader, as it
        can degrade follower mode performance.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def motorTemperatureAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::GetMotorTemperature().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :deprecated: Calling this method will have no effect, as status 0 cannot
                     be disabled.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def motorTemperaturePeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::GetMotorTemperature(). The default period is 10ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        **NOTE:** This signal shares a status frame with applied output
        which is used by other SPARK devices in follower mode. Setting too long
        of a period should be avoided if this SPARK device is the leader, as it
        can degrade follower mode performance.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def outputCurrentAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::GetOutputCurrent().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :deprecated: Calling this method will have no effect, as status 0 cannot
                     be disabled.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def outputCurrentPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::GetOutputCurrent(). The default period is 10ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        **NOTE:** This signal shares a status frame with applied output
        which is used by other SPARK devices in follower mode. Setting too long
        of a period should be avoided if this SPARK device is the leader, as it
        can degrade follower mode performance.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def primaryEncoderPositionAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkRelativeEncoder::GetPosition().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def primaryEncoderPositionPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkRelativeEncoder::GetPosition(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def primaryEncoderVelocityAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkRelativeEncoder::GetVelocity().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def primaryEncoderVelocityPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkRelativeEncoder::GetVelocity(). The default period is 20ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def warningsAlwaysOn(self, enabled: bool) -> SignalsConfig:
        """
        Set whether to always enable the status frame that provides the signal
        returned by SparkBase::GetWarnings() and
        SparkBase::GetStickyWarnings().
        
        Status frames are only enabled when a signal is requested via its
        respective getter method, and there may be a small period of time where
        the signal's data is unavailable due to waiting for the SPARK to receive
        the command to enable the status frame. Use this method to enable the
        status frame at all times.
        
        If multiple alwaysOn values are set for signals within the same status
        frame, the result from OR'ing the values will be used.
        
        :param enabled: True to always enable the status frame
        
        :returns: The modified SignalsConfig object for method chaining
        """
    def warningsPeriodMs(self, periodMs: int) -> SignalsConfig:
        """
        Set the period (ms) of the status frame that provides the signal returned
        by SparkBase::GetWarnings() and SparkBase::GetStickyWarnings().
        The default period is 250ms.
        
        If multiple periods are set for signals within the same status frame,
        the minimum given value will be used.
        
        :param periodMs: The period in milliseconds
        
        :returns: The modified SignalsConfig object for method chaining
        """
class SignalsConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getAbsoluteEncoderPositionAlwaysOn(self) -> bool:
        ...
    def getAbsoluteEncoderPositionPeriodMs(self) -> int:
        ...
    def getAbsoluteEncoderVelocityAlwaysOn(self) -> bool:
        ...
    def getAbsoluteEncoderVelocityPeriodMs(self) -> int:
        ...
    def getAnalogPositionAlwaysOn(self) -> bool:
        ...
    def getAnalogPositionPeriodMs(self) -> int:
        ...
    def getAnalogVelocityAlwaysOn(self) -> bool:
        ...
    def getAnalogVelocityPeriodMs(self) -> int:
        ...
    def getAnalogVoltageAlwaysOn(self) -> bool:
        ...
    def getAnalogVoltagePeriodMs(self) -> int:
        ...
    def getAppliedOutputAlwaysOn(self) -> bool:
        ...
    def getAppliedOutputPeriodMs(self) -> int:
        ...
    def getBusVoltageAlwaysOn(self) -> bool:
        ...
    def getBusVoltagePeriodMs(self) -> int:
        ...
    def getExternalOrAltEncoderPositionAlwaysOn(self) -> bool:
        ...
    def getExternalOrAltEncoderPositionPeriodMs(self) -> int:
        ...
    def getExternalOrAltEncoderVelocityAlwaysOn(self) -> bool:
        ...
    def getExternalOrAltEncoderVelocityPeriodMs(self) -> int:
        ...
    def getFaultsAlwaysOn(self) -> bool:
        ...
    def getFaultsPeriodMs(self) -> int:
        ...
    def getIAccumulationAlwaysOn(self) -> bool:
        ...
    def getIAccumulationPeriodMs(self) -> int:
        ...
    def getLimitsAlwaysOn(self) -> bool:
        ...
    def getLimitsPeriodMs(self) -> int:
        ...
    def getMotorTemperatureAlwaysOn(self) -> bool:
        ...
    def getMotorTemperaturePeriodMs(self) -> int:
        ...
    def getOutputCurrentAlwaysOn(self) -> bool:
        ...
    def getOutputCurrentPeriodMs(self) -> int:
        ...
    def getPrimaryEncoderPositionAlwaysOn(self) -> bool:
        ...
    def getPrimaryEncoderPositionPeriodMs(self) -> int:
        ...
    def getPrimaryEncoderVelocityAlwaysOn(self) -> bool:
        ...
    def getPrimaryEncoderVelocityPeriodMs(self) -> int:
        ...
    def getWarningsAlwaysOn(self) -> bool:
        ...
    def getWarningsPeriodMs(self) -> int:
        ...
class SmartMotionConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def allowedClosedLoopError(self, allowedError: float, slot: ClosedLoopSlot = ...) -> SmartMotionConfig:
        """
        Set the allowed closed loop error for the Smart Motion mode of the
        controller for a specific closed loop slot. This value is how much
        deviation from the setpoint is tolerated and is useful in preventing
        oscillation around the setpoint. Natively, the units are in rotations but
        will be affected by the position conversion factor.
        
        :deprecated: It is recommended to migrate to MAXMotion instead.
        
        :param allowedError: The allowed error with the position conversion factor
                             applied
        :param slot:         The closed loop slot to set the values for
        
        :returns: The modified SmartMotionConfig object for method chaining
        """
    def apply(self, config: SmartMotionConfig) -> SmartMotionConfig:
        """
        Applies settings from another SmartMotionConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SmartMotionConfig to copy settings from
        
        :returns: The updated SmartMotionConfig for method chaining
        """
    def maxAcceleration(self, maxAcceleration: float, slot: ClosedLoopSlot = ...) -> SmartMotionConfig:
        """
        Set the maximum acceleration for the Smart Motion mode of the controller
        for a specific PID slot. This is the rate at which the velocity will
        increase until the max velocity is reached. Natively, the units are in
        RPM per second but will be affected by the velocity conversion factor.
        
        :deprecated: It is recommended to migrate to MAXMotion instead.
        
        :param maxAcceleration: The maximum acceleration with the velocity
                                conversion factor applied
        :param slot:            The closed loop slot to set the values for
        
        :returns: The modified SmartMotionConfig object for method chaining
        """
    def maxVelocity(self, maxVelocity: float, slot: ClosedLoopSlot = ...) -> SmartMotionConfig:
        """
        Set the maximum velocity for the Smart Motion mode of the controller.
        This is the cruising velocity of the profile. Natively, the units are in
        RPM but will be affected by the velocity conversion factor.
        
        This will set the value for closed loop slot 0. To set the value for a
        specific closed loop slot, use SmartMotionConfig::MaxVelocity(double,
        ClosedLoopSlot).
        
        :deprecated: It is recommended to migrate to MAXMotion instead.
        
        :param maxVelocity: The maximum velocity with the velocity conversion
                            factor applied
        :param slot:        The closed loop slot to set the values for
        
        :returns: The modified SmartMotionConfig object for method chaining
        """
    def minOutputVelocity(self, minVelocity: float, slot: ClosedLoopSlot = ...) -> SmartMotionConfig:
        """
        Set the minimum velocity for the Smart Motion mode of the controller for
        a specific closed loop slot. Any requested velocities below this value
        will be set to 0. Natively, the units are in RPM but will be affected by
        the velocity conversion factor.
        
        :deprecated: It is recommended to migrate to MAXMotion instead.
        
        :param minVelocity: The minimum velocity with the velocity conversion
                            factor applied
        :param slot:        The closed loop slot to set the values for
        
        :returns: The modified SmartMotionConfig object for method chaining
        """
class SmartMotionConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getAllowedClosedLoopError(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxAcceleration(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMaxVelocity(self, slot: ClosedLoopSlot = ...) -> float:
        ...
    def getMinOutputVelocity(self, slot: ClosedLoopSlot = ...) -> float:
        ...
class SoftLimitConfig(BaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def apply(self, config: SoftLimitConfig) -> SoftLimitConfig:
        """
        Applies settings from another SoftLimitConfig to this one.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SoftLimitConfig to copy settings from
        
        :returns: The updated SoftLimitConfig for method chaining
        """
    def forwardSoftLimit(self, limit: float) -> SoftLimitConfig:
        """
        Set the forward soft limit based on the position of the selected feedback
        sensor. This will disable motor actuation in the forward direction past
        this position. This value should have the position conversion factor
        applied to it.
        
        :param limit: The forward soft limit position with the conversion factor
                      applied
        
        :returns: The modified SoftLimitConfig object for method chaining
        """
    def forwardSoftLimitEnabled(self, enabled: bool) -> SoftLimitConfig:
        """
        Set whether to enable or disable the forward soft limit.
        
        :param enabled: True to enable the forward soft limit
        
        :returns: The modified SoftLimitConfig object for method chaining
        """
    def reverseSoftLimit(self, limit: float) -> SoftLimitConfig:
        """
        Set the reverse soft limit based on the position of the selected feedback
        sensor. This will disable motor actuation in the reverse direction past
        this position. This value should have the position conversion factor
        applied to it.
        
        :param limit: The reverse soft limit position with the conversion factor
                      applied
        
        :returns: The modified SoftLimitConfig object for method chaining
        """
    def reverseSoftLimitEnabled(self, enabled: bool) -> SoftLimitConfig:
        """
        Set whether to enable or disable the reverse soft limit.
        
        :param enabled: True to enable the reverse soft limit
        
        :returns: The modified SoftLimitConfig object for method chaining
        """
class SoftLimitConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getForwardSoftLimit(self) -> float:
        ...
    def getForwardSoftLimitEnabled(self) -> bool:
        ...
    def getReverseSoftLimit(self) -> float:
        ...
    def getReverseSoftLimitEnabled(self) -> bool:
        ...
class SparkAbsoluteEncoder(AbsoluteEncoder):
    """
    Get an instance of this class by using SparkBase::GetEncoder() or
    SparkBase::GetEncoder(SparkMaxRelativeEncoder::Type, int).
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'rotations per second' by default, and can be changed by a scale
        factor using setVelocityConversionFactor().
        
        :returns: Number of rotations per second of the motor
        """
class SparkAbsoluteEncoderSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, motor: SparkMax) -> None:
        ...
    @typing.overload
    def __init__(self, motor: SparkFlex) -> None:
        ...
    def getInverted(self) -> bool:
        ...
    def getPosition(self) -> float:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getZeroOffset(self) -> float:
        ...
    def iterate(self, velocity: float, dt: float) -> None:
        ...
    def setInverted(self, inverted: bool) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setPositionConversionFactor(self, positionConversionFactor: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def setVelocityConversionFactor(self, velocityConversionFactor: float) -> None:
        ...
    def setZeroOffset(self, zeroOffset: float) -> None:
        ...
class SparkAnalogSensor(AnalogInput):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the sensor. Returns value in the native unit
        of 'volt' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Position of the sensor in volts
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the sensor. Returns value in the native units of
        'volts per second' by default, and can be changed by a
        scale factor using setVelocityConversionFactor().
        
        :returns: Velocity of the sensor in volts per second
        """
    def getVoltage(self) -> float:
        """
        Get the voltage of the analog sensor.
        
        :returns: Voltage of the sensor
        """
class SparkAnalogSensorSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, motor: SparkMax) -> None:
        ...
    @typing.overload
    def __init__(self, motor: SparkFlex) -> None:
        ...
    def getInverted(self) -> bool:
        ...
    def getPosition(self) -> float:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getVoltage(self) -> float:
        ...
    def iterate(self, velocity: float, dt: float) -> None:
        ...
    def setInverted(self, inverted: bool) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setPositionConversionFactor(self, positionConversionFactor: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def setVelocityConversionFactor(self, velocityConversionFactor: float) -> None:
        ...
    def setVoltage(self, voltage: float) -> None:
        ...
class SparkBase(SparkLowLevel):
    class Faults:
        can: bool
        escEeprom: bool
        firmware: bool
        gateDriver: bool
        motorType: bool
        other: bool
        rawBits: int
        sensor: bool
        temperature: bool
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @typing.overload
        def __init__(self) -> None:
            ...
        @typing.overload
        def __init__(self, faults: int) -> None:
            ...
    class IdleMode:
        """
        Members:
        
          kCoast
        
          kBrake
        """
        __members__: typing.ClassVar[dict[str, SparkBase.IdleMode]]  # value = {'kCoast': <IdleMode.kCoast: 0>, 'kBrake': <IdleMode.kBrake: 1>}
        kBrake: typing.ClassVar[SparkBase.IdleMode]  # value = <IdleMode.kBrake: 1>
        kCoast: typing.ClassVar[SparkBase.IdleMode]  # value = <IdleMode.kCoast: 0>
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
    class PersistMode:
        """
        Members:
        
          kNoPersistParameters
        
          kPersistParameters
        """
        __members__: typing.ClassVar[dict[str, SparkBase.PersistMode]]  # value = {'kNoPersistParameters': <PersistMode.kNoPersistParameters: 0>, 'kPersistParameters': <PersistMode.kPersistParameters: 1>}
        kNoPersistParameters: typing.ClassVar[SparkBase.PersistMode]  # value = <PersistMode.kNoPersistParameters: 0>
        kPersistParameters: typing.ClassVar[SparkBase.PersistMode]  # value = <PersistMode.kPersistParameters: 1>
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
    class ResetMode:
        """
        Members:
        
          kNoResetSafeParameters
        
          kResetSafeParameters
        """
        __members__: typing.ClassVar[dict[str, SparkBase.ResetMode]]  # value = {'kNoResetSafeParameters': <ResetMode.kNoResetSafeParameters: 0>, 'kResetSafeParameters': <ResetMode.kResetSafeParameters: 1>}
        kNoResetSafeParameters: typing.ClassVar[SparkBase.ResetMode]  # value = <ResetMode.kNoResetSafeParameters: 0>
        kResetSafeParameters: typing.ClassVar[SparkBase.ResetMode]  # value = <ResetMode.kResetSafeParameters: 1>
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
    class SoftLimitDirection:
        """
        Members:
        
          kForward
        
          kReverse
        """
        __members__: typing.ClassVar[dict[str, SparkBase.SoftLimitDirection]]  # value = {'kForward': <SoftLimitDirection.kForward: 0>, 'kReverse': <SoftLimitDirection.kReverse: 1>}
        kForward: typing.ClassVar[SparkBase.SoftLimitDirection]  # value = <SoftLimitDirection.kForward: 0>
        kReverse: typing.ClassVar[SparkBase.SoftLimitDirection]  # value = <SoftLimitDirection.kReverse: 1>
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
    class Warnings:
        brownout: bool
        escEeprom: bool
        extEeprom: bool
        hasReset: bool
        other: bool
        overcurrent: bool
        rawBits: int
        sensor: bool
        stall: bool
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @typing.overload
        def __init__(self) -> None:
            ...
        @typing.overload
        def __init__(self, warnings: int) -> None:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, deviceID: int, type: SparkLowLevel.MotorType, model: SparkLowLevel.SparkModel) -> None:
        """
        Create a new object to control a SPARK motor Controller
        
        :param deviceID: The device ID.
        :param type:     The motor type connected to the controller. Brushless
                         motor wires must be connected to their matching
                         colors, and the hall sensor must be plugged in. Brushed motors must
                         be connected to the Red and Black terminals only.
        """
    def _getEncoderEvenIfAlreadyCreated(self) -> SparkRelativeEncoder:
        ...
    def _getMotorInterface(self) -> int:
        """
        Get the current motor interface for the SPARK.
        
        :returns:
        """
    def _getSparkModel(self) -> SparkLowLevel.SparkModel:
        """
        Get the Model of this SPARK Device. Useful for determining if this
        is a Flex, MAX, or other device
        
        :returns: the model of this device
        """
    def clearFaults(self) -> REVLibError:
        """
        Clears all non-sticky faults.
        
        Sticky faults must be cleared by resetting the motor controller.
        """
    def configure(self, config: SparkBaseConfig, resetMode: SparkBase.ResetMode, persistMode: SparkBase.PersistMode) -> REVLibError:
        """
        Set the configuration for the SPARK.
        
        If @c resetMode is ResetMode::kResetSafeParameters, this
        method will reset safe writable parameters to their default values before
        setting the given configuration. The following parameters will not be
        reset by this action: CAN ID, Motor Type, Idle Mode, PWM Input Deadband,
        and Duty Cycle Offset.
        
        If @c persistMode is PersistMode::kPersistParameters, this
        method will save all parameters to the SPARK's non-volatile memory after
        setting the given configuration. This will allow parameters to persist
        across power cycles.
        
        :param config:      The desired SPARK configuration
        :param resetMode:   Whether to reset safe parameters before setting the
                            configuration
        :param persistMode: Whether to persist the parameters after setting the
                            configuration
        
        :returns: REVLibError::kOk if successful
        """
    def configureAsync(self, config: SparkBaseConfig, resetMode: SparkBase.ResetMode, persistMode: SparkBase.PersistMode) -> REVLibError:
        """
        Set the configuration for the SPARK without waiting for a response.
        
        If @c resetMode is ResetMode::kResetSafeParameters, this
        method will reset safe writable parameters to their default values before
        setting the given configuration. The following parameters will not be
        reset by this action: CAN ID, Motor Type, Idle Mode, PWM Input Deadband,
        and Duty Cycle Offset.
        
        If @c persistMode is PersistMode::kPersistParameters, this
        method will save all parameters to the SPARK's non-volatile memory after
        setting the given configuration. This will allow parameters to persist
        across power cycles.
        
        NOTE: This method will immediately return REVLibError::kOk and the
        action will be done in the background. Any errors that occur will be
        reported to the driver station.
        
        :param config:      The desired SPARK configuration
        :param resetMode:   Whether to reset safe parameters before setting the
                            configuration
        :param persistMode: Whether to persist the parameters after setting the
                            configuration
        
        :returns: REVLibError::kOk
                  @see Configure()
        """
    def disable(self) -> None:
        """
        Common interface for disabling a motor.
        """
    def get(self) -> float:
        """
        Common interface for getting the current set speed of a speed controller.
        
        :returns: The current set speed.  Value is between -1.0 and 1.0.
        """
    def getAbsoluteEncoder(self) -> SparkAbsoluteEncoder:
        """
        Returns an object for interfacing with a connected absolute encoder.
        
        The default encoder type is assumed to be a duty cycle sensor.
        """
    def getAnalog(self) -> SparkAnalogSensor:
        """
        Returns an object for interfacing with a connected analog sensor.
        By default, the mode is set to kAbsolute, thus treating the
        sensor as an absolute sensor.
        """
    def getAppliedOutput(self) -> float:
        """
        Simulation note: this value will not be updated during simulation
        unless
        {@link SparkSim#iterate} is called
        
        Returns motor controller's output duty cycle.
        """
    def getBusVoltage(self) -> float:
        """
        Returns the voltage fed into the motor controller.
        """
    def getClosedLoopController(self) -> SparkClosedLoopController:
        """
        Returns an object for interfacing with the integrated Closed Loop
        Controller.
        """
    def getEncoder(self) -> SparkRelativeEncoder:
        """
        Returns an object for interfacing with the encoder connected to the
        encoder pins or front port of the SPARK MAX or the motor interface of the
        SPARK Flex.
        """
    def getFaults(self) -> SparkBase.Faults:
        """
        Get the active faults that are currently present on the SPARK. Faults
        are fatal errors that prevent the motor from running.
        
        :returns: A struct with each fault and their active value
        """
    def getForwardLimitSwitch(self) -> SparkLimitSwitch:
        """
        Returns an object for interfacing with the forward limit switch connected
        to the appropriate pins on the data port.
        
        This call will disable support for the alternate encoder.
        """
    def getInverted(self) -> bool:
        """
        Common interface for returning the inversion state of a speed controller.
        
        This call has no effect if the controller is a follower.
        
        :deprecated: Use SparkBaseConfigAccessor.GetInverted() via
                     SparkMax.configAccessor or SparkFlex.configAccessor instead
        
        :returns: isInverted The state of inversion, true is inverted.
        """
    def getLastError(self) -> REVLibError:
        """
        All device errors are tracked on a per thread basis for all
        devices in that thread. This is meant to be called
        immediately following another call that has the possibility
        of throwing an error to validate if an  error has occurred.
        
        :returns: the last error that was generated.
        """
    def getMotorTemperature(self) -> float:
        """
        Returns the motor temperature in Celsius.
        """
    def getOutputCurrent(self) -> float:
        """
        Returns motor controller's output current in Amps.
        """
    def getReverseLimitSwitch(self) -> SparkLimitSwitch:
        """
        Returns an object for interfacing with the reverse limit switch connected
        to the appropriate pins on the data port.
        
        This call will disable support for the alternate encoder.
        """
    def getStickyFaults(self) -> SparkBase.Faults:
        """
        Get the sticky faults that were present on the SPARK at one point
        since the sticky faults were last cleared. Faults are fatal errors
        that prevent the motor from running.
        
        Sticky faults can be cleared with SparkBase::ClearFaults().
        
        :returns: A struct with each fault and their sticky value
        """
    def getStickyWarnings(self) -> SparkBase.Warnings:
        """
        Get the sticky warnings that were present on the SPARK at one point
        since the sticky warnings were last cleared. Warnings are non-fatal
        errors.
        
        Sticky warnings can be cleared with SparkBase::clearFaults().
        
        :returns: A struct with each warning and their sticky value
        """
    def getWarnings(self) -> SparkBase.Warnings:
        """
        Get the active warnings that are currently present on the SPARK.
        Warnings are non-fatal errors.
        
        :returns: A struct with each warning and their active value
        """
    def hasActiveFault(self) -> bool:
        ...
    def hasActiveWarning(self) -> bool:
        """
        Get whether the SPARK has one or more active warnings.
        
        :returns: true if there is an active warning
                  @see GetWarnings()
        """
    def hasStickyFault(self) -> bool:
        """
        Get whether the SPARK has one or more sticky faults.
        
        :returns: true if there is a sticky fault
                  @see GetStickyFaults()
        """
    def hasStickyWarning(self) -> bool:
        """
        Get whether the SPARK has one or more sticky warnings.
        
        :returns: true if there is a sticky warning
                  @see GetStickyWarnings()
        """
    def isFollower(self) -> bool:
        """
        Returns whether the controller is following another controller
        
        :returns: True if this device is following another controller false
                  otherwise
        """
    def pauseFollowerMode(self) -> REVLibError:
        """
        Pause follower mode.
        
        NOTE: If the SPARK experiences a power cycle and has follower mode
        configured, follower mode will automatically restart.
        
        :returns: REVLibError::kOk if successful
        """
    def pauseFollowerModeAsync(self) -> REVLibError:
        """
        Pause follower mode without waiting for a response.
        
        NOTE: If the SPARK experiences a power cycle and has follower mode
        configured, follower mode will automatically restart.
        
        NOTE: This method will immediately return REVLibError::kOk and the
        action will be done in the background. Any errors that occur will be
        reported to the driver station.
        
        :returns: REVLibError::kOk
                  @see PauseFollowerMode()
        """
    def resumeFollowerMode(self) -> REVLibError:
        """
        Resume follower mode if the SPARK has a valid follower mode config.
        
        NOTE: Follower mode will start automatically upon configuring follower
        mode. If the SPARK experiences a power cycle and has follower mode
        configured, follower mode will automatically restart. This method is only
        useful after PauseFollowerMode() has been called.
        
        :returns: REVLibError::kOk if successful
        """
    def resumeFollowerModeAsync(self) -> REVLibError:
        """
        Resume follower mode if the SPARK has a valid follower
        mode config without waiting for a response.
        
        NOTE: Follower mode will start automatically upon configuring follower
        mode. If the SPARK experiences a power cycle and has follower mode
        configured, follower mode will automatically restart. This method is only
        useful after PauseFollowerMode() has been called.
        
        NOTE: This method will immediately return REVLibError::kOk and the
        action will be done in the background. Any errors that occur will be
        reported to the driver station.
        
        :returns: REVLibError::kOk
                  @see ResumeFollowerMode()
        """
    def set(self, speed: float) -> None:
        """
        Common interface for setting the speed of a speed controller.
        
        :param speed: The speed to set.  Value should be between -1.0 and 1.0.
        """
    def setCANTimeout(self, milliseconds: int) -> REVLibError:
        """
        Sets the timeout duration for waiting for CAN responses from the device.
        
        :param milliseconds: The timeout in milliseconds.
        """
    def setInverted(self, isInverted: bool) -> None:
        """
        Common interface for inverting direction of a speed controller.
        
        This call has no effect if the controller is a follower. To invert
        a follower, see the follow() method.
        
        :deprecated: Use SparkBaseConfig.Inverted() with Configure() instead
        
        :param isInverted: The state of inversion, true is inverted.
        """
    def setVoltage(self, output: wpimath.units.volts) -> None:
        """
        Sets the voltage output of the SpeedController.  This is equivalent to
        a call to SetReference(output, SparkBase::ControlType::kVoltage). The
        behavior of this call differs slightly from the WPILib documentation for
        this call since the device internally sets the desired voltage (not a
        compensation value). That means that this *can* be a 'set-and-forget'
        call.
        
        :param output: The voltage to output.
        """
    def stopMotor(self) -> None:
        """
        Common interface to stop the motor until Set is called again.
        """
class SparkBaseConfig(BaseConfig):
    class IdleMode:
        """
        Members:
        
          kCoast
        
          kBrake
        """
        __members__: typing.ClassVar[dict[str, SparkBaseConfig.IdleMode]]  # value = {'kCoast': <IdleMode.kCoast: 0>, 'kBrake': <IdleMode.kBrake: 1>}
        kBrake: typing.ClassVar[SparkBaseConfig.IdleMode]  # value = <IdleMode.kBrake: 1>
        kCoast: typing.ClassVar[SparkBaseConfig.IdleMode]  # value = <IdleMode.kCoast: 0>
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
    def __init__(self) -> None:
        ...
    @typing.overload
    def apply(self, config: SparkBaseConfig) -> SparkBaseConfig:
        """
        Applies settings from another SparkBaseConfig to this one,
        including all of its nested configurations.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SparkBaseConfig to copy settings from
        
        :returns: The updated SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: AbsoluteEncoderConfig) -> SparkBaseConfig:
        """
        Applies settings from an  AbsoluteEncoderConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  AbsoluteEncoderConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: AnalogSensorConfig) -> SparkBaseConfig:
        """
        Applies settings from an  AnalogSensorConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  AnalogSensorConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: EncoderConfig) -> SparkBaseConfig:
        """
        Applies settings from an  EncoderConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  EncoderConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: LimitSwitchConfig) -> SparkBaseConfig:
        """
        Applies settings from a  LimitSwitchConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  LimitSwitchConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: SoftLimitConfig) -> SparkBaseConfig:
        """
        Applies settings from a  SoftLimitConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  SoftLimitConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: ClosedLoopConfig) -> SparkBaseConfig:
        """
        Applies settings from a  ClosedLoopConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  ClosedLoopConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    @typing.overload
    def apply(self, config: SignalsConfig) -> SparkBaseConfig:
        """
        Applies settings from a  SignalsConfig to this
        SparkBaseConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The  SignalsConfig to copy settings from
        
        :returns: The updated  SparkBaseConfig for method chaining
        """
    def closedLoopRampRate(self, rate: float) -> SparkBaseConfig:
        """
        Sets the ramp rate for closed loop control modes.
        
        This is the maximum rate at which the motor controller's output is
        allowed to change.
        
        :param rate: Time in seconds to go from 0 to full throttle.
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def disableFollowerMode(self) -> SparkBaseConfig:
        """
        Disables follower mode on the controller.
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def disableVoltageCompensation(self) -> SparkBaseConfig:
        """
        Disables the voltage compensation setting for all modes on the SPARK.
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def flatten(self) -> str:
        ...
    @typing.overload
    def follow(self, leaderCanId: int, invert: bool = False) -> SparkBaseConfig:
        """
        Causes this controller's output to mirror the provided leader.
        
        Only voltage output is mirrored. Settings changed on the leader do not
        affect the follower.
        
        Following anything other than a CAN-enabled SPARK is not officially
        supported.
        
        :param leaderCanId: The CAN ID of the device to follow.
        :param invert:      Set the follower to output opposite of the leader
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    @typing.overload
    def follow(self, leader: SparkBase, invert: bool = False) -> SparkBaseConfig:
        """
        Causes this controller's output to mirror the provided leader.
        
        Only voltage output is mirrored. Settings changed on the leader do not
        affect the follower.
        
        Following anything other than a CAN-enabled SPARK is not officially
        supported.
        
        :param leader: The motor controller to follow.
        :param invert: Set the follower to output opposite of the leader
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def inverted(self, inverted: bool) -> SparkBaseConfig:
        """
        Common interface for inverting direction of a speed controller.
        
        This call has no effect if the controller is a follower. To invert a
        follower, see the follow() method.
        
        :param inverted: True for inverted
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def openLoopRampRate(self, rate: float) -> SparkBaseConfig:
        """
        Sets the ramp rate for open loop control modes.
        
        This is the maximum rate at which the motor controller's output is
        allowed to change.
        
        :param rate: Time in seconds to go from 0 to full throttle.
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def secondaryCurrentLimit(self, limit: float, chopCycles: int = 0) -> SparkBaseConfig:
        """
        Sets the secondary current limit in Amps.
        
        The motor controller will disable the output of the controller briefly
        if the current limit is exceeded to reduce the current. This limit is a
        simplified 'on/off' controller. This limit is enabled by default but is
        set higher than the default Smart Current Limit.
        
        The time the controller is off after the current limit is reached is
        determined by the parameter limitCycles, which is the number of PWM
        cycles (20kHz). The recommended value is the default of 0 which is the
        minimum time and is part of a PWM cycle from when the over current is
        detected. This allows the controller to regulate the current close to the
        limit value.
        
        The total time is set by the equation <code>
        t = (50us - t0) + 50us * limitCycles
        t = total off time after over current
        t0 = time from the start of the PWM cycle until over current is detected
        </code>
        
        :param limit:      The current limit in Amps.
        :param chopCycles: The number of additional PWM cycles to turn the driver
                           off after overcurrent is detected.
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def setIdleMode(self, idleMode: SparkBaseConfig.IdleMode) -> SparkBaseConfig:
        """
        Sets the idle mode setting for the SPARK.
        
        :param idleMode: kCoast or kBrake
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def smartCurrentLimit(self, stallLimit: int, freeLimit: int = 0, limitRpm: int = 20000) -> SparkBaseConfig:
        """
        Sets the current limit in Amps.
        
        The motor controller will reduce the controller voltage output to
        avoid surpassing this limit. This limit is enabled by default and used
        for brushless only. This limit is highly recommended when using the NEO
        brushless motor.
        
        The NEO Brushless Motor has a low internal resistance, which can mean
        large current spikes that could be enough to cause damage to the motor
        and controller. This current limit provides a smarter strategy to deal
        with high current draws and keep the motor and controller operating in a
        safe region.
        
        The controller can also limit the current based on the RPM of the
        motor in a linear fashion to help with controllability in closed loop
        control. For a response that is linear the entire RPM range leave limit
        RPM at 0.
        
        :param stallLimit: The current limit in Amps at 0 RPM.
        :param freeLimit:  The current limit at free speed (5700RPM for NEO).
        :param limitRpm:   RPM less than this value will be set to the stallLimit,
                           RPM values greater than limitRpm will scale linearly to freeLimit
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    def voltageCompensation(self, nominalVoltage: float) -> SparkBaseConfig:
        """
        Sets the voltage compensation setting for all modes on the SPARK and
        enables voltage compensation.
        
        :param nominalVoltage: Nominal voltage to compensate output to
        
        :returns: The modified SparkBaseConfig object for method chaining
        """
    @property
    def absoluteEncoder(self) -> AbsoluteEncoderConfig:
        ...
    @property
    def analogSensor(self) -> AnalogSensorConfig:
        ...
    @property
    def closedLoop(self) -> ClosedLoopConfig:
        ...
    @property
    def encoder(self) -> EncoderConfig:
        ...
    @property
    def limitSwitch(self) -> LimitSwitchConfig:
        ...
    @property
    def signals(self) -> SignalsConfig:
        ...
    @property
    def softLimit(self) -> SoftLimitConfig:
        ...
class SparkBaseConfigAccessor:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getClosedLoopRampRate(self) -> float:
        ...
    def getFollowerModeInverted(self) -> bool:
        ...
    def getFollowerModeLeaderId(self) -> int:
        ...
    def getIdleMode(self) -> SparkBaseConfig.IdleMode:
        ...
    def getInverted(self) -> bool:
        ...
    def getOpenLoopRampRate(self) -> float:
        ...
    def getSecondaryCurrentLimit(self) -> float:
        ...
    def getSecondaryCurrentLimitChopCycles(self) -> int:
        ...
    def getSmartCurrentFreeLimit(self) -> int:
        ...
    def getSmartCurrentLimit(self) -> int:
        ...
    def getSmartCurrentRPMLimit(self) -> int:
        ...
    def getVoltageCompensation(self) -> float:
        ...
    def getVoltageCompensationEnabled(self) -> bool:
        ...
    @property
    def absoluteEncoder(self) -> AbsoluteEncoderConfigAccessor:
        """
        Accessor for parameters relating to the absolute encoder. To configure
        these values, use AbsoluteEncoderConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def analogSensor(self) -> AnalogSensorConfigAccessor:
        """
        Accessor for parameters relating to the analog sensor. To configure
        these values, use AnalogSensorConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def closedLoop(self) -> ClosedLoopConfigAccessor:
        """
        Accessor for parameters relating to the closed loop controller. To
        configure these values, use ClosedLoopConfig and call
        SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def encoder(self) -> EncoderConfigAccessor:
        """
        Accessor for parameters relating to the primary encoder. To configure
        these values, use EncoderConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def limitSwitch(self) -> LimitSwitchConfigAccessor:
        """
        Accessor for parameters relating to the hardware limit switches. To
        configure these values, use LimitSwitchConfig and call
        SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def signals(self) -> SignalsConfigAccessor:
        """
        Accessor for parameters relating to status signals. To configure
        these values, use SignalsConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
    @property
    def softLimit(self) -> SoftLimitConfigAccessor:
        """
        Accessor for parameters relating to the software limits. To configure
        these values, use SoftLimitConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
class SparkClosedLoopController:
    class ArbFFUnits:
        """
        Units for arbitrary feed-forward
        
        Members:
        
          kVoltage
        
          kPercentOut
        """
        __members__: typing.ClassVar[dict[str, SparkClosedLoopController.ArbFFUnits]]  # value = {'kVoltage': <ArbFFUnits.kVoltage: 0>, 'kPercentOut': <ArbFFUnits.kPercentOut: 1>}
        kPercentOut: typing.ClassVar[SparkClosedLoopController.ArbFFUnits]  # value = <ArbFFUnits.kPercentOut: 1>
        kVoltage: typing.ClassVar[SparkClosedLoopController.ArbFFUnits]  # value = <ArbFFUnits.kVoltage: 0>
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
    def getIAccum(self) -> float:
        """
        Get the I accumulator of the closed loop controller. This is useful when
        wishing to see what the I accumulator value is to help with PID tuning
        
        :returns: The value of the I accumulator
        """
    def setIAccum(self, iAccum: float) -> REVLibError:
        """
        Set the I accumulator of the closed loop controller. This is useful when
        wishing to force a reset on the I accumulator of the Closed Loop
        Controller. You can also preset values to see how it will respond to
        certain I characteristics
        
        To use this function, the controller must be in a closed loop control
        mode by calling setReference()
        
        :param iAccum: The value to set the I accumulator to
        
        :returns: REVLibError::kOk if successful
        """
    def setReference(self, value: float, ctrl: SparkLowLevel.ControlType, slot: ClosedLoopSlot = ..., arbFeedforward: float = 0, arbFFUnits: SparkClosedLoopController.ArbFFUnits = ...) -> REVLibError:
        """
        Set the controller reference value based on the selected control mode.
        
        :param value:          The value to set depending on the control mode. For basic
                               duty cycle control this should be a value between -1 and 1
                               Otherwise: Voltage Control: Voltage (volts) Velocity Control: Velocity
                               (RPM) Position Control: Position (Rotations) Current Control: Current
                               (Amps). The units can be changed for position and velocity by a scale
                               factor using setPositionConversionFactor().
        :param ctrl:           Is the control type
        :param slot:           The ClosedLoopSlot to use
        :param arbFeedforward: A value from -32.0 to 32.0 which is a voltage
                               applied to the motor after the result of the specified control mode. The
                               units for the parameter is Volts. This value is set after the control
                               mode, but before any current limits or ramp rates.
        :param arbFFUnits:     the units for arbitrary feed-forward
        
        :returns: REVLibError::kOk if successful
        """
class SparkExternalEncoderSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, motor: SparkFlex) -> None:
        ...
    def getInverted(self) -> bool:
        ...
    def getPosition(self) -> float:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getZeroOffset(self) -> float:
        ...
    def iterate(self, velocity: float, dt: float) -> None:
        ...
    def setInverted(self, inverted: bool) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setPositionConversionFactor(self, positionConversionFactor: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def setVelocityConversionFactor(self, velocityConversionFactor: float) -> None:
        ...
    def setZeroOffset(self, zeroOffset: float) -> None:
        ...
class SparkFlex(SparkBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, deviceID: int, type: SparkLowLevel.MotorType) -> None:
        """
        Create a new object to control a SPARK Flex motor Controller
        
        :param deviceID: The device ID.
        :param type:     The motor type connected to the controller. Brushless
                         motor wires must be connected to their matching colors,
                         and the hall sensor must be plugged in. Brushed motors
                         must be connected to the Red and Black terminals only.
        """
    def getExternalEncoder(self) -> SparkFlexExternalEncoder:
        """
        Returns an object for interfacing with an external quadrature encoder
        """
    @property
    def configAccessor(self) -> SparkFlexConfigAccessor:
        """
        Accessor for SPARK parameter values. This object contains fields and
        methods to retrieve parameters that have been applied to the device. To
        set parameters, see SparkBaseConfig and SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and should
        be used infrequently.
        """
class SparkFlexConfig(SparkBaseConfig):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    @typing.overload
    def apply(self, config: SparkFlexConfig) -> SparkFlexConfig:
        """
        Applies settings from another  SparkFlexConfig to this one,
        including all of its nested configurations.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SparkFlexConfig to copy settings from
        
        :returns: The updated SparkFlexConfig for method chaining
        """
    @typing.overload
    def apply(self, config: ExternalEncoderConfig) -> SparkFlexConfig:
        """
        Applies settings from an  ExternalEncoderConfig to this
        SparkFlexConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The ExternalEncoderConfig to copy settings from
        
        :returns: The updated SparkFlexConfig for method chaining
        """
    @typing.overload
    def apply(self, config: SparkBaseConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: AbsoluteEncoderConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: AnalogSensorConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: EncoderConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: LimitSwitchConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: SoftLimitConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: ClosedLoopConfig) -> SparkFlexConfig:
        ...
    @typing.overload
    def apply(self, config: SignalsConfig) -> SparkFlexConfig:
        ...
    def flatten(self) -> str:
        ...
    @property
    def externalEncoder(self) -> ExternalEncoderConfig:
        ...
class SparkFlexConfigAccessor(SparkBaseConfigAccessor):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def externalEncoder(self) -> ExternalEncoderConfigAccessor:
        """
        Accessor for parameters relating to the external encoder. To configure
        these values, use ExternalEncoderConfig and call SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
class SparkFlexExternalEncoder(RelativeEncoder):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().
        
        :returns: Number the RPM of the motor
        """
    def setPosition(self, position: float) -> REVLibError:
        """
        Set the position of the encoder.
        
        :param position: Number of rotations of the motor
        
        :returns: REVLibError::kOk if successful
        """
class SparkFlexSim(SparkSim):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, sparkFlex: SparkFlex, motor: wpimath._controls._controls.plant.DCMotor) -> None:
        ...
    def getExternalEncoderSim(self) -> SparkExternalEncoderSim:
        ...
class SparkLimitSwitch:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def get(self) -> bool:
        """
        Get the state of the limit switch, whether or not it is enabled
        (limiting the rotation of the motor).
        """
class SparkLimitSwitchSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, motor: SparkMax, forward: bool) -> None:
        ...
    @typing.overload
    def __init__(self, motor: SparkFlex, forward: bool) -> None:
        ...
    def getEnabled(self) -> bool:
        ...
    def getPressed(self) -> bool:
        ...
    def setPressed(self, state: bool) -> None:
        ...
class SparkLowLevel(wpilib.interfaces._interfaces.MotorController):
    class ControlType:
        """
        Members:
        
          kDutyCycle
        
          kVelocity
        
          kVoltage
        
          kPosition
        
          kSmartMotion : 
        
        :deprecated: It is recommended to migrate to MAXMotion Velocity mode
                     instead.
        
          kCurrent
        
          kSmartVelocity : 
        
        :deprecated: It is recommended to migrate to MAXMotion Velocity mode
                     instead.
        
          kMAXMotionPositionControl
        
          kMAXMotionVelocityControl
        """
        __members__: typing.ClassVar[dict[str, SparkLowLevel.ControlType]]  # value = {'kDutyCycle': <ControlType.kDutyCycle: 0>, 'kVelocity': <ControlType.kVelocity: 1>, 'kVoltage': <ControlType.kVoltage: 2>, 'kPosition': <ControlType.kPosition: 3>, 'kSmartMotion': <ControlType.kSmartMotion: 4>, 'kCurrent': <ControlType.kCurrent: 5>, 'kSmartVelocity': <ControlType.kSmartVelocity: 6>, 'kMAXMotionPositionControl': <ControlType.kMAXMotionPositionControl: 7>, 'kMAXMotionVelocityControl': <ControlType.kMAXMotionVelocityControl: 8>}
        kCurrent: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kCurrent: 5>
        kDutyCycle: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kDutyCycle: 0>
        kMAXMotionPositionControl: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kMAXMotionPositionControl: 7>
        kMAXMotionVelocityControl: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kMAXMotionVelocityControl: 8>
        kPosition: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kPosition: 3>
        kSmartMotion: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kSmartMotion: 4>
        kSmartVelocity: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kSmartVelocity: 6>
        kVelocity: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kVelocity: 1>
        kVoltage: typing.ClassVar[SparkLowLevel.ControlType]  # value = <ControlType.kVoltage: 2>
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
    class MotorType:
        """
        Members:
        
          kBrushed
        
          kBrushless
        """
        __members__: typing.ClassVar[dict[str, SparkLowLevel.MotorType]]  # value = {'kBrushed': <MotorType.kBrushed: 0>, 'kBrushless': <MotorType.kBrushless: 1>}
        kBrushed: typing.ClassVar[SparkLowLevel.MotorType]  # value = <MotorType.kBrushed: 0>
        kBrushless: typing.ClassVar[SparkLowLevel.MotorType]  # value = <MotorType.kBrushless: 1>
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
    class ParameterStatus:
        """
        Members:
        
          kOK
        
          kInvalidID
        
          kMismatchType
        
          kAccessMode
        
          kInvalid
        
          kNotImplementedDeprecated
        """
        __members__: typing.ClassVar[dict[str, SparkLowLevel.ParameterStatus]]  # value = {'kOK': <ParameterStatus.kOK: 0>, 'kInvalidID': <ParameterStatus.kInvalidID: 1>, 'kMismatchType': <ParameterStatus.kMismatchType: 2>, 'kAccessMode': <ParameterStatus.kAccessMode: 3>, 'kInvalid': <ParameterStatus.kInvalid: 4>, 'kNotImplementedDeprecated': <ParameterStatus.kNotImplementedDeprecated: 5>}
        kAccessMode: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kAccessMode: 3>
        kInvalid: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kInvalid: 4>
        kInvalidID: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kInvalidID: 1>
        kMismatchType: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kMismatchType: 2>
        kNotImplementedDeprecated: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kNotImplementedDeprecated: 5>
        kOK: typing.ClassVar[SparkLowLevel.ParameterStatus]  # value = <ParameterStatus.kOK: 0>
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
    class PeriodicFrame:
        """
        Members:
        
          kStatus0
        
          kStatus1
        
          kStatus2
        
          kStatus3
        
          kStatus4
        
          kStatus5
        
          kStatus6
        
          kStatus7
        """
        __members__: typing.ClassVar[dict[str, SparkLowLevel.PeriodicFrame]]  # value = {'kStatus0': <PeriodicFrame.kStatus0: 0>, 'kStatus1': <PeriodicFrame.kStatus1: 1>, 'kStatus2': <PeriodicFrame.kStatus2: 2>, 'kStatus3': <PeriodicFrame.kStatus3: 3>, 'kStatus4': <PeriodicFrame.kStatus4: 4>, 'kStatus5': <PeriodicFrame.kStatus5: 5>, 'kStatus6': <PeriodicFrame.kStatus6: 6>, 'kStatus7': <PeriodicFrame.kStatus7: 7>}
        kStatus0: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus0: 0>
        kStatus1: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus1: 1>
        kStatus2: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus2: 2>
        kStatus3: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus3: 3>
        kStatus4: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus4: 4>
        kStatus5: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus5: 5>
        kStatus6: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus6: 6>
        kStatus7: typing.ClassVar[SparkLowLevel.PeriodicFrame]  # value = <PeriodicFrame.kStatus7: 7>
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
    class PeriodicStatus0:
        appliedOutput: float
        current: float
        hardForwardLimitReached: bool
        hardReverseLimitReached: bool
        inverted: bool
        motorTemperature: int
        primaryHeartbeatLock: bool
        softForwardLimitReached: bool
        softReverseLimitReached: bool
        timestamp: int
        voltage: float
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus1:
        brownoutStickyWarning: bool
        brownoutWarning: bool
        canFault: bool
        canStickyFault: bool
        drvFault: bool
        drvStickyFault: bool
        escEepromFault: bool
        escEepromStickyFault: bool
        escEepromStickyWarning: bool
        escEepromWarning: bool
        extEepromStickyWarning: bool
        extEepromWarning: bool
        firmwareFault: bool
        firmwareStickyFault: bool
        hasResetStickyWarning: bool
        hasResetWarning: bool
        isFollower: bool
        motorTypeFault: bool
        motorTypeStickyFault: bool
        otherFault: bool
        otherStickyFault: bool
        otherStickyWarning: bool
        otherWarning: bool
        overcurrentStickyWarning: bool
        overcurrentWarning: bool
        sensorFault: bool
        sensorStickyFault: bool
        sensorStickyWarning: bool
        sensorWarning: bool
        stallStickyWarning: bool
        stallWarning: bool
        temperatureFault: bool
        temperatureStickyFault: bool
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus2:
        primaryEncoderPosition: float
        primaryEncoderVelocity: float
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus3:
        analogPosition: float
        analogVelocity: float
        analogVoltage: float
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus4:
        externalOrAltEncoderPosition: float
        externalOrAltEncoderVelocity: float
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus5:
        dutyCycleEncoderPosition: float
        dutyCycleEncoderVelocity: float
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus6:
        dutyCycleNoSignal: int
        dutyCyclePeriod: float
        timestamp: int
        unadjustedDutyCycle: float
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class PeriodicStatus7:
        iAccumulation: float
        timestamp: int
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    class SparkModel:
        """
        Members:
        
          kSparkMax
        
          kSparkFlex
        
          kUnknown
        """
        __members__: typing.ClassVar[dict[str, SparkLowLevel.SparkModel]]  # value = {'kSparkMax': <SparkModel.kSparkMax: 0>, 'kSparkFlex': <SparkModel.kSparkFlex: 1>, 'kUnknown': <SparkModel.kUnknown: 255>}
        kSparkFlex: typing.ClassVar[SparkLowLevel.SparkModel]  # value = <SparkModel.kSparkFlex: 1>
        kSparkMax: typing.ClassVar[SparkLowLevel.SparkModel]  # value = <SparkModel.kSparkMax: 0>
        kUnknown: typing.ClassVar[SparkLowLevel.SparkModel]  # value = <SparkModel.kUnknown: 255>
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
    kAPIBuildVersion: typing.ClassVar[int] = 2
    kAPIMajorVersion: typing.ClassVar[int] = 233
    kAPIMinorVersion: typing.ClassVar[int] = 0
    kAPIVersion: typing.ClassVar[int] = 132710402
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def createSimFaultManager(self) -> None:
        """
        Create the sim gui Fault Manager for this Spark Device
        """
    def getDeviceId(self) -> int:
        """
        Get the configured Device ID of the SPARK.
        
        :returns: int device ID
        """
    def getFirmwareString(self) -> str:
        """
        Get the firmware version of the SPARK as a string.
        
        :returns: std::string Human readable firmware version string
        """
    @typing.overload
    def getFirmwareVersion(self) -> int:
        """
        Get the firmware version of the SPARK.
        
        :returns: uint32_t Firmware version integer. Value is represented as 4
                  bytes, Major.Minor.Build H.Build L
        """
    @typing.overload
    def getFirmwareVersion(self) -> tuple[int, bool]:
        ...
    def getMotorType(self) -> SparkLowLevel.MotorType:
        """
        Get the motor type setting for the SPARK.
        
        :returns: MotorType Motor type setting
        """
    def getSerialNumber(self) -> list[int]:
        """
        Get the unique serial number of the SPARK. Currently not implemented.
        
        :returns: std::vector<uint8_t> Vector of bytes representig the unique
                  serial number
        """
    def setCANMaxRetries(self, numRetries: int) -> None:
        """
        Set the maximum number of times to retry an RTR CAN frame. This applies
        to calls such as SetParameter* and GetParameter* where a request is made
        to the SPARK motor controller and a response is expected. Anytime sending
        the request or receiving the response fails, it will retry the request a
        number of times, no more than the value set by this method. If an attempt
        succeeds, it will immediately return. The minimum number of retries is 0,
        where only a single attempt will be made and will return regardless of
        success or failure.
        
        The default maximum is 5 retries.
        
        :param numRetries: The maximum number of retries
        """
    def setControlFramePeriodMs(self, periodMs: int) -> None:
        """
        Set the control frame send period for the native CAN Send thread. To
        disable periodic sends, set periodMs to 0.
        
        :param periodMs: The send period in milliseconds between 1ms and 100ms
                         or set to 0 to disable periodic sends. Note this is not updated until
                         the next call to Set() or SetReference().
        """
    def setPeriodicFrameTimeout(self, timeoutMs: int) -> None:
        """
        Set the amount of time to wait for a periodic status frame before
        returning a timeout error. This timeout will apply to all periodic status
        frames for the SPARK motor controller.
        
        To prevent invalid timeout errors, the minimum timeout for a given
        periodic status is 2.1 times its period. To use the minimum timeout for
        all status frames, set timeoutMs to 0.
        
        The default timeout is 500ms.
        
        :param timeoutMs: The timeout in milliseconds
        """
class SparkMax(SparkBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, deviceID: int, type: SparkLowLevel.MotorType) -> None:
        """
        Create a new object to control a SPARK MAX motor Controller
        
        :param deviceID: The device ID.
        :param type:     The motor type connected to the controller. Brushless
                         motor wires must be connected to their matching colors,
                         and the hall sensor must be plugged in. Brushed motors must be connected
                         to the Red and Black terminals only.
        """
    def configure(self, config: SparkBaseConfig, resetMode: SparkBase.ResetMode, persistMode: SparkBase.PersistMode) -> REVLibError:
        ...
    def getAbsoluteEncoder(self) -> SparkAbsoluteEncoder:
        ...
    def getAlternateEncoder(self) -> SparkMaxAlternateEncoder:
        """
        Returns an object for interfacing with a quadrature encoder connected to
        the alternate encoder mode data port pins. These are defined as:
        
        Pin 4 (Forward Limit Switch): Index
        Pin 6 (Multi-function): Encoder A
        Pin 8 (Reverse Limit Switch): Encoder B
        
        This call will disable support for the limit switch inputs.
        """
    def getForwardLimitSwitch(self) -> SparkLimitSwitch:
        ...
    def getReverseLimitSwitch(self) -> SparkLimitSwitch:
        ...
    @property
    def configAccessor(self) -> SparkMaxConfigAccessor:
        """
        Accessor for SPARK parameter values. This object contains fields and
        methods to retrieve parameters that have been applied to the device. To
        set parameters, see SparkBaseConfig and SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and should
        be used infrequently.
        """
class SparkMaxAlternateEncoder(RelativeEncoder):
    """
    Get an instance of this class by using SparkMax::GetEncoder() or
    SparkMax::GetEncoder(SparkMax::EncoderType, int).
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().
        
        :returns: Number the RPM of the motor
        """
    def setPosition(self, position: float) -> REVLibError:
        """
        Set the position of the encoder.
        
        :param position: Number of rotations of the motor
        
        :returns: REVLibError::kOk if successful
        """
class SparkMaxAlternateEncoderSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, motor: SparkMax) -> None:
        ...
    def getInverted(self) -> bool:
        ...
    def getPosition(self) -> float:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getZeroOffset(self) -> float:
        ...
    def iterate(self, velocity: float, dt: float) -> None:
        ...
    def setInverted(self, inverted: bool) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setPositionConversionFactor(self, positionConversionFactor: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def setVelocityConversionFactor(self, velocityConversionFactor: float) -> None:
        ...
    def setZeroOffset(self, zeroOffset: float) -> None:
        ...
class SparkMaxConfig(SparkBaseConfig):
    class DataPortConfig:
        """
        Members:
        
          kInvalid
        
          kLimitSwitchesAndAbsoluteEncoder
        
          kAlternateEncoder
        """
        __members__: typing.ClassVar[dict[str, SparkMaxConfig.DataPortConfig]]  # value = {'kInvalid': <DataPortConfig.kInvalid: -1>, 'kLimitSwitchesAndAbsoluteEncoder': <DataPortConfig.kLimitSwitchesAndAbsoluteEncoder: 0>, 'kAlternateEncoder': <DataPortConfig.kAlternateEncoder: 1>}
        kAlternateEncoder: typing.ClassVar[SparkMaxConfig.DataPortConfig]  # value = <DataPortConfig.kAlternateEncoder: 1>
        kInvalid: typing.ClassVar[SparkMaxConfig.DataPortConfig]  # value = <DataPortConfig.kInvalid: -1>
        kLimitSwitchesAndAbsoluteEncoder: typing.ClassVar[SparkMaxConfig.DataPortConfig]  # value = <DataPortConfig.kLimitSwitchesAndAbsoluteEncoder: 0>
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
    def __init__(self) -> None:
        ...
    @typing.overload
    def apply(self, config: SparkMaxConfig) -> SparkMaxConfig:
        """
        Applies settings from another  SparkMaxConfig to this one,
        including all of its nested configurations.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The SparkMaxConfig to copy settings from
        
        :returns: The updated SparkMaxConfig for method chaining
        """
    @typing.overload
    def apply(self, config: AlternateEncoderConfig) -> SparkMaxConfig:
        """
        Applies settings from an  AlternateEncoderConfig to this
        SparkMaxConfig.
        
        Settings in the provided config will overwrite existing values in this
        object. Settings not specified in the provided config remain unchanged.
        
        :param config: The AlternateEncoderConfig to copy settings from
        
        :returns: The updated SparkMaxConfig for method chaining
        """
    @typing.overload
    def apply(self, config: SparkBaseConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: AbsoluteEncoderConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: AnalogSensorConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: EncoderConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: LimitSwitchConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: SoftLimitConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: ClosedLoopConfig) -> SparkMaxConfig:
        ...
    @typing.overload
    def apply(self, config: SignalsConfig) -> SparkMaxConfig:
        ...
    def flatten(self) -> str:
        ...
    @property
    def alternateEncoder(self) -> AlternateEncoderConfig:
        ...
class SparkMaxConfigAccessor(SparkBaseConfigAccessor):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def alternateEncoder(self) -> AlternateEncoderConfigAccessor:
        """
        Accessor for parameters relating to the alternate encoder. To configure
        these values, use AlternateEncoderConfig and call
        SparkBase::Configure.
        
        NOTE: This uses calls that are blocking to retrieve parameters and
        should be used infrequently.
        """
class SparkMaxSim(SparkSim):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, sparkMax: SparkMax, motor: wpimath._controls._controls.plant.DCMotor) -> None:
        ...
    def getAlternateEncoderSim(self) -> SparkMaxAlternateEncoderSim:
        ...
class SparkParameter:
    """
    Members:
    
      kCanID
    
      kInputMode
    
      kMotorType
    
      kCommAdvance
    
      kSensorType
    
      kCtrlType
    
      kIdleMode
    
      kInputDeadband
    
      kLegacyFeedbackSensorPID0
    
      kClosedLoopControlSensor
    
      kPolePairs
    
      kCurrentChop
    
      kCurrentChopCycles
    
      kP_0
    
      kI_0
    
      kD_0
    
      kF_0
    
      kIZone_0
    
      kDFilter_0
    
      kOutputMin_0
    
      kOutputMax_0
    
      kP_1
    
      kI_1
    
      kD_1
    
      kF_1
    
      kIZone_1
    
      kDFilter_1
    
      kOutputMin_1
    
      kOutputMax_1
    
      kP_2
    
      kI_2
    
      kD_2
    
      kF_2
    
      kIZone_2
    
      kDFilter_2
    
      kOutputMin_2
    
      kOutputMax_2
    
      kP_3
    
      kI_3
    
      kD_3
    
      kF_3
    
      kIZone_3
    
      kDFilter_3
    
      kOutputMin_3
    
      kOutputMax_3
    
      kInverted
    
      kOutputRatio
    
      kSerialNumberLow
    
      kSerialNumberMid
    
      kSerialNumberHigh
    
      kLimitSwitchFwdPolarity
    
      kLimitSwitchRevPolarity
    
      kHardLimitFwdEn
    
      kHardLimitRevEn
    
      kSoftLimitFwdEn
    
      kSoftLimitRevEn
    
      kRampRate
    
      kFollowerID
    
      kFollowerConfig
    
      kSmartCurrentStallLimit
    
      kSmartCurrentFreeLimit
    
      kSmartCurrentConfig
    
      kSmartCurrentReserved
    
      kMotorKv
    
      kMotorR
    
      kMotorL
    
      kMotorRsvd1
    
      kMotorRsvd2
    
      kMotorRsvd3
    
      kEncoderCountsPerRev
    
      kEncoderAverageDepth
    
      kEncoderSampleDelta
    
      kEncoderInverted
    
      kEncoderRsvd1
    
      kVoltageCompMode
    
      kCompensatedNominalVoltage
    
      kSmartMotionMaxVelocity_0
    
      kSmartMotionMaxAccel_0
    
      kSmartMotionMinVelOutput_0
    
      kSmartMotionAllowedClosedLoopError_0
    
      kSmartMotionAccelStrategy_0
    
      kSmartMotionMaxVelocity_1
    
      kSmartMotionMaxAccel_1
    
      kSmartMotionMinVelOutput_1
    
      kSmartMotionAllowedClosedLoopError_1
    
      kSmartMotionAccelStrategy_1
    
      kSmartMotionMaxVelocity_2
    
      kSmartMotionMaxAccel_2
    
      kSmartMotionMinVelOutput_2
    
      kSmartMotionAllowedClosedLoopError_2
    
      kSmartMotionAccelStrategy_2
    
      kSmartMotionMaxVelocity_3
    
      kSmartMotionMaxAccel_3
    
      kSmartMotionMinVelOutput_3
    
      kSmartMotionAllowedClosedLoopError_3
    
      kSmartMotionAccelStrategy_3
    
      kIMaxAccum_0
    
      kSlot3Placeholder1_0
    
      kSlot3Placeholder2_0
    
      kSlot3Placeholder3_0
    
      kIMaxAccum_1
    
      kSlot3Placeholder1_1
    
      kSlot3Placeholder2_1
    
      kSlot3Placeholder3_1
    
      kIMaxAccum_2
    
      kSlot3Placeholder1_2
    
      kSlot3Placeholder2_2
    
      kSlot3Placeholder3_2
    
      kIMaxAccum_3
    
      kSlot3Placeholder1_3
    
      kSlot3Placeholder2_3
    
      kSlot3Placeholder3_3
    
      kPositionConversionFactor
    
      kVelocityConversionFactor
    
      kClosedLoopRampRate
    
      kSoftLimitFwd
    
      kSoftLimitRev
    
      kSoftLimitRsvd0
    
      kSoftLimitRsvd1
    
      kAnalogRevPerVolt
    
      kAnalogRotationsPerVoltSec
    
      kAnalogAverageDepth
    
      kAnalogSensorMode
    
      kAnalogInverted
    
      kAnalogSampleDelta
    
      kAnalogRsvd0
    
      kAnalogRsvd1
    
      kDataPortConfig
    
      kAltEncoderCountsPerRev
    
      kAltEncoderAverageDepth
    
      kAltEncoderSampleDelta
    
      kAltEncoderInverted
    
      kAltEncodePositionFactor
    
      kAltEncoderVelocityFactor
    
      kAltEncoderRsvd0
    
      kAltEncoderRsvd1
    
      kHallSensorSampleRate
    
      kHallSensorAverageDepth
    
      kNumParameters
    
      kDutyCyclePositionFactor
    
      kDutyCycleVelocityFactor
    
      kDutyCycleInverted
    
      kDutyCycleSensorMode
    
      kDutyCycleAverageDepth
    
      kDutyCycleSampleDelta
    
      kDutyCycleOffsetv1p6p2
    
      kDutyCycleRsvd0
    
      kDutyCycleRsvd1
    
      kDutyCycleRsvd2
    
      kPositionPIDWrapEnable
    
      kPositionPIDMinInput
    
      kPositionPIDMaxInput
    
      kDutyCycleZeroCentered
    
      kDutyCyclePrescaler
    
      kDutyCycleOffset
    
      kProductId
    
      kDeviceMajorVersion
    
      kDeviceMinorVersion
    
      kStatus0Period
    
      kStatus1Period
    
      kStatus2Period
    
      kStatus3Period
    
      kStatus4Period
    
      kStatus5Period
    
      kStatus6Period
    
      kStatus7Period
    
      kMAXMotionMaxVelocity_0
    
      kMAXMotionMaxAccel_0
    
      kMAXMotionMaxJerk_0
    
      kMAXMotionAllowedClosedLoopError_0
    
      kMAXMotionPositionMode_0
    
      kMAXMotionMaxVelocity_1
    
      kMAXMotionMaxAccel_1
    
      kMAXMotionMaxJerk_1
    
      kMAXMotionAllowedClosedLoopError_1
    
      kMAXMotionPositionMode_1
    
      kMAXMotionMaxVelocity_2
    
      kMAXMotionMaxAccel_2
    
      kMAXMotionMaxJerk_2
    
      kMAXMotionAllowedClosedLoopError_2
    
      kMAXMotionPositionMode_2
    
      kMAXMotionMaxVelocity_3
    
      kMAXMotionMaxAccel_3
    
      kMAXMotionMaxJerk_3
    
      kMAXMotionAllowedClosedLoopError_3
    
      kMAXMotionPositionMode_3
    
      kForceEnableStatus0
    
      kForceEnableStatus1
    
      kForceEnableStatus2
    
      kForceEnableStatus3
    
      kForceEnableStatus4
    
      kForceEnableStatus5
    
      kForceEnableStatus6
    
      kForceEnableStatus7
    
      kFollowerModeLeaderId
    
      kFollowerModeIsInverted
    
      kDutyCycleEncoderStartPulseUs
    
      kDutyCycleEncoderEndPulseUs
    """
    __members__: typing.ClassVar[dict[str, SparkParameter]]  # value = {'kCanID': <SparkParameter.kCanID: 0>, 'kInputMode': <SparkParameter.kInputMode: 1>, 'kMotorType': <SparkParameter.kMotorType: 2>, 'kCommAdvance': <SparkParameter.kCommAdvance: 3>, 'kSensorType': <SparkParameter.kSensorType: 4>, 'kCtrlType': <SparkParameter.kCtrlType: 5>, 'kIdleMode': <SparkParameter.kIdleMode: 6>, 'kInputDeadband': <SparkParameter.kInputDeadband: 7>, 'kLegacyFeedbackSensorPID0': <SparkParameter.kLegacyFeedbackSensorPID0: 8>, 'kClosedLoopControlSensor': <SparkParameter.kClosedLoopControlSensor: 9>, 'kPolePairs': <SparkParameter.kPolePairs: 10>, 'kCurrentChop': <SparkParameter.kCurrentChop: 11>, 'kCurrentChopCycles': <SparkParameter.kCurrentChopCycles: 12>, 'kP_0': <SparkParameter.kP_0: 13>, 'kI_0': <SparkParameter.kI_0: 14>, 'kD_0': <SparkParameter.kD_0: 15>, 'kF_0': <SparkParameter.kF_0: 16>, 'kIZone_0': <SparkParameter.kIZone_0: 17>, 'kDFilter_0': <SparkParameter.kDFilter_0: 18>, 'kOutputMin_0': <SparkParameter.kOutputMin_0: 19>, 'kOutputMax_0': <SparkParameter.kOutputMax_0: 20>, 'kP_1': <SparkParameter.kP_1: 21>, 'kI_1': <SparkParameter.kI_1: 22>, 'kD_1': <SparkParameter.kD_1: 23>, 'kF_1': <SparkParameter.kF_1: 24>, 'kIZone_1': <SparkParameter.kIZone_1: 25>, 'kDFilter_1': <SparkParameter.kDFilter_1: 26>, 'kOutputMin_1': <SparkParameter.kOutputMin_1: 27>, 'kOutputMax_1': <SparkParameter.kOutputMax_1: 28>, 'kP_2': <SparkParameter.kP_2: 29>, 'kI_2': <SparkParameter.kI_2: 30>, 'kD_2': <SparkParameter.kD_2: 31>, 'kF_2': <SparkParameter.kF_2: 32>, 'kIZone_2': <SparkParameter.kIZone_2: 33>, 'kDFilter_2': <SparkParameter.kDFilter_2: 34>, 'kOutputMin_2': <SparkParameter.kOutputMin_2: 35>, 'kOutputMax_2': <SparkParameter.kOutputMax_2: 36>, 'kP_3': <SparkParameter.kP_3: 37>, 'kI_3': <SparkParameter.kI_3: 38>, 'kD_3': <SparkParameter.kD_3: 39>, 'kF_3': <SparkParameter.kF_3: 40>, 'kIZone_3': <SparkParameter.kIZone_3: 41>, 'kDFilter_3': <SparkParameter.kDFilter_3: 42>, 'kOutputMin_3': <SparkParameter.kOutputMin_3: 43>, 'kOutputMax_3': <SparkParameter.kOutputMax_3: 44>, 'kInverted': <SparkParameter.kInverted: 45>, 'kOutputRatio': <SparkParameter.kOutputRatio: 46>, 'kSerialNumberLow': <SparkParameter.kSerialNumberLow: 47>, 'kSerialNumberMid': <SparkParameter.kSerialNumberMid: 48>, 'kSerialNumberHigh': <SparkParameter.kSerialNumberHigh: 49>, 'kLimitSwitchFwdPolarity': <SparkParameter.kLimitSwitchFwdPolarity: 50>, 'kLimitSwitchRevPolarity': <SparkParameter.kLimitSwitchRevPolarity: 51>, 'kHardLimitFwdEn': <SparkParameter.kHardLimitFwdEn: 52>, 'kHardLimitRevEn': <SparkParameter.kHardLimitRevEn: 53>, 'kSoftLimitFwdEn': <SparkParameter.kSoftLimitFwdEn: 54>, 'kSoftLimitRevEn': <SparkParameter.kSoftLimitRevEn: 55>, 'kRampRate': <SparkParameter.kRampRate: 56>, 'kFollowerID': <SparkParameter.kFollowerID: 57>, 'kFollowerConfig': <SparkParameter.kFollowerConfig: 58>, 'kSmartCurrentStallLimit': <SparkParameter.kSmartCurrentStallLimit: 59>, 'kSmartCurrentFreeLimit': <SparkParameter.kSmartCurrentFreeLimit: 60>, 'kSmartCurrentConfig': <SparkParameter.kSmartCurrentConfig: 61>, 'kSmartCurrentReserved': <SparkParameter.kSmartCurrentReserved: 62>, 'kMotorKv': <SparkParameter.kMotorKv: 63>, 'kMotorR': <SparkParameter.kMotorR: 64>, 'kMotorL': <SparkParameter.kMotorL: 65>, 'kMotorRsvd1': <SparkParameter.kMotorRsvd1: 66>, 'kMotorRsvd2': <SparkParameter.kMotorRsvd2: 67>, 'kMotorRsvd3': <SparkParameter.kMotorRsvd3: 68>, 'kEncoderCountsPerRev': <SparkParameter.kEncoderCountsPerRev: 69>, 'kEncoderAverageDepth': <SparkParameter.kEncoderAverageDepth: 70>, 'kEncoderSampleDelta': <SparkParameter.kEncoderSampleDelta: 71>, 'kEncoderInverted': <SparkParameter.kEncoderInverted: 72>, 'kEncoderRsvd1': <SparkParameter.kEncoderRsvd1: 73>, 'kVoltageCompMode': <SparkParameter.kVoltageCompMode: 74>, 'kCompensatedNominalVoltage': <SparkParameter.kCompensatedNominalVoltage: 75>, 'kSmartMotionMaxVelocity_0': <SparkParameter.kSmartMotionMaxVelocity_0: 76>, 'kSmartMotionMaxAccel_0': <SparkParameter.kSmartMotionMaxAccel_0: 77>, 'kSmartMotionMinVelOutput_0': <SparkParameter.kSmartMotionMinVelOutput_0: 78>, 'kSmartMotionAllowedClosedLoopError_0': <SparkParameter.kSmartMotionAllowedClosedLoopError_0: 79>, 'kSmartMotionAccelStrategy_0': <SparkParameter.kSmartMotionAccelStrategy_0: 80>, 'kSmartMotionMaxVelocity_1': <SparkParameter.kSmartMotionMaxVelocity_1: 81>, 'kSmartMotionMaxAccel_1': <SparkParameter.kSmartMotionMaxAccel_1: 82>, 'kSmartMotionMinVelOutput_1': <SparkParameter.kSmartMotionMinVelOutput_1: 83>, 'kSmartMotionAllowedClosedLoopError_1': <SparkParameter.kSmartMotionAllowedClosedLoopError_1: 84>, 'kSmartMotionAccelStrategy_1': <SparkParameter.kSmartMotionAccelStrategy_1: 85>, 'kSmartMotionMaxVelocity_2': <SparkParameter.kSmartMotionMaxVelocity_2: 86>, 'kSmartMotionMaxAccel_2': <SparkParameter.kSmartMotionMaxAccel_2: 87>, 'kSmartMotionMinVelOutput_2': <SparkParameter.kSmartMotionMinVelOutput_2: 88>, 'kSmartMotionAllowedClosedLoopError_2': <SparkParameter.kSmartMotionAllowedClosedLoopError_2: 89>, 'kSmartMotionAccelStrategy_2': <SparkParameter.kSmartMotionAccelStrategy_2: 90>, 'kSmartMotionMaxVelocity_3': <SparkParameter.kSmartMotionMaxVelocity_3: 91>, 'kSmartMotionMaxAccel_3': <SparkParameter.kSmartMotionMaxAccel_3: 92>, 'kSmartMotionMinVelOutput_3': <SparkParameter.kSmartMotionMinVelOutput_3: 93>, 'kSmartMotionAllowedClosedLoopError_3': <SparkParameter.kSmartMotionAllowedClosedLoopError_3: 94>, 'kSmartMotionAccelStrategy_3': <SparkParameter.kSmartMotionAccelStrategy_3: 95>, 'kIMaxAccum_0': <SparkParameter.kIMaxAccum_0: 96>, 'kSlot3Placeholder1_0': <SparkParameter.kSlot3Placeholder1_0: 97>, 'kSlot3Placeholder2_0': <SparkParameter.kSlot3Placeholder2_0: 98>, 'kSlot3Placeholder3_0': <SparkParameter.kSlot3Placeholder3_0: 99>, 'kIMaxAccum_1': <SparkParameter.kIMaxAccum_1: 100>, 'kSlot3Placeholder1_1': <SparkParameter.kSlot3Placeholder1_1: 101>, 'kSlot3Placeholder2_1': <SparkParameter.kSlot3Placeholder2_1: 102>, 'kSlot3Placeholder3_1': <SparkParameter.kSlot3Placeholder3_1: 103>, 'kIMaxAccum_2': <SparkParameter.kIMaxAccum_2: 104>, 'kSlot3Placeholder1_2': <SparkParameter.kSlot3Placeholder1_2: 105>, 'kSlot3Placeholder2_2': <SparkParameter.kSlot3Placeholder2_2: 106>, 'kSlot3Placeholder3_2': <SparkParameter.kSlot3Placeholder3_2: 107>, 'kIMaxAccum_3': <SparkParameter.kIMaxAccum_3: 108>, 'kSlot3Placeholder1_3': <SparkParameter.kSlot3Placeholder1_3: 109>, 'kSlot3Placeholder2_3': <SparkParameter.kSlot3Placeholder2_3: 110>, 'kSlot3Placeholder3_3': <SparkParameter.kSlot3Placeholder3_3: 111>, 'kPositionConversionFactor': <SparkParameter.kPositionConversionFactor: 112>, 'kVelocityConversionFactor': <SparkParameter.kVelocityConversionFactor: 113>, 'kClosedLoopRampRate': <SparkParameter.kClosedLoopRampRate: 114>, 'kSoftLimitFwd': <SparkParameter.kSoftLimitFwd: 115>, 'kSoftLimitRev': <SparkParameter.kSoftLimitRev: 116>, 'kSoftLimitRsvd0': <SparkParameter.kSoftLimitRsvd0: 117>, 'kSoftLimitRsvd1': <SparkParameter.kSoftLimitRsvd1: 118>, 'kAnalogRevPerVolt': <SparkParameter.kAnalogRevPerVolt: 119>, 'kAnalogRotationsPerVoltSec': <SparkParameter.kAnalogRotationsPerVoltSec: 120>, 'kAnalogAverageDepth': <SparkParameter.kAnalogAverageDepth: 121>, 'kAnalogSensorMode': <SparkParameter.kAnalogSensorMode: 122>, 'kAnalogInverted': <SparkParameter.kAnalogInverted: 123>, 'kAnalogSampleDelta': <SparkParameter.kAnalogSampleDelta: 124>, 'kAnalogRsvd0': <SparkParameter.kAnalogRsvd0: 125>, 'kAnalogRsvd1': <SparkParameter.kAnalogRsvd1: 126>, 'kDataPortConfig': <SparkParameter.kDataPortConfig: 127>, 'kAltEncoderCountsPerRev': <SparkParameter.kAltEncoderCountsPerRev: 128>, 'kAltEncoderAverageDepth': <SparkParameter.kAltEncoderAverageDepth: 129>, 'kAltEncoderSampleDelta': <SparkParameter.kAltEncoderSampleDelta: 130>, 'kAltEncoderInverted': <SparkParameter.kAltEncoderInverted: 131>, 'kAltEncodePositionFactor': <SparkParameter.kAltEncodePositionFactor: 132>, 'kAltEncoderVelocityFactor': <SparkParameter.kAltEncoderVelocityFactor: 133>, 'kAltEncoderRsvd0': <SparkParameter.kAltEncoderRsvd0: 134>, 'kAltEncoderRsvd1': <SparkParameter.kAltEncoderRsvd1: 135>, 'kHallSensorSampleRate': <SparkParameter.kHallSensorSampleRate: 136>, 'kHallSensorAverageDepth': <SparkParameter.kHallSensorAverageDepth: 137>, 'kNumParameters': <SparkParameter.kNumParameters: 138>, 'kDutyCyclePositionFactor': <SparkParameter.kDutyCyclePositionFactor: 139>, 'kDutyCycleVelocityFactor': <SparkParameter.kDutyCycleVelocityFactor: 140>, 'kDutyCycleInverted': <SparkParameter.kDutyCycleInverted: 141>, 'kDutyCycleSensorMode': <SparkParameter.kDutyCycleSensorMode: 142>, 'kDutyCycleAverageDepth': <SparkParameter.kDutyCycleAverageDepth: 143>, 'kDutyCycleSampleDelta': <SparkParameter.kDutyCycleSampleDelta: 144>, 'kDutyCycleOffsetv1p6p2': <SparkParameter.kDutyCycleOffsetv1p6p2: 145>, 'kDutyCycleRsvd0': <SparkParameter.kDutyCycleRsvd0: 146>, 'kDutyCycleRsvd1': <SparkParameter.kDutyCycleRsvd1: 147>, 'kDutyCycleRsvd2': <SparkParameter.kDutyCycleRsvd2: 148>, 'kPositionPIDWrapEnable': <SparkParameter.kPositionPIDWrapEnable: 149>, 'kPositionPIDMinInput': <SparkParameter.kPositionPIDMinInput: 150>, 'kPositionPIDMaxInput': <SparkParameter.kPositionPIDMaxInput: 151>, 'kDutyCycleZeroCentered': <SparkParameter.kDutyCycleZeroCentered: 152>, 'kDutyCyclePrescaler': <SparkParameter.kDutyCyclePrescaler: 153>, 'kDutyCycleOffset': <SparkParameter.kDutyCycleOffset: 154>, 'kProductId': <SparkParameter.kProductId: 155>, 'kDeviceMajorVersion': <SparkParameter.kDeviceMajorVersion: 156>, 'kDeviceMinorVersion': <SparkParameter.kDeviceMinorVersion: 157>, 'kStatus0Period': <SparkParameter.kStatus0Period: 158>, 'kStatus1Period': <SparkParameter.kStatus1Period: 159>, 'kStatus2Period': <SparkParameter.kStatus2Period: 160>, 'kStatus3Period': <SparkParameter.kStatus3Period: 161>, 'kStatus4Period': <SparkParameter.kStatus4Period: 162>, 'kStatus5Period': <SparkParameter.kStatus5Period: 163>, 'kStatus6Period': <SparkParameter.kStatus6Period: 164>, 'kStatus7Period': <SparkParameter.kStatus7Period: 165>, 'kMAXMotionMaxVelocity_0': <SparkParameter.kMAXMotionMaxVelocity_0: 166>, 'kMAXMotionMaxAccel_0': <SparkParameter.kMAXMotionMaxAccel_0: 167>, 'kMAXMotionMaxJerk_0': <SparkParameter.kMAXMotionMaxJerk_0: 168>, 'kMAXMotionAllowedClosedLoopError_0': <SparkParameter.kMAXMotionAllowedClosedLoopError_0: 169>, 'kMAXMotionPositionMode_0': <SparkParameter.kMAXMotionPositionMode_0: 170>, 'kMAXMotionMaxVelocity_1': <SparkParameter.kMAXMotionMaxVelocity_1: 171>, 'kMAXMotionMaxAccel_1': <SparkParameter.kMAXMotionMaxAccel_1: 172>, 'kMAXMotionMaxJerk_1': <SparkParameter.kMAXMotionMaxJerk_1: 173>, 'kMAXMotionAllowedClosedLoopError_1': <SparkParameter.kMAXMotionAllowedClosedLoopError_1: 174>, 'kMAXMotionPositionMode_1': <SparkParameter.kMAXMotionPositionMode_1: 175>, 'kMAXMotionMaxVelocity_2': <SparkParameter.kMAXMotionMaxVelocity_2: 176>, 'kMAXMotionMaxAccel_2': <SparkParameter.kMAXMotionMaxAccel_2: 177>, 'kMAXMotionMaxJerk_2': <SparkParameter.kMAXMotionMaxJerk_2: 178>, 'kMAXMotionAllowedClosedLoopError_2': <SparkParameter.kMAXMotionAllowedClosedLoopError_2: 179>, 'kMAXMotionPositionMode_2': <SparkParameter.kMAXMotionPositionMode_2: 180>, 'kMAXMotionMaxVelocity_3': <SparkParameter.kMAXMotionMaxVelocity_3: 181>, 'kMAXMotionMaxAccel_3': <SparkParameter.kMAXMotionMaxAccel_3: 182>, 'kMAXMotionMaxJerk_3': <SparkParameter.kMAXMotionMaxJerk_3: 183>, 'kMAXMotionAllowedClosedLoopError_3': <SparkParameter.kMAXMotionAllowedClosedLoopError_3: 184>, 'kMAXMotionPositionMode_3': <SparkParameter.kMAXMotionPositionMode_3: 185>, 'kForceEnableStatus0': <SparkParameter.kForceEnableStatus0: 186>, 'kForceEnableStatus1': <SparkParameter.kForceEnableStatus1: 187>, 'kForceEnableStatus2': <SparkParameter.kForceEnableStatus2: 188>, 'kForceEnableStatus3': <SparkParameter.kForceEnableStatus3: 189>, 'kForceEnableStatus4': <SparkParameter.kForceEnableStatus4: 190>, 'kForceEnableStatus5': <SparkParameter.kForceEnableStatus5: 191>, 'kForceEnableStatus6': <SparkParameter.kForceEnableStatus6: 192>, 'kForceEnableStatus7': <SparkParameter.kForceEnableStatus7: 193>, 'kFollowerModeLeaderId': <SparkParameter.kFollowerModeLeaderId: 194>, 'kFollowerModeIsInverted': <SparkParameter.kFollowerModeIsInverted: 195>, 'kDutyCycleEncoderStartPulseUs': <SparkParameter.kDutyCycleEncoderStartPulseUs: 196>, 'kDutyCycleEncoderEndPulseUs': <SparkParameter.kDutyCycleEncoderEndPulseUs: 197>}
    kAltEncodePositionFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncodePositionFactor: 132>
    kAltEncoderAverageDepth: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderAverageDepth: 129>
    kAltEncoderCountsPerRev: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderCountsPerRev: 128>
    kAltEncoderInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderInverted: 131>
    kAltEncoderRsvd0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderRsvd0: 134>
    kAltEncoderRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderRsvd1: 135>
    kAltEncoderSampleDelta: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderSampleDelta: 130>
    kAltEncoderVelocityFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAltEncoderVelocityFactor: 133>
    kAnalogAverageDepth: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogAverageDepth: 121>
    kAnalogInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogInverted: 123>
    kAnalogRevPerVolt: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogRevPerVolt: 119>
    kAnalogRotationsPerVoltSec: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogRotationsPerVoltSec: 120>
    kAnalogRsvd0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogRsvd0: 125>
    kAnalogRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogRsvd1: 126>
    kAnalogSampleDelta: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogSampleDelta: 124>
    kAnalogSensorMode: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kAnalogSensorMode: 122>
    kCanID: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCanID: 0>
    kClosedLoopControlSensor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kClosedLoopControlSensor: 9>
    kClosedLoopRampRate: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kClosedLoopRampRate: 114>
    kCommAdvance: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCommAdvance: 3>
    kCompensatedNominalVoltage: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCompensatedNominalVoltage: 75>
    kCtrlType: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCtrlType: 5>
    kCurrentChop: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCurrentChop: 11>
    kCurrentChopCycles: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kCurrentChopCycles: 12>
    kDFilter_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDFilter_0: 18>
    kDFilter_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDFilter_1: 26>
    kDFilter_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDFilter_2: 34>
    kDFilter_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDFilter_3: 42>
    kD_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kD_0: 15>
    kD_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kD_1: 23>
    kD_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kD_2: 31>
    kD_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kD_3: 39>
    kDataPortConfig: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDataPortConfig: 127>
    kDeviceMajorVersion: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDeviceMajorVersion: 156>
    kDeviceMinorVersion: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDeviceMinorVersion: 157>
    kDutyCycleAverageDepth: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleAverageDepth: 143>
    kDutyCycleEncoderEndPulseUs: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleEncoderEndPulseUs: 197>
    kDutyCycleEncoderStartPulseUs: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleEncoderStartPulseUs: 196>
    kDutyCycleInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleInverted: 141>
    kDutyCycleOffset: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleOffset: 154>
    kDutyCycleOffsetv1p6p2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleOffsetv1p6p2: 145>
    kDutyCyclePositionFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCyclePositionFactor: 139>
    kDutyCyclePrescaler: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCyclePrescaler: 153>
    kDutyCycleRsvd0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleRsvd0: 146>
    kDutyCycleRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleRsvd1: 147>
    kDutyCycleRsvd2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleRsvd2: 148>
    kDutyCycleSampleDelta: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleSampleDelta: 144>
    kDutyCycleSensorMode: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleSensorMode: 142>
    kDutyCycleVelocityFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleVelocityFactor: 140>
    kDutyCycleZeroCentered: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kDutyCycleZeroCentered: 152>
    kEncoderAverageDepth: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kEncoderAverageDepth: 70>
    kEncoderCountsPerRev: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kEncoderCountsPerRev: 69>
    kEncoderInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kEncoderInverted: 72>
    kEncoderRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kEncoderRsvd1: 73>
    kEncoderSampleDelta: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kEncoderSampleDelta: 71>
    kF_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kF_0: 16>
    kF_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kF_1: 24>
    kF_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kF_2: 32>
    kF_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kF_3: 40>
    kFollowerConfig: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kFollowerConfig: 58>
    kFollowerID: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kFollowerID: 57>
    kFollowerModeIsInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kFollowerModeIsInverted: 195>
    kFollowerModeLeaderId: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kFollowerModeLeaderId: 194>
    kForceEnableStatus0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus0: 186>
    kForceEnableStatus1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus1: 187>
    kForceEnableStatus2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus2: 188>
    kForceEnableStatus3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus3: 189>
    kForceEnableStatus4: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus4: 190>
    kForceEnableStatus5: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus5: 191>
    kForceEnableStatus6: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus6: 192>
    kForceEnableStatus7: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kForceEnableStatus7: 193>
    kHallSensorAverageDepth: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kHallSensorAverageDepth: 137>
    kHallSensorSampleRate: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kHallSensorSampleRate: 136>
    kHardLimitFwdEn: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kHardLimitFwdEn: 52>
    kHardLimitRevEn: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kHardLimitRevEn: 53>
    kIMaxAccum_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIMaxAccum_0: 96>
    kIMaxAccum_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIMaxAccum_1: 100>
    kIMaxAccum_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIMaxAccum_2: 104>
    kIMaxAccum_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIMaxAccum_3: 108>
    kIZone_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIZone_0: 17>
    kIZone_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIZone_1: 25>
    kIZone_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIZone_2: 33>
    kIZone_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIZone_3: 41>
    kI_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kI_0: 14>
    kI_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kI_1: 22>
    kI_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kI_2: 30>
    kI_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kI_3: 38>
    kIdleMode: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kIdleMode: 6>
    kInputDeadband: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kInputDeadband: 7>
    kInputMode: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kInputMode: 1>
    kInverted: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kInverted: 45>
    kLegacyFeedbackSensorPID0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kLegacyFeedbackSensorPID0: 8>
    kLimitSwitchFwdPolarity: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kLimitSwitchFwdPolarity: 50>
    kLimitSwitchRevPolarity: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kLimitSwitchRevPolarity: 51>
    kMAXMotionAllowedClosedLoopError_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionAllowedClosedLoopError_0: 169>
    kMAXMotionAllowedClosedLoopError_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionAllowedClosedLoopError_1: 174>
    kMAXMotionAllowedClosedLoopError_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionAllowedClosedLoopError_2: 179>
    kMAXMotionAllowedClosedLoopError_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionAllowedClosedLoopError_3: 184>
    kMAXMotionMaxAccel_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxAccel_0: 167>
    kMAXMotionMaxAccel_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxAccel_1: 172>
    kMAXMotionMaxAccel_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxAccel_2: 177>
    kMAXMotionMaxAccel_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxAccel_3: 182>
    kMAXMotionMaxJerk_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxJerk_0: 168>
    kMAXMotionMaxJerk_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxJerk_1: 173>
    kMAXMotionMaxJerk_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxJerk_2: 178>
    kMAXMotionMaxJerk_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxJerk_3: 183>
    kMAXMotionMaxVelocity_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxVelocity_0: 166>
    kMAXMotionMaxVelocity_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxVelocity_1: 171>
    kMAXMotionMaxVelocity_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxVelocity_2: 176>
    kMAXMotionMaxVelocity_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionMaxVelocity_3: 181>
    kMAXMotionPositionMode_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionPositionMode_0: 170>
    kMAXMotionPositionMode_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionPositionMode_1: 175>
    kMAXMotionPositionMode_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionPositionMode_2: 180>
    kMAXMotionPositionMode_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMAXMotionPositionMode_3: 185>
    kMotorKv: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorKv: 63>
    kMotorL: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorL: 65>
    kMotorR: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorR: 64>
    kMotorRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorRsvd1: 66>
    kMotorRsvd2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorRsvd2: 67>
    kMotorRsvd3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorRsvd3: 68>
    kMotorType: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kMotorType: 2>
    kNumParameters: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kNumParameters: 138>
    kOutputMax_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMax_0: 20>
    kOutputMax_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMax_1: 28>
    kOutputMax_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMax_2: 36>
    kOutputMax_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMax_3: 44>
    kOutputMin_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMin_0: 19>
    kOutputMin_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMin_1: 27>
    kOutputMin_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMin_2: 35>
    kOutputMin_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputMin_3: 43>
    kOutputRatio: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kOutputRatio: 46>
    kP_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kP_0: 13>
    kP_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kP_1: 21>
    kP_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kP_2: 29>
    kP_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kP_3: 37>
    kPolePairs: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kPolePairs: 10>
    kPositionConversionFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kPositionConversionFactor: 112>
    kPositionPIDMaxInput: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kPositionPIDMaxInput: 151>
    kPositionPIDMinInput: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kPositionPIDMinInput: 150>
    kPositionPIDWrapEnable: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kPositionPIDWrapEnable: 149>
    kProductId: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kProductId: 155>
    kRampRate: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kRampRate: 56>
    kSensorType: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSensorType: 4>
    kSerialNumberHigh: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSerialNumberHigh: 49>
    kSerialNumberLow: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSerialNumberLow: 47>
    kSerialNumberMid: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSerialNumberMid: 48>
    kSlot3Placeholder1_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder1_0: 97>
    kSlot3Placeholder1_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder1_1: 101>
    kSlot3Placeholder1_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder1_2: 105>
    kSlot3Placeholder1_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder1_3: 109>
    kSlot3Placeholder2_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder2_0: 98>
    kSlot3Placeholder2_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder2_1: 102>
    kSlot3Placeholder2_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder2_2: 106>
    kSlot3Placeholder2_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder2_3: 110>
    kSlot3Placeholder3_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder3_0: 99>
    kSlot3Placeholder3_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder3_1: 103>
    kSlot3Placeholder3_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder3_2: 107>
    kSlot3Placeholder3_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSlot3Placeholder3_3: 111>
    kSmartCurrentConfig: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartCurrentConfig: 61>
    kSmartCurrentFreeLimit: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartCurrentFreeLimit: 60>
    kSmartCurrentReserved: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartCurrentReserved: 62>
    kSmartCurrentStallLimit: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartCurrentStallLimit: 59>
    kSmartMotionAccelStrategy_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAccelStrategy_0: 80>
    kSmartMotionAccelStrategy_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAccelStrategy_1: 85>
    kSmartMotionAccelStrategy_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAccelStrategy_2: 90>
    kSmartMotionAccelStrategy_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAccelStrategy_3: 95>
    kSmartMotionAllowedClosedLoopError_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAllowedClosedLoopError_0: 79>
    kSmartMotionAllowedClosedLoopError_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAllowedClosedLoopError_1: 84>
    kSmartMotionAllowedClosedLoopError_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAllowedClosedLoopError_2: 89>
    kSmartMotionAllowedClosedLoopError_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionAllowedClosedLoopError_3: 94>
    kSmartMotionMaxAccel_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxAccel_0: 77>
    kSmartMotionMaxAccel_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxAccel_1: 82>
    kSmartMotionMaxAccel_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxAccel_2: 87>
    kSmartMotionMaxAccel_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxAccel_3: 92>
    kSmartMotionMaxVelocity_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxVelocity_0: 76>
    kSmartMotionMaxVelocity_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxVelocity_1: 81>
    kSmartMotionMaxVelocity_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxVelocity_2: 86>
    kSmartMotionMaxVelocity_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMaxVelocity_3: 91>
    kSmartMotionMinVelOutput_0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMinVelOutput_0: 78>
    kSmartMotionMinVelOutput_1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMinVelOutput_1: 83>
    kSmartMotionMinVelOutput_2: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMinVelOutput_2: 88>
    kSmartMotionMinVelOutput_3: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSmartMotionMinVelOutput_3: 93>
    kSoftLimitFwd: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitFwd: 115>
    kSoftLimitFwdEn: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitFwdEn: 54>
    kSoftLimitRev: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitRev: 116>
    kSoftLimitRevEn: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitRevEn: 55>
    kSoftLimitRsvd0: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitRsvd0: 117>
    kSoftLimitRsvd1: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kSoftLimitRsvd1: 118>
    kStatus0Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus0Period: 158>
    kStatus1Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus1Period: 159>
    kStatus2Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus2Period: 160>
    kStatus3Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus3Period: 161>
    kStatus4Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus4Period: 162>
    kStatus5Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus5Period: 163>
    kStatus6Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus6Period: 164>
    kStatus7Period: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kStatus7Period: 165>
    kVelocityConversionFactor: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kVelocityConversionFactor: 113>
    kVoltageCompMode: typing.ClassVar[SparkParameter]  # value = <SparkParameter.kVoltageCompMode: 74>
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
class SparkRelativeEncoder(RelativeEncoder):
    """
    Get an instance of this class by using SparkBase::GetEncoder() or
    SparkBase::GetEncoder(SparkRelativeEncoder::Type, int).
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getPosition(self) -> float:
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().
        
        :returns: Number of rotations of the motor
        """
    def getVelocity(self) -> float:
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().
        
        :returns: Number the RPM of the motor
        """
    def setPosition(self, position: float) -> REVLibError:
        """
        Set the position of the encoder.
        
        :param position: Number of rotations of the motor
        
        :returns: REVLibError::kOk if successful
        """
class SparkRelativeEncoderSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, motor: SparkMax) -> None:
        ...
    @typing.overload
    def __init__(self, motor: SparkFlex) -> None:
        ...
    def getInverted(self) -> bool:
        ...
    def getPosition(self) -> float:
        ...
    def getPositionConversionFactor(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def getVelocityConversionFactor(self) -> float:
        ...
    def getZeroOffset(self) -> float:
        ...
    def iterate(self, velocity: float, dt: float) -> None:
        ...
    def setInverted(self, inverted: bool) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setPositionConversionFactor(self, positionConversionFactor: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def setVelocityConversionFactor(self, velocityConversionFactor: float) -> None:
        ...
    def setZeroOffset(self, zeroOffset: float) -> None:
        ...
class SparkSim:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, spark: SparkBase, motor: wpimath._controls._controls.plant.DCMotor) -> None:
        ...
    def disable(self) -> None:
        ...
    def enable(self) -> None:
        ...
    def getAbsoluteEncoderSim(self) -> SparkAbsoluteEncoderSim:
        ...
    def getAnalogSensorSim(self) -> SparkAnalogSensorSim:
        ...
    def getAppliedOutput(self) -> float:
        ...
    def getBusVoltage(self) -> float:
        ...
    def getClosedLoopSlot(self) -> ClosedLoopSlot:
        ...
    def getFaultManager(self) -> SparkSimFaultManager:
        ...
    def getForwardLimitSwitchSim(self) -> SparkLimitSwitchSim:
        ...
    def getMotorCurrent(self) -> float:
        ...
    def getPosition(self) -> float:
        ...
    def getRelativeEncoderSim(self) -> SparkRelativeEncoderSim:
        ...
    def getReverseLimitSwitchSim(self) -> SparkLimitSwitchSim:
        ...
    def getSetpoint(self) -> float:
        ...
    def getVelocity(self) -> float:
        ...
    def iterate(self, velocity: float, vbus: float, dt: float) -> None:
        ...
    def setAppliedOutput(self, appliedOutput: float) -> None:
        ...
    def setBusVoltage(self, voltage: float) -> None:
        ...
    def setMotorCurrent(self, current: float) -> None:
        ...
    def setPosition(self, position: float) -> None:
        ...
    def setVelocity(self, velocity: float) -> None:
        ...
    def useDriverStationEnable(self) -> None:
        ...
class SparkSimFaultManager:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, motor: SparkMax) -> None:
        ...
    @typing.overload
    def __init__(self, motor: SparkFlex) -> None:
        ...
    def setFaults(self, faults: SparkBase.Faults) -> None:
        ...
    def setStickyFaults(self, faults: SparkBase.Faults) -> None:
        ...
    def setStickyWarnings(self, warnings: SparkBase.Warnings) -> None:
        ...
    def setWarnings(self, warnings: SparkBase.Warnings) -> None:
        ...
