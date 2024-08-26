import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
        "blurred-ellipse": 'url("/path-to-your-ellipse.svg")',
      },
      colors: {
        "custom-purple": "#894799",
      },
      blur: {
        "500": "500px",
      },

      fontFamily: {
        sans: ["Poppins", "sans-serif", "Pacifico"], // Set Poppins as the default sans font family
      },
    },
  },
  plugins: [
    function ({ addUtilities }) {
      addUtilities(
        {
          ".ellipse": {
            width: "733.5px",
            height: "592px",
            flexShrink: "0",
            backgroundColor: "#894799",
            filter: "blur(500px)",
            borderRadius: "50%", // Makes the element an ellipse if the width and height are different
          },
        },
        ["responsive", "hover"]
      );
    },
  ],
};
export default config;
