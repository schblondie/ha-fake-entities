import logging
from homeassistant.components.camera import (
  Camera,
  CameraEntityFeature,
)

_LOGGER = logging.getLogger(__name__)

class FakeCameraEntity(Camera):
  """Representation of a fake camera entity."""

  def __init__(self, name):
    """Initialize the camera entity."""
    self._name = name
    self._brand = None
    self._frame_interval = 0.5
    self._frontend_stream_type = None
    self._is_on = True
    self._is_recording = False
    self._is_streaming = False
    self._model = None
    self._motion_detection_enabled = False
    self._use_stream_for_stills = False
    self._volume_level = 0.5
    self._selected_stream = "main"
    self._selected_record_mode = "continuous"
    self._selected_snapshot_resolution = "high"
    self._selected_playback_speed = "normal"

  @property
  def brand(self):
    """Return the brand of the camera entity."""
    return self._brand

  @property
  def frame_interval(self):
    """Return the frame interval of the camera entity."""
    return self._frame_interval

  @property
  def frontend_stream_type(self):
    """Return the frontend stream type of the camera entity."""
    return self._frontend_stream_type

  @property
  def is_on(self):
    """Return the on state of the camera entity."""
    return self._is_on

  @property
  def model(self):
    """Return the model of the camera entity."""
    return self._model

  @property
  def motion_detection_enabled(self):
    """Return the motion detection state of the camera entity."""
    return self._motion_detection_enabled

  @property
  def use_stream_for_stills(self):
    """Return the use stream for stills state of the camera entity."""
    return self._use_stream_for_stills

  async def async_turn_on(self):
    """Turn on the camera entity."""
    _LOGGER.info("Turning on the camera")
    self._is_on = True

  async def async_turn_off(self):
    """Turn off the camera entity."""
    _LOGGER.info("Turning off the camera")
    self._is_on = False

  async def async_enable_motion_detection(self):
    """Enable motion detection in the camera."""
    _LOGGER.info("Enabling motion detection")
    self._motion_detection_enabled = True

  async def async_disable_motion_detection(self):
    """Disable motion detection in the camera."""
    _LOGGER.info("Disabling motion detection")
    self._motion_detection_enabled = False

  async def async_handle_web_rtc_offer(self, offer_sdp: str) -> str | None:
    """Handle the WebRTC offer and return an answer."""
    return None

  @property
  def name(self):
    """Return the name of the camera entity."""
    return self._name

  @property
  def supported_features(self):
    """Return the supported features of the camera entity."""
    return (
        CameraEntityFeature.ON_OFF
        | CameraEntityFeature.STREAM
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

  async def async_camera_image(self):
    """Return bytes of camera image."""
    return None

  async def stream_source(self):
    """Return the source of the stream."""
    return None

async def async_setup_entry(hass, config_entry, async_add_entities):
  """Set up the fake camera entry."""
  async_add_entities([FakeCameraEntity("Fake Camera")])
  return True