import React from "react";

const Hero = () => {
  return (
    <>
      <div className="w-full flex justify-center items-center">
        <div className="w-[1266px] h-[520px] relative">
          <div className="w-[845px] h-[583px] left-0 top-[34px] absolute">
            <div className="w-[845px] left-0 top-0 absolute text-[#894799] text-[80px] font-bold  leading-[90px]">
              Transforming Grading Into a Breeze!
            </div>
            <div className="w-[600px] left-0 top-[330px] absolute text-[#894799] text-lg font-medium font-['Poppins'] leading-[30px]">
              "Let's make grading more organized and effortless with our
              streamlined platform, featuring the latest tools for efficient
              assessment."
            </div>
            <div className="h-[67px] px-[30px] py-5 left-0 top-[460px] absolute bg-[#894799] rounded-[40px] justify-center items-center gap-2.5 inline-flex">
              <div className="text-white text-lg font-medium font-['Poppins']">
                Click to Get Started
              </div>
            </div>
            <div className="w-[168.54px] h-10 left-[276.86px] top-[470px] absolute">
              <div className="w-[45.86px] h-10 px-[4.78px] py-[4.17px] left-0 top-0 absolute justify-center items-center inline-flex">
                <div className="w-[36.31px] h-[31.67px] relative"></div>
              </div>
              <div className="w-[112.36px] left-[56.18px] top-[9px] absolute text-[#191a15] text-lg font-medium font-['Poppins']">
                View Demo
              </div>
            </div>
          </div>
          <div className="w-[576px] h-[626px] left-[690px] top-0 absolute flex-col justify-center items-center inline-flex">
            <img className="w-[526px] h-[576px]" src="Hero_Image.png" />
          </div>
        </div>
      </div>
      <div className="w-full flex justify-center items-center mt-20 pt-16 ">
        <div className="w-[1194px] h-[162px] relative">
          <div className="left-[113px] top-0 absolute text-center text-[#894799] text-[40px] font-bold font-['Poppins']">
            More than 2K Lecturers use AutoGradePro From
          </div>
          <div className="w-[1194px] h-[102px] pl-5 pr-[19.09px] pt-[31px] pb-[21px] left-0 top-[60px] absolute justify-center items-start gap-[93.03px] inline-flex">
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
            <img
              className="w-[114.28px] h-[50px]"
              src="https://via.placeholder.com/114x50"
            />
          </div>
        </div>
      </div>
    </>
  );
};

export default Hero;
