import { SignUp } from "@clerk/nextjs";
import Image from "next/image";

export default function Page() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
      <div className="max-w-screen-lg m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
        <div className=" bg-light-1  lg:flex lg:flex-wrap lg:gap-0 lg:justify-center  lg:items-center  rounded-l-lg hidden ">
          <div className="flex justify-center">
            <Image
              src="/Hero_image.png"
              alt="Logo"
              width={400} // Set the appropriate width
              height={400} // Set the appropriate height
              className="w-mx-auto mt-3"
            />
          </div>
          <div className="w-full lg:w-80  m-0 text-center text-white text-xl font-bold font-['Biryani'] ">
            Automated Grading System
          </div>
          <div className="w-full lg:w-80 m-0 text-center text-white text-base font-normal font-['Bubbler One'] ">
            "Empower your grading journey with precision and purpose”
          </div>
        </div>

        <div className="lg:w-1/2 flex items-center justify-center p-6 sm:p-12">
          <SignUp />
        </div>
      </div>
    </div>
  );
}
