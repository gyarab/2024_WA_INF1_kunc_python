/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
	content: [
		"../../app/templates/**/*.html",
		"../../app/templates/**/*.js",
		"../../app/templates/**/*.jsx",
		"../../app/templates/**/**/*.html",
		"../../app/templates/*.html",
		"../../app/templates/**/*/*.html",
	],
	theme: {
		extend: {},
	},
	plugins: [
		/**
		 * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
		 * for forms. If you don't like it or have own styling for forms,
		 * comment the line below to disable '@tailwindcss/forms'.
		 */
		require("@tailwindcss/forms"),
		require("@tailwindcss/typography"),
		require("@tailwindcss/aspect-ratio"),
	],
};
