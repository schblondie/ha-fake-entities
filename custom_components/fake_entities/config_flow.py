import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN

class FakeDevicesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fake Devices."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Fake Devices", data={})

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({})
        )
