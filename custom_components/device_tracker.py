from homeassistant.components.device_tracker import (
  SOURCE_TYPE_GPS,
  DeviceTrackerEntity
)
from homeassistant.const import STATE_HOME, STATE_NOT_HOME

class Fakedevice_trackerEntity(DeviceTrackerEntity):
  """Representation of a fake device_tracker entity."""

  def __init__(self, name):
    """Initialize the device_tracker entity."""
    self._name = name
    self._state = STATE_HOME
    self._latitude = 0.0
    self._longitude = 0.0
    self._source_type = SOURCE_TYPE_GPS
    self._battery = 100
    self._gps_accuracy = 0
    self._attributes = {}

  @property
  def name(self):
    """Return the name of the device_tracker entity."""
    return self._name

  @property
  def state(self):
    """Return the state of the entity."""
    return self._state

  @property
  def latitude(self):
    """Return the latitude of the entity."""
    return self._latitude

  @property
  def longitude(self):
    """Return the longitude of the entity."""
    return self._longitude

  @property
  def source_type(self):
    """Return the source type of the entity."""
    return self._source_type

  @property
  def battery_level(self):
    """Return the battery level of the entity."""
    return self._battery

  @property
  def gps_accuracy(self):
    """Return the GPS accuracy of the entity."""
    return self._gps_accuracy

  @property
  def device_state_attributes(self):
    """Return the state attributes of the entity."""
    return self._attributes