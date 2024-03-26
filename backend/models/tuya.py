from dataclasses import dataclass


@dataclass
class DeviceStatus:
    """
    Human readable dictionary from the status()-function (currently only is_on is used)
    """

    is_on: bool
    countdown: int | None
    add_ele: int | None
    cur_current: int | None
    cur_power: int | None
    cur_voltage: int | None
    relay_status: str | None
    light_mode: str | None
    child_lock: bool | None
    cycle_time: str | None
    random_time: str | None
    switch_inching: str | None

    def __init__(self, device_status: dict):
        self.is_on: bool = device_status["dps"].get("1")  # Error if can't read
        self.countdown: int | None = device_status["dps"].get("9", None)
        self.add_ele: int | None = device_status["dps"].get("17", None)
        self.cur_current: int | None = device_status["dps"].get("18", None)
        self.cur_power: int | None = device_status["dps"].get("19", None)
        self.cur_voltage: int | None = device_status["dps"].get("20", None)
        self.relay_status: str | None = device_status["dps"].get("38", None)
        self.light_mode: str | None = device_status["dps"].get("39", None)
        self.child_lock: bool | None = device_status["dps"].get("40", None)
        self.cycle_time: str | None = device_status["dps"].get("41", None)
        self.random_time: str | None = device_status["dps"].get("42", None)
        self.switch_inching: str | None = device_status["dps"].get("43", None)

    def __repr__(self):
        return (
            f"DeviceStatus(\n"
            f"    is_on={self.is_on},\n"
            f"    countdown={self.countdown},\n"
            f"    add_ele={self.add_ele},\n"
            f"    cur_current={self.cur_current},\n"
            f"    cur_power={self.cur_power},\n"
            f"    cur_voltage={self.cur_voltage},\n"
            f"    relay_status={self.relay_status},\n"
            f"    light_mode={self.light_mode},\n"
            f"    child_lock={self.child_lock},\n"
            f"    cycle_time={self.cycle_time},\n"
            f"    random_time={self.random_time},\n"
            f"    switch_inching={self.switch_inching}\n"
            f")"
        )
