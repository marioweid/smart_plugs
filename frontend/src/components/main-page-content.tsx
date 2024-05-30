"use client"

import PowerIcon from "@/components/power-icon"
import LoadingSpinner from "@/components/load-spinner";
import { useState } from "react"
import { useRouter } from 'next/navigation';

type DeviceCardProps = {
    name: string,
    isOn: number,
    id: string,
    toggleFunction: Function
}

export default function MainPageContent(props: DeviceCardProps) {
    let router = useRouter();
    const [loading, setLoading] = useState<boolean>(false);

    async function toggle(){
        console.log(`loading: (${loading})`)
        setLoading(true);

        await props.toggleFunction(props.id);
        router.refresh();
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

    return (
        <div className="p-6 w-full flex items-center flex-row bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 ">
            <h5 className="text-2xl w-11/12 select-none font-bold tracking-tight text-gray-900 dark:text-white">{props.name}</h5>
            <button onClick={() => toggle()}>
                <PowerIcon color={getColor(props.isOn)} />
            </button>
            {loading && <LoadingSpinner />}
        </div>

    );
};