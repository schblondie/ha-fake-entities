import logging

"""Fake camera Entity for Home Assistant."""

from homeassistant.components.camera import (
  CameraEntity,
  SUPPORT_ON_OFF,
  SUPPORT_STREAM,
  SUPPORT_RECORD,
  SUPPORT_SNAPSHOT,
  SUPPORT_PLAY,
  SUPPORT_PAUSE,
  SUPPORT_STOP,
  SUPPORT_VOLUME_SET,
  SUPPORT_VOLUME_MUTE,
  SUPPORT_AUDIO,
  SUPPORT_SELECT_STREAM,
  SUPPORT_SELECT_RECORD_MODE,
  SUPPORT_SELECT_SNAPSHOT_RESOLUTION,
  SUPPORT_SELECT_PLAYBACK_SPEED,
)

_LOGGER = logging.getLogger(__name__)

class FakeCameraEntity(CameraEntity):
  """Representation of a fake camera entity."""

  def __init__(self, name):
    """Initialize the camera entity."""
    self._name = name
    self._is_recording = False
    self._is_streaming = False
    self._is_muted = False
    self._volume_level = 0.5
    self._selected_stream = "main"
    self._selected_record_mode = "continuous"
    self._selected_snapshot_resolution = "high"
    self._selected_playback_speed = "normal"

  @property
  def name(self):
    """Return the name of the camera entity."""
    return self._name

  @property
  def supported_features(self):
    """Return the supported features of the camera entity."""
    return (
      SUPPORT_ON_OFF
      | SUPPORT_STREAM
      | SUPPORT_RECORD
      | SUPPORT_SNAPSHOT
      | SUPPORT_PLAY
      | SUPPORT_PAUSE
      | SUPPORT_STOP
      | SUPPORT_VOLUME_SET
      | SUPPORT_VOLUME_MUTE
      | SUPPORT_AUDIO
      | SUPPORT_SELECT_STREAM
      | SUPPORT_SELECT_RECORD_MODE
      | SUPPORT_SELECT_SNAPSHOT_RESOLUTION
      | SUPPORT_SELECT_PLAYBACK_SPEED
    )

  @property
  def is_recording(self):
    """Return the recording state of the camera entity."""
    return self._is_recording

  @property
  def is_streaming(self):
    """Return the streaming state of the camera entity."""
    return self._is_streaming

  @property
  def is_muted(self):
    """Return the mute state of the camera entity."""
    return self._is_muted

  @property
  def volume_level(self):
    """Return the volume level of the camera entity."""
    return self._volume_level

  @property
  def selected_stream(self):
    """Return the selected stream of the camera entity."""
    return self._selected_stream

  @property
  def selected_record_mode(self):
    """Return the selected record mode of the camera entity."""
    return self._selected_record_mode

  @property
  def selected_snapshot_resolution(self):
    """Return the selected snapshot resolution of the camera entity."""
    return self._selected_snapshot_resolution

  @property
  def selected_playback_speed(self):
    """Return the selected playback speed of the camera entity."""
    return self._selected_playback_speed

  def turn_on(self):
    """Turn on the camera entity."""
    _LOGGER.info("Turning on the camera")

  def turn_off(self):
    """Turn off the camera entity."""
    _LOGGER.info("Turning off the camera")

  def stream(self):
    """Start streaming from the camera entity."""
    _LOGGER.info("Starting the camera stream")

  def record(self):
    """Start recording from the camera entity."""
    _LOGGER.info("Starting camera recording")
    self._is_recording = True

  def stop_recording(self):
    """Stop recording from the camera entity."""
    _LOGGER.info("Stopping camera recording")
    self._is_recording = False

  def snapshot(self):
    """Take a snapshot from the camera entity."""
    _LOGGER.info("Taking a camera snapshot")

  def play(self):
    """Start playing back from the camera entity."""
    _LOGGER.info("Starting camera playback")

  def pause(self):
    """Pause the camera entity playback."""
    _LOGGER.info("Pausing camera playback")

  def stop(self):
    """Stop the camera entity playback."""
    _LOGGER.info("Stopping camera playback")

  def set_volume_level(self, volume):
    """Set the volume level of the camera entity."""
    _LOGGER.info("Setting camera volume level to %s", volume)
    self._volume_level = volume

  def mute_volume(self):
    """Mute the volume of the camera entity."""
    _LOGGER.info("Muting camera volume")
    self._is_muted = True

  def unmute_volume(self):
    """Unmute the volume of the camera entity."""
    _LOGGER.info("Unmuting camera volume")
    self._is_muted = False

  def select_stream(self, stream):
    """Select a stream from the camera entity."""
    _LOGGER.info("Selecting camera stream: %s", stream)
    self._selected_stream = stream

  def select_record_mode(self, record_mode):
    """Select a record mode from the camera entity."""
    _LOGGER.info("Selecting camera record mode: %s", record_mode)
    self._selected_record_mode = record_mode

  def select_snapshot_resolution(self, resolution):
    """Select a snapshot resolution from the camera entity."""
    _LOGGER.info("Selecting camera snapshot resolution: %s", resolution)
    self._selected_snapshot_resolution = resolution

  def select_playback_speed(self, speed):
    """Select a playback speed from the camera entity."""
    _LOGGER.info("Selecting camera playback speed: %s", speed)
    self._selected_playback_speed = speed
