"""Fake Entities Component."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "fake_entities"
DOMAINS = [
    'alarm_control_panel', 'binary_sensor', 'camera', 'climate', 'cover',
    'device_tracker', 'fan', 'light', 'lock', 'media_player',
    'sensor', 'switch', 'vacuum', 'water_heater'
]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Fake Entities component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Fake Entities from a config entry."""
    for domain in DOMAINS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, domain)
        )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    for domain in DOMAINS:
        await hass.config_entries.async_forward_entry_unload(entry, domain)
    return True
