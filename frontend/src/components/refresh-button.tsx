'use client'
import { useRouter } from 'next/navigation';


function RefreshButton() {
  const router = useRouter();

  async function handleRefresh() {
    router.refresh()
  }

  return (
    <button type="button" onClick={async () => handleRefresh()}className="text-slate-200 bg-white border
    border-slate-200 focus:outline-none hover:bg-gray-100 focus:ring-4 
    focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-gray-800 
    dark:text-slate-200 dark:border-slate-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 
    dark:focus:ring-gray-700">Refresh</button>
  );
}

export default RefreshButton;
