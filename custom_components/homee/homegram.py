from homeassistant.helpers.entity import ToggleEntity

class HomeegramEntity(ToggleEntity):
    """Entität für ein homeegram mit Play/Stop und Aktivieren/Deaktivieren."""

    def __init__(self, homee, homeegram):
        self._homee = homee
        self._id = homeegram['id']
        self._name = homeegram['name']
        self._is_active = homeegram['active']
        self._is_running = False

    @property
    def name(self):
        """Gibt den Namen der Entität zurück."""
        return self._name

    @property
    def is_on(self):
        """Zeigt, ob das homeegram aktiv ist."""
        return self._is_active

    @property
    def extra_state_attributes(self):
        """Zusätzliche Statusinformationen."""
        return {
            "is_running": self._is_running,
        }

    def turn_on(self):
        """Aktiviert das homeegram."""
        self._homee.enable_homeegram(self._id)
        self._is_active = True
        self.schedule_update_ha_state()

    def turn_off(self):
        """Deaktiviert das homeegram."""
        self._homee.disable_homeegram(self._id)
        self._is_active = False
        self.schedule_update_ha_state()

    def play(self):
        """Startet das homeegram."""
        self._homee.play_homeegram(self._id)
        self._is_running = True
        self.schedule_update_ha_state()

    def stop(self):
        """Stoppt das homeegram."""
        self._homee.stop_homeegram(self._id)
        self._is_running = False
        self.schedule_update_ha_state()
