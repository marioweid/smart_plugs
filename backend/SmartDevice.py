import tinytuya
from models.tuya import DeviceStatus


class SmartDevice:

    def __init__(
        self,
        device_id: str,
        local_key: str,
        ip4_address: str,
        db_id: str | None = None,
        name: str | None = None,
        version: str = "3.3",
    ):
        self._device: tinytuya.OutletDevice = tinytuya.OutletDevice(
            dev_id=device_id, address=ip4_address, local_key=local_key, version=version
        )
        self.db_id = db_id
        self.name = name

    def status(self):
        status = self._device.status()
        print(status)
        return DeviceStatus(status)

    def is_on(self) -> bool:
        """Returns the power state of the SmartDevice and sets the self.latest_is_on

        Returns:
            bool: the power state of the device [1 (on) 0 (off)]
        """

        try:
            state = self.status().is_on
        except KeyError:
            state = False
        return state 

    def toggle_power(self) -> bool:
        """Toggles the power state of the device

        Returns:
            bool: The new power state of the device
        """
        if self.is_on():
            status = self._device.turn_off()
        else:
            status = self._device.turn_on()
        return DeviceStatus(status).is_on
