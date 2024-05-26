import logging

"""Fake alarm_control_panel Entity for Home Assistant."""

from homeassistant.components.alarm_control_panel import (
  AlarmControlPanelEntity,
  SUPPORT_ALARM_ARM_AWAY,
  SUPPORT_ALARM_ARM_HOME,
  SUPPORT_ALARM_ARM_NIGHT,
  SUPPORT_ALARM_TRIGGER,
  SUPPORT_ALARM_DISARM,
)

_LOGGER = logging.getLogger(__name__)

class FakeAlarmControlPanelEntity(AlarmControlPanelEntity):
  """Representation of a fake alarm_control_panel entity."""

  def __init__(self, name):
    """Initialize the alarm_control_panel entity."""
    self._name = name
    self._state = "disarmed"

  @property
  def name(self):
    """Return the name of the alarm_control_panel entity."""
    return self._name

  @property
  def state(self):
    """Return the state of the alarm_control_panel entity."""
    return self._state

  @property
  def supported_features(self):
    """Return the list of supported features."""
    return (
      SUPPORT_ALARM_ARM_AWAY
      | SUPPORT_ALARM_ARM_HOME
      | SUPPORT_ALARM_ARM_NIGHT
      | SUPPORT_ALARM_TRIGGER
      | SUPPORT_ALARM_DISARM
    )

  def alarm_arm_away(self, code=None):
    """Arm the alarm in away mode."""
    _LOGGER.info("Arming the alarm in away mode")
    # Add your code here to arm the alarm in away mode

  def alarm_arm_home(self, code=None):
    """Arm the alarm in home mode."""
    _LOGGER.info("Arming the alarm in home mode")
    # Add your code here to arm the alarm in home mode

  def alarm_arm_night(self, code=None):
    """Arm the alarm in night mode."""
    _LOGGER.info("Arming the alarm in night mode")
    # Add your code here to arm the alarm in night mode

  def alarm_trigger(self, code=None):
    """Trigger the alarm."""
    _LOGGER.info("Triggering the alarm")
    # Add your code here to trigger the alarm

  def alarm_disarm(self, code=None):
    """Disarm the alarm."""
    _LOGGER.info("Disarming the alarm")
    # Add your code here to disarm the alarm

  # Add more methods and properties here