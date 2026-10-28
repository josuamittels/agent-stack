import { readFile, writeFile } from 'node:fs/promises'

const layoutPath = new URL('../node_modules/nextra-theme-docs/dist/layout.js', import.meta.url)
const expected = 'LayoutPropsSchema.safeParse(themeConfig)'
const fixed = 'LayoutPropsSchema.safeParse({ children, ...themeConfig })'

let source
try {
	source = await readFile(layoutPath, 'utf8')
} catch (error) {
	if (error.code === 'ENOENT') {
		throw new Error('Install the docs dependencies before applying the Nextra layout patch.')
	}
	throw error
}

if (source.includes(fixed)) process.exit(0)
if (!source.includes(expected)) {
	throw new Error('The installed Nextra layout does not match the version this patch supports.')
}

await writeFile(layoutPath, source.replace(expected, fixed))
console.log('Applied the Nextra Layout children validation patch.')
