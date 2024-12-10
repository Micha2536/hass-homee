# Ergänze die Konfigurationsoptionen
class OptionsFlowHandler(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        """Optionen bearbeiten."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = {
            "homeegram_ids": [
                (hg["id"], hg["name"]) for hg in self.hass.data[DOMAIN].get("homeegrams", [])
            ]
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("selected_homeegrams", default=[]): cv.multi_select(options["homeegram_ids"])
            }),
        )
