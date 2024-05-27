import logging

"""Fake climate Entity for Home Assistant."""

from homeassistant.components.climate import (
  ClimateEntity,
  ClimateEntityFeature,
  HVACMode,
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
    self._target_temperature_low = None
    self._target_temperature_high = None
    self._temperature_unit = '°C'
    self._hvac_mode = None

  @property
  def name(self):
    """Return the name of the climate entity."""
    return self._name

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.TARGET_TEMPERATURE
      | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.TARGET_HUMIDITY
      | ClimateEntityFeature.FAN_MODE
      | ClimateEntityFeature.PRESET_MODE
      | ClimateEntityFeature.SWING_MODE
      | ClimateEntityFeature.TURN_ON
      | ClimateEntityFeature.TURN_OFF
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
  def temperature_unit(self):
    """Return the unit of measurement used by the platform."""
    return self._temperature_unit

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
  def target_temperature_low(self):
    """Return the target temperature low."""
    return self._target_temperature_low
  
  @property
  def target_temperature_high(self):
    """Return the target temperature high."""
    return self._target_temperature_high

  @property
  def target_humidity_range(self):
    """Return the target humidity range."""
    return self._target_humidity_range

  @property
  def hvac_mode(self):
    """Return the current operation mode."""
    return self._hvac_mode

  @property
  def hvac_modes(self):
    """Return the list of available hvac operation modes."""
    return [HVACMode.OFF, HVACMode.HEAT, HVACMode.COOL, HVACMode.HEAT_COOL, HVACMode.AUTO, HVACMode.DRY, HVACMode.FAN_ONLY]
  
  @property
  def preset_modes(self):
    """Return the list of available preset operation modes."""
    return ["none", "eco", "away", "boost", "comfort", "home", "sleep", 'activity']
  
  @property
  def swing_modes(self):
    """Return the list of available swing operation modes."""
    return ["swing_off", "swing_on", "swing_vertical", "swing_horizontal", "swing_both"]
  
  @property
  def fan_modes(self):
    """Return the list of available fan operation modes."""
    return ["fan_on", "fan_off", "fan_auto", "fan_low", "fan_medium", "fan_high", "fan_middle", "fan_diffuse"]
  
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

  def set_target_temperature_low(self, target_temperature_low):
    """Set the target temperature low."""
    self._target_temperature_low = target_temperature_low
  
  def set_target_temperature_high(self, target_temperature_high):
    """Set the target temperature high."""
    self._target_temperature_high = target_temperature_high

  def set_target_humidity_range(self, target_humidity_range):
    """Set the target humidity range."""
    self._target_humidity_range = target_humidity_range
class FakeHeaterEntity(FakeclimateEntity):
  """Representation of a fake heater entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.TARGET_TEMPERATURE
      | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.TURN_ON
      | ClimateEntityFeature.TURN_OFF
    )

  @property
  def hvac_modes(self):
    """Return the list of available hvac operation modes."""
    return [HVACMode.OFF, HVACMode.HEAT]

class FakeFanEntity(FakeclimateEntity):
  """Representation of a fake fan entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.FAN_MODE
      | ClimateEntityFeature.SWING_MODE
      | ClimateEntityFeature.TURN_ON
      | ClimateEntityFeature.TURN_OFF
    )
  
  @property
  def hvac_modes(self):
    """Return the list of available hvac operation modes."""
    return [HVACMode.OFF, HVACMode.FAN_ONLY]

class FakeACEntity(FakeclimateEntity):
  """Representation of a fake AC entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      ClimateEntityFeature.TARGET_TEMPERATURE
      | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
      | ClimateEntityFeature.FAN_MODE
      | ClimateEntityFeature.TURN_ON
      | ClimateEntityFeature.TURN_OFF
    )
  
  @property
  def hvac_modes(self):
    """Return the list of available hvac operation modes."""
    return [HVACMode.OFF, HVACMode.COOL, HVACMode.FAN_ONLY]

async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake climate entry."""
  async_add_entities([
    FakeclimateEntity("Fake Climate"),
    FakeHeaterEntity("Fake Heater"),
    FakeFanEntity("Fake Fan"),
    FakeACEntity("Fake AC"),
  ])
  return True