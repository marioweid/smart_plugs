from smart_plugs.SmartDevice import SmartDevice
import os

# Read environment variables or use default values
dev_id = os.environ.get("SMART_DEVICE_ID", "")
local_key = os.environ.get("SMART_DEVICE_LOCAL_KEY", "")
ip4_addr = os.environ.get("SMART_DEVICE_IP_ADDRESS", "default_ip_address")

# Create a new SmartDevice
device = SmartDevice(
    dev_id=dev_id,
    local_key=local_key,
    ip4_addr=ip4_addr,
)

print(device.status())

device.toggle_power()