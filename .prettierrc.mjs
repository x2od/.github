import x2odPrettierConfig from '@x2od/prettier-config' with { type: 'json' };

/**
 * @see https://prettier.io/docs/configuration
 * @type {import("prettier").Config}
 */
const config = {
	...x2odPrettierConfig,
	overrides: [
		...x2odPrettierConfig.overrides,
		{
			files: '*.json*',
			options: {
				quoteProps: 'consistent',
				singleQuote: false,
				useTabs: false
			}
		},
		{
			files: '*.json5',
			options: {
				parser: 'jsonc',
				quoteProps: 'consistent',
				singleQuote: false
			}
		},
		// Extensionless "gh" scripts are shell files, so format them as sh.
		{
			files: 'gh',
			options: {
				parser: 'sh'
			}
		}
	]
};

export default config;
