import DeviceCard from "@/components/device-card";
// import RefreshButton from "@/components/refresh-button";
import { DeviceResponse } from "@/logic/models/Responses";
import { getDevices, toggleDevice } from "@/logic/ServerSideRequests";

export default async function DeviceSite() {
    let devices: Array<DeviceResponse> = await getDevices()

    async function toggleFunction(id: string) {
      'use server'
      let response = await toggleDevice(id);
      console.log(response)
    }

    return (
        <main className="flex flex-col items-center p-6">
          <div className="w-full flex items-center flex-row pb-2">
            <h1 className="w-11/12 text-slate-200 text-4xl font-bold">Smart Plugs</h1>
            {/* <RefreshButton/> */}
          </div>
          
          <div className="w-full flex flex-col items-center gap-2">
          {devices.map(device => (
            <DeviceCard key={device.id} id={device.id} name={device.name} isOn={device.is_on} latest_event_time={device.latest_event_time} toggleFunction={toggleFunction}/>
          ))}            
          </div>


        </main>
    )
}