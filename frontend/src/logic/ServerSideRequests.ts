import { DeviceResponse } from "@/logic/models/Responses"

const defaultRequestProps: RequestInit = {cache: "no-store" }
const defaultRequestHeder: {} = {
    'Content-Type': 'application/json',
}

const backendURL = process.env.BACKEND_URL

export async function getDevices(): Promise<Array<DeviceResponse>> {
    const res = await fetch(`${backendURL}/devices`, {...defaultRequestProps, headers:defaultRequestHeder})
    return await res.json()
}

export async function toggleDevice(id: string): Promise<DeviceResponse> {
    const res = await fetch(`${backendURL}/devices/${id}/toggle`, {...defaultRequestProps, headers:defaultRequestHeder})
    return await res.json()
}