import nextra from 'nextra'
import { fileURLToPath } from 'node:url'

const withNextra = nextra({})
export default withNextra({
  output: 'export',
  trailingSlash: true,
  images: { unoptimized: true },
  turbopack: { root: fileURLToPath(new URL('.', import.meta.url)) },
})
