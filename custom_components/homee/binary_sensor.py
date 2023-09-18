"""The homee binary sensor platform."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorDeviceClass,
)
from homeassistant.config_entries import ConfigEntry
from pymee.const import AttributeType, NodeProfile
from pymee.model import HomeeAttribute, HomeeNode

from . import HomeeNodeEntity, helpers
from .const import CONF_DOOR_GROUPS, CONF_GROUPS, CONF_WINDOW_GROUPS

_LOGGER = logging.getLogger(__name__)

HOMEE_BINARY_SENSOR_ATTRIBUTES = [
    AttributeType.OPEN_CLOSE,
    AttributeType.ON_OFF,
    AttributeType.LOCK_STATE,
    AttributeType.SMOKE_ALARM,
]


def get_device_class(node: HomeeNodeEntity) -> int:
    """Determine the device class a homee node based on the available attributes."""
    device_class = BinarySensorDeviceClass.OPENING
    state_attr = AttributeType.OPEN_CLOSE

    if node._on_off.type == AttributeType.ON_OFF:
        state_attr = AttributeType.ON_OFF
        device_class = BinarySensorDeviceClass.PLUG

    if node._on_off.type == AttributeType.LOCK_STATE:
        state_attr = AttributeType.LOCK_STATE
        device_class = BinarySensorDeviceClass.LOCK

    if node._on_off.type == AttributeType.SMOKE_ALARM:
        state_attr = AttributeType.SMOKE_ALARM
        device_class = BinarySensorDeviceClass.SMOKE

    return (device_class, state_attr)


def is_binary_sensor_node(node: HomeeNode):
    """Determine if a node is a binary sensor based on profile and attributes."""
    return node.profile in [
        NodeProfile.OPEN_CLOSE_SENSOR,
        NodeProfile.OPEN_CLOSE_AND_TEMPERATURE_SENSOR,
        NodeProfile.OPEN_CLOSE_WITH_TEMPERATURE_AND_BRIGHTNESS_SENSOR,
        NodeProfile.LOCK,
        NodeProfile.SMOKE_DETECTOR,
        NodeProfile.SMOKE_DETECTOR_AND_CODETECTOR,
        NodeProfile.SMOKE_DETECTOR_AND_SIREN,
        NodeProfile.SMOKE_DETECTOR_WITH_TEMPERATURE_SENSOR,
    ]


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_devices):
    """Add the homee platform for the binary sensor integration."""

    devices = []
    for node in helpers.get_imported_nodes(hass, config_entry):
        for attribute in node.attributes:
            if attribute.type in HOMEE_BINARY_SENSOR_ATTRIBUTES:
                devices.append(HomeeBinarySensor(node, config_entry, attribute))
    if devices:
        async_add_devices(devices)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return True


class HomeeBinarySensor(HomeeNodeEntity, BinarySensorEntity):
    """Representation of a homee binary sensor device."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(
        self,
        node: HomeeNode,
        entry: ConfigEntry,
        binary_sensor_attribute: HomeeAttribute = None
    ) -> None:
        """Initialize a homee binary sensor entity."""
        HomeeNodeEntity.__init__(self, node, self, entry)

        self._on_off = binary_sensor_attribute
        self._configure_device_class()
        self._unique_id = f"{self._node.id}-binary_sensor-{self._on_off.id}"

    def _configure_device_class(self):
        """Configure the device class of the sensor."""

        # Get the initial device class and state attribute
        self._device_class, self._state_attr = get_device_class(self)

        # Set Window/Door device class based on configured groups
        if any(
            str(group.id) in self._entry.options[CONF_GROUPS].get(CONF_WINDOW_GROUPS, [])
            for group in self._node.groups
        ):
            self._device_class = BinarySensorDeviceClass.WINDOW
        elif any(
            str(group.id) in self._entry.options[CONF_GROUPS].get(CONF_DOOR_GROUPS, [])
            for group in self._node.groups
        ):
            self._device_class = BinarySensorDeviceClass.DOOR

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return bool(self.attribute(self._state_attr))

    @property
    def device_class(self):
        """Return the class of this device, from component DEVICE_CLASSES."""
        return self._device_class
