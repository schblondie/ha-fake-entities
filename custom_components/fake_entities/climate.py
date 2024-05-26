import logging

"""Fake climate Entity for Home Assistant."""

from homeassistant.components.climate import (
  ClimateEntity,
  ClimateEntityFeature,
)

class FakeclimateEntity(ClimateEntity):
  """Representation of a fake climate entity."""

  def __init__(self, name):
    """Initialize the climate entity."""
    self._name = name
    self._target_temperature = None
    self._current_temperature = None
    self._target_humidity = None
    self._current_humidity = None
    self._preset_mode = None
    self._fan_mode = None
    self._swing_mode = None
    self._aux_heat = None
    self._is_on = None
    self._operation_mode = None
    self._hold_mode = None
    self._away_mode = None
    self._target_temperature_range = None
    self._target_humidity_range = None

  @property
  def name(self):
    """Return the name of the climate entity."""
    return self._name

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE
      | ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.SUPPORT_TARGET_HUMIDITY
      | ClimateEntityFeature.SUPPORT_FAN_MODE
      | ClimateEntityFeature.SUPPORT_PRESET_MODE
      | ClimateEntityFeature.SUPPORT_SWING_MODE
      | ClimateEntityFeature.SUPPORT_TURN_ON
      | ClimateEntityFeature.SUPPORT_TURN_OFF
    )

  @property
  def target_temperature(self):
    """Return the target temperature."""
    return self._target_temperature

  @property
  def current_temperature(self):
    """Return the current temperature."""
    return self._current_temperature

  @property
  def target_humidity(self):
    """Return the target humidity."""
    return self._target_humidity

  @property
  def current_humidity(self):
    """Return the current humidity."""
    return self._current_humidity

  @property
  def preset_mode(self):
    """Return the preset mode."""
    return self._preset_mode

  @property
  def fan_mode(self):
    """Return the fan mode."""
    return self._fan_mode

  @property
  def swing_mode(self):
    """Return the swing mode."""
    return self._swing_mode

  @property
  def aux_heat(self):
    """Return the aux heat."""
    return self._aux_heat

  @property
  def is_on(self):
    """Return True if the entity is on."""
    return self._is_on

  @property
  def operation_mode(self):
    """Return the operation mode."""
    return self._operation_mode

  @property
  def hold_mode(self):
    """Return the hold mode."""
    return self._hold_mode

  @property
  def away_mode(self):
    """Return the away mode."""
    return self._away_mode

  @property
  def target_temperature_range(self):
    """Return the target temperature range."""
    return self._target_temperature_range

  @property
  def target_humidity_range(self):
    """Return the target humidity range."""
    return self._target_humidity_range

  def set_temperature(self, **kwargs):
    """Set the target temperature."""
    if "temperature" in kwargs:
      self._target_temperature = kwargs["temperature"]

  def set_humidity(self, **kwargs):
    """Set the target humidity."""
    if "humidity" in kwargs:
      self._target_humidity = kwargs["humidity"]

  def set_preset_mode(self, preset_mode):
    """Set the preset mode."""
    self._preset_mode = preset_mode

  def set_fan_mode(self, fan_mode):
    """Set the fan mode."""
    self._fan_mode = fan_mode

  def set_swing_mode(self, swing_mode):
    """Set the swing mode."""
    self._swing_mode = swing_mode

  def set_aux_heat(self, aux_heat):
    """Set the aux heat."""
    self._aux_heat = aux_heat

  def turn_on(self):
    """Turn on the entity."""
    self._is_on = True

  def turn_off(self):
    """Turn off the entity."""
    self._is_on = False

  def set_operation_mode(self, operation_mode):
    """Set the operation mode."""
    self._operation_mode = operation_mode

  def set_hold_mode(self, hold_mode):
    """Set the hold mode."""
    self._hold_mode = hold_mode

  def set_away_mode(self, away_mode):
    """Set the away mode."""
    self._away_mode = away_mode

  def set_target_temperature_range(self, target_temperature_range):
    """Set the target temperature range."""
    self._target_temperature_range = target_temperature_range

  def set_target_humidity_range(self, target_humidity_range):
    """Set the target humidity range."""
    self._target_humidity_range = target_humidity_range
class FakeHeaterEntity(FakeclimateEntity):
  """Representation of a fake heater entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE
      | ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.SUPPORT_TURN_ON
      | ClimateEntityFeature.SUPPORT_TURN_OFF
    )

class FakeFanEntity(FakeclimateEntity):
  """Representation of a fake fan entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.SUPPORT_FAN_MODE
      | ClimateEntityFeature.SUPPORT_SWING_MODE
      | ClimateEntityFeature.SUPPORT_TURN_ON
      | ClimateEntityFeature.SUPPORT_TURN_OFF
    )

class FakeACEntity(FakeclimateEntity):
  """Representation of a fake AC entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE
      | ClimateEntityFeature.SUPPORT_TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.SUPPORT_FAN_MODE
      | ClimateEntityFeature.SUPPORT_TURN_ON
      | ClimateEntityFeature.SUPPORT_TURN_OFF
    )

async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake climate entry."""
  async_add_entities([
    FakeclimateEntity("Fake Climate"),
    FakeHeaterEntity("Fake Heater"),
    FakeFanEntity("Fake Fan"),
    FakeACEntity("Fake AC"),
  ])
  return True