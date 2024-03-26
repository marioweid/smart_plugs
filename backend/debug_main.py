from SmartDevice import SmartDevice

dev_id = "<DEV_ID>"
local_key = "<LOCAL_KEY>"
local_key = "<LOCAL_KEY>"
ip4_addr = "<IP4-ADDRESS>"
device = SmartDevice(
    dev_id=dev_id,
    local_key=local_key,
    ip4_addr=ip4_addr,
)


print(device.status())

device.toggle_power()