import logging
from homeassistant.components.switch import SwitchEntity

"""Fake switch Entity for Home Assistant."""


_LOGGER = logging.getLogger(__name__)

class FakeswitchEntity(SwitchEntity):
  """Representation of a fake switch entity."""

  def __init__(self, name):
    """Initialize the switch entity."""
    self._name = name
    self._state = False

  @property
  def name(self):
    """Return the name of the switch entity."""
    return self._name

  @property
  def is_on(self):
    """Return true if the switch is on."""
    return self._state

  def turn_on(self, **kwargs):
    """Turn the switch on."""
    self._state = True
    self.schedule_update_ha_state()

  def turn_off(self, **kwargs):
    """Turn the switch off."""
    self._state = False
    self.schedule_update_ha_state()

  def toggle(self, **kwargs):
    """Toggle the switch state."""
    self._state = not self._state
    self.schedule_update_ha_state()

  @property
  def device_state_attributes(self):
    """Return the state attributes."""
    return {
      "friendly_name": self._name,
      "custom_attribute": "example",
    }

  @property
  def icon(self):
    """Return the icon to be used for this entity."""
    return "mdi:lightbulb"

  @property
  def supported_features(self):
    """Flag supported features."""
    return 0

  # Add more methods and properties here
