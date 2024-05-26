from homeassistant.components.water_heater import WaterHeaterEntity, WaterHeaterEntityFeature

# Replace the deprecated constants with the new ones
SUPPORT_TARGET_TEMPERATURE = WaterHeaterEntityFeature.TARGET_TEMPERATURE
SUPPORT_OPERATION_MODE = WaterHeaterEntityFeature.OPERATION_MODE
SUPPORT_AWAY_MODE = WaterHeaterEntityFeature.AWAY_MODE

class FakeWaterHeaterEntity(WaterHeaterEntity):
    """Representation of a fake water heater entity."""

    def __init__(self, name):
        """Initialize the water heater entity."""
        self._name = name
        self._temperature = None
        self._operation_mode = None
        self._away_mode = None
        self._temperature_unit = '°C'

    @property
    def name(self):
        """Return the name of the water heater entity."""
        return self._name
    
    @property
    def temperature_unit(self):
        """Return the unit of measurement used by the platform."""
        return self._temperature_unit
    
    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_TARGET_TEMPERATURE | SUPPORT_OPERATION_MODE | SUPPORT_AWAY_MODE

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._temperature

    @property
    def operation_mode(self):
        """Return current operation ie. heat, cool, idle."""
        return self._operation_mode

    @property
    def is_away_mode_on(self):
        """Return true if away mode is on."""
        return self._away_mode

    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        pass

    def set_operation_mode(self, operation_mode):
        """Set new target operation mode."""
        pass

    def turn_away_mode_on(self):
        """Turn away mode on."""
        pass

    def turn_away_mode_off(self):
        """Turn away mode off."""
        pass
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the fake water heater entry."""
    async_add_entities([FakeWaterHeaterEntity("Fake Water Heater")])
    return True