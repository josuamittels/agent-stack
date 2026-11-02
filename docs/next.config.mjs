import nextra from 'nextra'
import { fileURLToPath } from 'node:url'

const withNextra = nextra({})
export default withNextra({
  turbopack: { root: fileURLToPath(new URL('.', import.meta.url)) },
  async redirects() {
    return [{
      source: '/capabilities/disciplines/natural-writing',
      destination: '/capabilities/disciplines/write',
      permanent: true,
    }]
  },
})
