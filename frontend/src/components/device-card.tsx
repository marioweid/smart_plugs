"use client"

import PowerIcon from "@/components/power-icon"
import LoadingSpinner from "@/components/load-spinner";
import { useState } from "react"
import { useRouter } from 'next/navigation';

type DeviceCardProps = {
    name: string,
    isOn: number,
    id: string,
    latest_event_time: string,
    toggleFunction: Function
}

export default function DeviceCard(props: DeviceCardProps) {
    let router = useRouter();
    const [loading, setLoading] = useState<boolean>(false);

    async function toggle(){
        setLoading(true);

        await props.toggleFunction(props.id);
        router.refresh();
        setLoading(false);
    }

    function getColor(status: number){
        switch (status) {
            case 0:
                return "red";
            case 1:
                return "green";
            case 2:
                return "gray";
            default:
                return "gray"; // fallback color
        }
    };

    function formatDateTime(input: string): string {
        if (input=== ""){
            return ""
        }
        const [datePart, timePart] = input.split(' ');
        const [hours, minutes, seconds] = timePart.split(':');
        return `${hours}:${minutes}`;   
    };

    return (
        <div className="p-6 w-full flex items-center flex-row bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 ">
            <div className="w-11/12 select-none tracking-tight ">
                <h5 className="text-2xl font-bold text-gray-900 dark:text-white">{props.name}</h5>
                <p> Last toggle: {formatDateTime(props.latest_event_time)}</p>

            </div>
            <button onClick={() => toggle()}>
                <PowerIcon color={getColor(props.isOn)} />
            </button>
            {loading && <LoadingSpinner />}
        </div>

    );
};