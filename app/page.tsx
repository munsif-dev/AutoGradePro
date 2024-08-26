import React from "react";
import Demo from "@/components/Demo";
import InputAndLink from "@/components/InputAndLink";
import Pricing from "@/components/Pricing";
import Hero from "@/components/Hero";
import Features from "@/components/Features";

const page = () => {
  return (
    <>
      <Hero />
      <Features />
      <InputAndLink />
      <Pricing />
      <Demo />
    </>
  );
};

export default page;
