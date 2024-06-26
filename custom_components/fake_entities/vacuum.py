import logging

from homeassistant.components.vacuum import (
    VacuumEntityFeature,
    StateVacuumEntity,
)

_LOGGER = logging.getLogger(__name__)

class FakevacuumEntity(StateVacuumEntity):
    """Representation of a fake vacuum entity."""

    def __init__(self, name):
        """Initialize the vacuum entity."""
        self._name = name
        self._state = None
        self._status = None
        self._battery_level = None
        self._fan_speed = None
        self._attr_fan_speed_list = ["low", "medium", "high"]

    @property
    def name(self):
        """Return the name of the vacuum entity."""
        return self._name

    @property
    def state(self):
        """Return the state of the vacuum entity."""
        return self._state

    @property
    def status(self):
        """Return the status of the vacuum entity."""
        return self._status

    @property
    def battery_level(self):
        """Return the battery level of the vacuum entity."""
        return self._battery_level

    @property
    def fan_speed(self):
        """Return the fan speed of the vacuum entity."""
        return self._fan_speed

    @property
    def supported_features(self):
        """Flag vacuum cleaner robot features that are supported."""
        return (
            VacuumEntityFeature.PAUSE |
            VacuumEntityFeature.STOP |
            VacuumEntityFeature.RETURN_HOME |
            VacuumEntityFeature.FAN_SPEED |
            VacuumEntityFeature.BATTERY |
            VacuumEntityFeature.STATUS |
            VacuumEntityFeature.STATE |
            VacuumEntityFeature.START
        )

    def start(self):
        """Start the vacuum cleaner."""
        pass

    def stop(self):
        """Stop the vacuum cleaner."""
        pass

    def return_to_base(self):
        """Send the vacuum cleaner back to its dock."""
        pass

    def clean_spot(self):
        """Perform a spot clean-up."""
        pass

    def locate(self):
        """Locate the vacuum cleaner."""
        pass

    def set_fan_speed(self, fan_speed, **kwargs):
        """Set fan speed."""
        pass

    def send_command(self, command, params=None, **kwargs):
        """Send a command to a vacuum cleaner."""
        pass
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the fake vacuum entry."""
    async_add_entities([FakevacuumEntity("Fake Vacuum")])
    return True