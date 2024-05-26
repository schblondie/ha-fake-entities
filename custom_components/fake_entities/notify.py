import logging

"""Fake notify Entity for Home Assistant."""

from homeassistant.components.notify import (
  ATTR_DATA,
  ATTR_MESSAGE,
  ATTR_TARGET,
  ATTR_TITLE,
  ATTR_TITLE_DEFAULT,
  PLATFORM_SCHEMA,
  BaseNotificationService,
)

_LOGGER = logging.getLogger(__name__)

class FakenotifyEntity(BaseNotificationService):
  """Representation of a fake notify entity."""

  def __init__(self, name):
    """Initialize the notify entity."""
    self._name = name

  @property
  def name(self):
    """Return the name of the notify entity."""
    return self._name

  def send_message(self, message="", **kwargs):
    """Send a message."""
    data = kwargs.get(ATTR_DATA)
    target = kwargs.get(ATTR_TARGET)
    title = kwargs.get(ATTR_TITLE, ATTR_TITLE_DEFAULT)

    _LOGGER.info("Sending message: %s", message)
    _LOGGER.info("Data: %s", data)
    _LOGGER.info("Target: %s", target)
    _LOGGER.info("Title: %s", title)

async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake notify entry."""
  async_add_entities([FakenotifyEntity("Fake Notify")])
  return True