/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        'vf-red' : '#930303',
        'red-logo':'#b40000'
      },
      backgroundImage:{
        logo: "url('./assets/altLogo.png')",
      },
    },
  },
  plugins: [],
}

