import logging

"""Fake cover Entity for Home Assistant."""

from homeassistant.components.cover import (
  CoverEntity,
  SUPPORT_OPEN,
  SUPPORT_CLOSE,
  SUPPORT_STOP,
  SUPPORT_SET_POSITION,
  SUPPORT_SET_TILT_POSITION,
)

_LOGGER = logging.getLogger(__name__)

class FakeCoverEntity(CoverEntity):
  """Representation of a fake cover entity."""

  def __init__(self, name):
    """Initialize the cover entity."""
    self._name = name
    self._is_open = False
    self._current_position = 0
    self._current_tilt_position = 0

  @property
  def name(self):
    """Return the name of the cover entity."""
    return self._name

  @property
  def is_opening(self):
    """Return if the cover is opening or not."""
    return False

  @property
  def is_closing(self):
    """Return if the cover is closing or not."""
    return False

  @property
  def is_closed(self):
    """Return if the cover is closed or not."""
    return not self._is_open

  @property
  def current_cover_position(self):
    """Return the current position of the cover."""
    return self._current_position

  @property
  def current_cover_tilt_position(self):
    """Return the current tilt position of the cover."""
    return self._current_tilt_position

  @property
  def supported_features(self):
    """Flag supported features."""
    return (
      SUPPORT_OPEN
      | SUPPORT_CLOSE
      | SUPPORT_STOP
      | SUPPORT_SET_POSITION
      | SUPPORT_SET_TILT_POSITION
    )

  def open_cover(self, **kwargs):
    """Open the cover."""
    self._is_open = True
    self._current_position = 100
    self.schedule_update_ha_state()

  def close_cover(self, **kwargs):
    """Close the cover."""
    self._is_open = False
    self._current_position = 0
    self.schedule_update_ha_state()

  def stop_cover(self, **kwargs):
    """Stop the cover."""
    self.schedule_update_ha_state()

  def set_cover_position(self, position, **kwargs):
    """Set the cover position."""
    self._current_position = position
    self.schedule_update_ha_state()

  def set_cover_tilt_position(self, tilt_position, **kwargs):
    """Set the cover tilt position."""
    self._current_tilt_position = tilt_position
    self.schedule_update_ha_state()
async def async_setup_entry(hass, entry, async_add_entities):
  """Set up the Fake Cover Entity."""
  async_add_entities([FakeCoverEntity("Fake Cover")])
  return True