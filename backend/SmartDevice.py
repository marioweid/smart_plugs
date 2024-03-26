import tinytuya
from backend.models.tuya import DeviceStatus

class SmartDevice:

    def __init__(
        self, dev_id: str, local_key: str, ip4_addr: str, version: str = "3.3"
    ):
        self._device: tinytuya.OutletDevice = tinytuya.OutletDevice(
            dev_id=dev_id, address=ip4_addr, local_key=local_key, version=version
        )
    
    def status(self):
        return DeviceStatus(self._device.status())
    
    def is_on(self) -> bool:
        """Returns the power state of the SmartDevice

        Returns:
            bool: the power state of the device [1 (on) 0 (off)]
        """
        return self.status().is_on
    
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
