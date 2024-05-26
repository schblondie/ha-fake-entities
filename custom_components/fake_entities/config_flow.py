import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN

class FakeEntitiesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fake Entities."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return FakeEntitiesOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Fake Entities", data={})

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({})
        )

class FakeEntitiesOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle an options flow for Fake Entities."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init", data_schema=vol.Schema({})
        )
