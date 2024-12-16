/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  daisyui: {
    themes: ["cupcake"],
  },
  theme: {
    
    extend: {
      colors: {
        primary: {
          DEFAULT: '#1d4ed8', // Blue
          hover: '#2563eb',  // Blue Hover
          active: '#1e3a8a', // Blue Active
        },
      },
    },
  },
  plugins: [require('daisyui'),],
}

