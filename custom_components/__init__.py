"""Fake Entities Component."""
DOMAIN = "fake_entities"

DOMAINS = ['alarm_control_panel', 'binary_sensor', 'camera', 'climate', 'cover', 'device_tracker', 'fan', 'light', 'lock', 'media_player', 'notify', 'sensor', 'switch', 'vacuum', 'water_heater']

async def async_setup(hass, config):
    """Set up the Fake Entities component."""
    for domain in DOMAINS:
        hass.helpers.discovery.load_platform(domain, DOMAIN, {}, config)
    return True