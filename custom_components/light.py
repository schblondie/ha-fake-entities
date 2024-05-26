import logging

"""Fake light Entity for Home Assistant."""

from homeassistant.components.light import (
  ATTR_BRIGHTNESS,
  ATTR_COLOR_TEMP,
  ATTR_EFFECT,
  ATTR_HS_COLOR,
  ATTR_RGB_COLOR,
  ATTR_TRANSITION,
  ATTR_WHITE_VALUE,
  SUPPORT_BRIGHTNESS,
  SUPPORT_COLOR,
  SUPPORT_COLOR_TEMP,
  SUPPORT_EFFECT,
  SUPPORT_TRANSITION,
  SUPPORT_WHITE_VALUE,
  LightEntity,
)

_LOGGER = logging.getLogger(__name__)

class FakelightEntity(LightEntity):
  """Representation of a fake light entity."""

  def __init__(self, name):
    """Initialize the light entity."""
    self._name = name
    self._state = False
    self._brightness = 255
    self._color_temp = 300
    self._hs_color = (0, 0)
    self._rgb_color = (255, 255, 255)
    self._effect = "None"
    self._white_value = 255
    self._supported_features = (
      SUPPORT_BRIGHTNESS
      | SUPPORT_COLOR_TEMP
      | SUPPORT_COLOR
      | SUPPORT_EFFECT
      | SUPPORT_TRANSITION
      | SUPPORT_WHITE_VALUE
    )

  @property
  def name(self):
    """Return the name of the light entity."""
    return self._name

  @property
  def is_on(self):
    """Return true if the light is on."""
    return self._state

  @property
  def brightness(self):
    """Return the brightness of the light."""
    return self._brightness

  @property
  def color_temp(self):
    """Return the color temperature of the light."""
    return self._color_temp

  @property
  def hs_color(self):
    """Return the HS color value of the light."""
    return self._hs_color

  @property
  def rgb_color(self):
    """Return the RGB color value of the light."""
    return self._rgb_color

  @property
  def effect(self):
    """Return the current effect of the light."""
    return self._effect

  @property
  def white_value(self):
    """Return the white value of the light."""
    return self._white_value

  @property
  def supported_features(self):
    """Return the supported features of the light."""
    return self._supported_features

  def turn_on(self, **kwargs):
    """Turn the light on."""
    self._state = True

    if ATTR_BRIGHTNESS in kwargs:
      self._brightness = kwargs[ATTR_BRIGHTNESS]

    if ATTR_COLOR_TEMP in kwargs:
      self._color_temp = kwargs[ATTR_COLOR_TEMP]

    if ATTR_HS_COLOR in kwargs:
      self._hs_color = kwargs[ATTR_HS_COLOR]

    if ATTR_RGB_COLOR in kwargs:
      self._rgb_color = kwargs[ATTR_RGB_COLOR]

    if ATTR_EFFECT in kwargs:
      self._effect = kwargs[ATTR_EFFECT]

    if ATTR_WHITE_VALUE in kwargs:
      self._white_value = kwargs[ATTR_WHITE_VALUE]

  def turn_off(self, **kwargs):
    """Turn the light off."""
    self._state = False

  # Add more methods and properties here
