import x2odPrettierConfig from "@x2od/prettier-config" with { type: "json" };

/**
 * @see https://prettier.io/docs/configuration
 * @type {import("prettier").Config}
 */
const config = {
	...x2odPrettierConfig,
	overrides: [
		...x2odPrettierConfig.overrides,
		{
			files: "package.json",
			options: {
				printWidth: 100
			}
		},
		{
			files: "*.json5",
			options: {
				quoteProps: "preserve",
				singleQuote: false
			}
		},
		// Extensionless "gh" scripts are shell files, so format them as sh.
		{
			files: "gh",
			options: {
				parser: "sh"
			}
		}
	]
};

export default config;
