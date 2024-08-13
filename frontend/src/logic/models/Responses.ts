export type DeviceResponse = {
    id: string,
    is_on: number, // 0=off 1=on 2=unknown
    name: string
    latest_event_time: string
}