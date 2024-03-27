"use client"

import PowerIcon from "@/components/power-icon"
import { useState } from "react"
import { useRouter } from 'next/navigation';

type DeviceCardProps = {
    name: string,
    isOn: boolean,
    id: string,
    toggleFunction: Function
}

export default function DeviceCard(props: DeviceCardProps) {
    let router = useRouter();


    function toggle(){
        props.toggleFunction(props.id);
        router.refresh()
    }

    return (
        <div className="p-6 w-full flex items-center flex-row bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 ">
            <h5 className="text-2xl w-11/12 select-none font-bold tracking-tight text-gray-900 dark:text-white">{props.name}</h5>
            <button onClick={() => toggle()}>
                {props.isOn ? <PowerIcon color="green" />: <PowerIcon color="red" />}
            </button>
        </div>

    );
};