/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')
const colors = require('tailwindcss/colors');

module.exports = {
    important: true,
    darkMode: "class",
    content: [
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js',
        './node_modules/tw-elements/dist/js/**/*.js'
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    transparent: 'transparent',
                    current: 'currentColor',
                    black: colors.black,
                    white: colors.white,
                    rose: colors.rose,
                    pink: colors.pink,
                    fuchsia: colors.fuchsia,
                    purple: colors.purple,
                    violet: colors.violet,
                    indigo: colors.indigo,
                    blue: colors.blue,
                    sky: colors.sky, // As of Tailwind CSS v2.2, `lightBlue` has been renamed to `sky`
                    cyan: colors.cyan,
                    teal: colors.teal,
                    emerald: colors.emerald,
                    green: colors.green,
                    lime: colors.lime,
                    yellow: colors.yellow,
                    amber: colors.amber,
                    orange: colors.orange,
                    red: colors.red,
                    slate: colors.slate,
                    zinc: colors.zinc,
                    gray: colors.coolGray,
                    neutral: colors.slate,
                    stone: colors.stone,
                },
            },
            fontFamily: {
                sans: ['Inter var', ...defaultTheme.fontFamily.sans],
            },
        },
    },
    variants: {
        backgroundColor: ["checked"],
        borderColor: ["checked"],
        inset: ["checked"],
        zIndex: ["hover", "active"],
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('flowbite/plugin'),
        require('kutty'),
        require('tw-elements/dist/plugin'),
    ],
    future: {
        purgeLayersByDefault: true,
        removeDeprecatedGapUtilities: true,
    },
}
