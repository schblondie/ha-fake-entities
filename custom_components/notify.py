import logging

"""Fake notify Entity for Home Assistant."""

from homeassistant.components.notify import (
  ATTR_DATA,
  ATTR_MESSAGE,
  ATTR_TARGET,
  ATTR_TITLE,
  ATTR_TITLE_DEFAULT,
  ATTR_TITLE_ICON,
  ATTR_TITLE_COLOR,
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
    title_icon = kwargs.get(ATTR_TITLE_ICON)
    title_color = kwargs.get(ATTR_TITLE_COLOR)

    _LOGGER.info("Sending message: %s", message)
    _LOGGER.info("Data: %s", data)
    _LOGGER.info("Target: %s", target)
    _LOGGER.info("Title: %s", title)
    _LOGGER.info("Title Icon: %s", title_icon)
    _LOGGER.info("Title Color: %s", title_color)

  # Add more methods and properties here
