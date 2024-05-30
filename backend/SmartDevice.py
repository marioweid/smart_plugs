import tinytuya
from models.tuya import DeviceStatus


class SmartDevice:
    def __init__(
        self,
        device_id: str,
        local_key: str,
        ip4_address: str,
        id: str | None = None,
        name: str | None = None,
        version: str = "3.3",
    ):
        self._device: tinytuya.OutletDevice = tinytuya.OutletDevice(
            dev_id=device_id,
            address=ip4_address,
            local_key=local_key,
            version=version,
            connection_retry_limit=1,
            connection_timeout=3,
        )
        self.id = id
        self.name = name
        self.ip4 = ip4_address

    def status(self) -> DeviceStatus:
        """Get the state of the device.

        Returns:
            DeviceStatus: state of the device
              - is_on (int): 0=off 1=on 2=unknown
        """
        status = self._device.status()
        return DeviceStatus(status)

    def toggle_power(self) -> int:
        """Toggles the power state of the device

        Returns:
            int: The new power state of the device
        """
        match self.status().is_on:
            case 1:
                status = self._device.turn_off()
            case 0:
                status = self._device.turn_on()
            case _:
                return 2
        return DeviceStatus(status).is_on
