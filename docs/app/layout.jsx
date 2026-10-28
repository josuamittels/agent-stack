import { Layout, Navbar } from 'nextra-theme-docs'
import { Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import { docsTitle } from '../docs.config'
import 'nextra-theme-docs/style.css'
import './reference-cards.css'

export const metadata = { title: docsTitle }

export default async function RootLayout({ children }) {
	return (
		<html lang="en" dir="ltr" suppressHydrationWarning>
			<Head />
			<body>
				<Layout
					navbar={<Navbar logo={<span>{docsTitle}</span>} />}
					pageMap={await getPageMap()}
					editLink={null}
					feedback={{ content: null }}
				>
					{children}
				</Layout>
			</body>
		</html>
	)
}
