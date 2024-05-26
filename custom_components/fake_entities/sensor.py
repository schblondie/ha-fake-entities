import logging

"""Fake sensor Entity for Home Assistant."""

from homeassistant.components.sensor import (
  DEVICE_CLASS_HUMIDITY,
  DEVICE_CLASS_TEMPERATURE,
  STATE_CLASS_MEASUREMENT,
  SensorEntity,
)

_LOGGER = logging.getLogger(__name__)

class FakesensorEntity(SensorEntity):
  """Representation of a fake sensor entity."""

  def __init__(self, name):
    """Initialize the sensor entity."""
    self._name = name
    self._state = None

  @property
  def name(self):
    """Return the name of the sensor entity."""
    return self._name

  @property
  def state(self):
    """Return the state of the sensor entity."""
    return self._state

  @property
  def unit_of_measurement(self):
    """Return the unit of measurement of the sensor entity."""
    return "°C"

  @property
  def device_class(self):
    """Return the device class of the sensor entity."""
    return DEVICE_CLASS_TEMPERATURE

  @property
  def state_class(self):
    """Return the state class of the sensor entity."""
    return STATE_CLASS_MEASUREMENT

  @property
  def device_info(self):
    """Return device information for the sensor entity."""
    return {
      "identifiers": {(DOMAIN, self.unique_id)},
      "name": self.name,
      "manufacturer": "Fake Manufacturer",
      "model": "Fake Model",
      "sw_version": "1.0",
    }

  @property
  def extra_state_attributes(self):
    """Return the extra state attributes of the sensor entity."""
    return {"attribute1": "value1", "attribute2": "value2"}

  async def async_update(self):
    """Update the state of the sensor entity."""
    # Add your update logic here
    self._state = 25.0
async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake sensor entry."""
  async_add_entities([FakesensorEntity("Fake Temperature Sensor")])
  return True