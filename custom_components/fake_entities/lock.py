import logging

"""Fake lock Entity for Home Assistant."""

from homeassistant.components.lock import (
  LockEntity,
  SUPPORT_OPEN,
  SUPPORT_CLOSE,
  SUPPORT_LOCK,
  SUPPORT_UNLOCK,
  SUPPORT_OPEN_TILT,
  SUPPORT_CLOSE_TILT,
  SUPPORT_STOP,
  SUPPORT_SET_CODE,
  SUPPORT_CLEAR_CODE,
  SUPPORT_ALARM,
  SUPPORT_BATTERY,
  SUPPORT_STATUS,
)

_LOGGER = logging.getLogger(__name__)

class FakelockEntity(LockEntity):
  """Representation of a fake lock entity."""

  def __init__(self, name):
    """Initialize the lock entity."""
    self._name = name
    self._is_locked = False
    self._is_open = False
    self._is_tilt_open = False
    self._code = None
    self._alarm = None
    self._battery_level = None

  @property
  def name(self):
    """Return the name of the lock entity."""
    return self._name

  @property
  def is_locked(self):
    """Return true if the lock is locked."""
    return self._is_locked

  @property
  def is_open(self):
    """Return true if the lock is open."""
    return self._is_open

  @property
  def is_tilt_open(self):
    """Return true if the lock tilt is open."""
    return self._is_tilt_open

  @property
  def code_format(self):
    """Return the required code format for the lock."""
    return "^\\d{4}$"

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_OPEN
      | SUPPORT_CLOSE
      | SUPPORT_LOCK
      | SUPPORT_UNLOCK
      | SUPPORT_OPEN_TILT
      | SUPPORT_CLOSE_TILT
      | SUPPORT_STOP
      | SUPPORT_SET_CODE
      | SUPPORT_CLEAR_CODE
      | SUPPORT_ALARM
      | SUPPORT_BATTERY
      | SUPPORT_STATUS
    )

  def lock(self, **kwargs):
    """Lock the lock."""
    self._is_locked = True

  def unlock(self, **kwargs):
    """Unlock the lock."""
    self._is_locked = False

  def open(self, **kwargs):
    """Open the lock."""
    self._is_open = True

  def close(self, **kwargs):
    """Close the lock."""
    self._is_open = False

  def open_tilt(self, **kwargs):
    """Open the lock tilt."""
    self._is_tilt_open = True

  def close_tilt(self, **kwargs):
    """Close the lock tilt."""
    self._is_tilt_open = False

  def stop(self, **kwargs):
    """Stop the lock."""
    pass

  def set_code(self, code, **kwargs):
    """Set the lock code."""
    self._code = code

  def clear_code(self, **kwargs):
    """Clear the lock code."""
    self._code = None

  @property
  def code(self):
    """Return the lock code."""
    return self._code

  @property
  def alarm(self):
    """Return the lock alarm status."""
    return self._alarm

  @property
  def battery_level(self):
    """Return the lock battery level."""
    return self._battery_level

  @property
  def device_state_attributes(self):
    """Return the lock attributes."""
    return {
      "battery_level": self._battery_level,
      "alarm": self._alarm,
    }
async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake lock entry."""
  async_add_entities([FakelockEntity("Fake Lock")])
  return True