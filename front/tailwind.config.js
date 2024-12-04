/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      colors: {
        'gm': {
          primary: '#1a365d',
          secondary: '#2d3748',
        },
        'new-world': {
          primary: '#4a5568',
          secondary: '#2d3748',
        },
        'faction': {
          covenant: '#ecc94b',
          marauder: '#48bb78',
          syndicate: '#9f7aea',
        }
      },
      fontFamily: {
        'gmaster': ['gmaster', 'sans-serif'],
        'circular-web': ['circular-web', 'sans-serif'],
        'general': ['general', 'sans-serif'],
        'robert-medium': ['robert-medium', 'sans-serif'],
        'robert-regular': ['robert-regular', 'sans-serif'],
      },
    },
  },
  plugins: [],
  corePlugins: {  },
}

