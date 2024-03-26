from smart_plugs.SmartDevice import SmartDevice
import os

# Device 1
dev_id_1 = os.environ.get("SMART_DEVICE_1_ID", "xxx")
local_key_1 = os.environ.get("SMART_DEVICE_1_LOCAL_KEY", "xxx")
ip4_addr_1 = os.environ.get("SMART_DEVICE_1_IP_ADDRESS", "xxx")
device_1 = SmartDevice(
    dev_id=dev_id_1,
    local_key=local_key_1,
    ip4_addr=ip4_addr_1,
)

# Device 2
dev_id_2 = os.environ.get("SMART_DEVICE_2_ID", "xxx")
local_key_2 = os.environ.get("SMART_DEVICE_2_LOCAL_KEY", "xxx")
ip4_addr_2 = os.environ.get("SMART_DEVICE_2_IP_ADDRESS", "xxx")
device_2 = SmartDevice(
    dev_id=dev_id_2,
    local_key=local_key_2,
    ip4_addr=ip4_addr_2,
)


print(device_1.status())
print(device_2.status())

device_1.toggle_power()
device_2.toggle_power()