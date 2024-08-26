import React from "react";

const Header = () => {
  return (
    <div className="w-full flex justify-center items-center">
      <div className="w-full h-[107px] mx-5 pl-[5px] pt-[7px] pb-1 flex justify-center items-center gap-[35px] ">
        <img className="w-20 h-20" src="Logo.png" />
        <div className="w-[1146px] h-11 relative">
          <div className="w-[289.52px] left-0 top-0 absolute text-[#894799] text-4xl font-extrabold font-['Montserrat']">
            AutoGradePro
          </div>
          <div className="w-[434.28px] h-[27px] left-[421.14px] top-[7px] absolute">
            <div className="w-[54.28px] left-0 top-0 absolute text-black text-lg font-medium ">
              Home
            </div>
            <div className="w-[64.93px] left-[96.86px] top-[2px] absolute text-[#a6a6a6] text-base font-medium ">
              Product
            </div>
            <div className="w-[33px] left-[204.37px] top-[2px] absolute text-[#a6a6a6] text-base font-medium ">
              FAQ
            </div>
            <div className="w-[36.19px] left-[279.94px] top-[2px] absolute text-[#a6a6a6] text-base font-medium ">
              Blog
            </div>
            <div className="w-[75.57px] left-[358.71px] top-[2px] absolute text-[#a6a6a6] text-base font-medium ">
              About Us
            </div>
          </div>
          <div className="w-[152.21px] h-10 left-[993.79px] top-[2px] absolute">
            <div className="w-[45.77px] left-0 top-[8px] absolute text-[#a6a6a6] text-base font-medium ">
              Login
            </div>
            <div className="w-[85.15px] h-10 left-[67.06px] top-0 absolute">
              <div className="w-[85.15px] h-10 left-0 top-0 absolute bg-[#894799] rounded-[10px]" />
              <div className="w-[63.86px] left-[10.64px] top-[8px] absolute text-[#f8f8fa] text-base font-medium ">
                Sign Up
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
