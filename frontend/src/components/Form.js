import useSWR from "swr";
import axios from "axios";

export default function Form() {
  const fetcher = async (url) => {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  };
  const { data, error } = useSWR(
    "http://localhost:8000/get_all_data/",
    fetcher
  );
  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <p>ID: {data.id}</p>
      <p>Date: {data.date}</p>
      Creater: {data.creater}
    </div>
  );

  // return (
  //   <div class="flex h-screen items-center justify-center bg-[#fbfbfb]">
  //     <div class="grid w-80 grid-rows-3 gap-1">
  //       <p class="font-semibold text-gray-700">
  //         💌 Get the best of Product Hunt, directly in your inbox.
  //       </p>
  //       <input
  //         type="text"
  //         class="h-10 w-full rounded border p-2 text-sm"
  //         placeholder="Your email"
  //       />
  //       <button class="rounded bg-[#FD5E57] text-gray-50 hover:bg-gradient-to-r hover:from-[#FD5E57] hover:to-[#FC477E]">
  //         Subscribe to the newsletter
  //       </button>
  //       <a href="">
  //         <p class="mt-4 flex items-center text-xs text-gray-500 hover:text-gray-700">
  //           Read the latest issue
  //           <svg
  //             xmlns="http://www.w3.org/2000/svg"
  //             fill="none"
  //             viewBox="0 0 24 24"
  //             stroke-width="1.5"
  //             stroke="currentColor"
  //             class="ml-1 h-3 w-3"
  //           >
  //             <path
  //               stroke-linecap="round"
  //               stroke-linejoin="round"
  //               d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
  //             />
  //           </svg>
  //         </p>
  //       </a>
  //     </div>
  //   </div>
  // );
}
