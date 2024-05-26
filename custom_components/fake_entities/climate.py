class FakeHeaterEntity(FakeclimateEntity):
  """Representation of a fake heater entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_TARGET_TEMPERATURE
      | SUPPORT_ON_OFF
      | SUPPORT_AUX_HEAT
    )

class FakeFanEntity(FakeclimateEntity):
  """Representation of a fake fan entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_ON_OFF
      | SUPPORT_FAN_MODE
    )

class FakeACEntity(FakeclimateEntity):
  """Representation of a fake AC entity."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_TARGET_TEMPERATURE
      | SUPPORT_ON_OFF
      | SUPPORT_FAN_MODE
    )

class UltimateClimateEntity(FakeclimateEntity):
  """Representation of an ultimate climate entity that supports all features."""

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_TARGET_TEMPERATURE
      | SUPPORT_TARGET_HUMIDITY
      | SUPPORT_TARGET_HUMIDITY_HIGH
      | SUPPORT_TARGET_HUMIDITY_LOW
      | SUPPORT_PRESET_MODE
      | SUPPORT_FAN_MODE
      | SUPPORT_SWING_MODE
      | SUPPORT_AUX_HEAT
      | SUPPORT_ON_OFF
      | SUPPORT_OPERATION_MODE
      | SUPPORT_HOLD_MODE
      | SUPPORT_AWAY_MODE
      | SUPPORT_TARGET_TEMPERATURE_RANGE
      | SUPPORT_TARGET_HUMIDITY_RANGE
      | SUPPORT_TARGET_HUMIDITY_STEP
      | SUPPORT_TARGET_TEMPERATURE_STEP
      | SUPPORT_TARGET_TEMPERATURE_HIGH
      | SUPPORT_TARGET_TEMPERATURE_LOW
      | SUPPORT_TARGET_TEMPERATURE_PRECISION
      | SUPPORT_TARGET_HUMIDITY_PRECISION
      | SUPPORT_FAN_MODE_PRESET
      | SUPPORT_SWING_MODE_PRESET
      | SUPPORT_OPERATION_MODE_PRESET
      | SUPPORT_HOLD_MODE_PRESET
      | SUPPORT_AWAY_MODE_PRESET
      | SUPPORT_AUX_HEAT_PRESET
    )

async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake climate entry."""
  async_add_entities([
    FakeHeaterEntity("Fake Heater"),
    FakeFanEntity("Fake Fan"),
    FakeACEntity("Fake AC"),
    UltimateClimateEntity("Ultimate Climate"),
  ])
  return True