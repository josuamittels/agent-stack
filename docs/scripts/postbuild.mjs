import fs from 'node:fs'
import path from 'node:path'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const docs = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const output = path.join(docs, 'out')
const site = new URL(process.env.DOCS_SITE_URL || 'https://agents.mittels.org')
if (!fs.existsSync(path.join(output, 'index.html'))) throw new Error('Build the static export first.')
const indexed = spawnSync('pagefind', ['--site', 'out', '--output-path', 'out/_pagefind'], {
  cwd: docs, stdio: 'inherit', shell: false,
})
if (indexed.status !== 0) process.exit(indexed.status || 1)

function htmlFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(directory, entry.name)
    return entry.isDirectory() ? htmlFiles(file) : entry.name === 'index.html' ? [file] : []
  })
}
const escapeXml = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
const urls = htmlFiles(output).filter(file => !file.includes('/_not-found/') && !file.includes('/out/404/')).map(file => {
  const relative = path.relative(output, path.dirname(file)).split(path.sep).join('/')
  return new URL(relative ? relative + '/' : '/', site).href
}).sort()
fs.writeFileSync(path.join(output, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls.map(url => `  <url><loc>${escapeXml(url)}</loc></url>`).join('\n') + '\n</urlset>\n')
fs.writeFileSync(path.join(output, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${new URL('/sitemap.xml', site).href}\n`)
console.log(`Static search, sitemap and robots ready for ${site.origin}: ${urls.length} routes.`)
