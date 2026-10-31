import nextra from 'nextra'
import { fileURLToPath } from 'node:url'

const withNextra = nextra({})
export default withNextra({
  turbopack: { root: fileURLToPath(new URL('.', import.meta.url)) }
})
