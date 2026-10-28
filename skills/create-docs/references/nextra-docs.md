---
name: nextra-docs
description: "Local operational reference for generating a Nextra Docs Theme application under a target repository's docs directory."
version: "0.1.0"
created: "2026-10-28"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "The Nextra Project"
type: "reference"
status: "experimental"
---

# Nextra docs setup

Use this reference for interactive output. It was checked against the official Nextra documentation on 2026-10-28. Routine generation uses this local guide and the bundled starter. Read official sources when an installed version is incompatible, behavior differs, or a needed feature is not covered. This reference describes the Nextra 4 App Router model. Do not mix it with older Pages Router instructions.

## Select the package boundary

For a new site, make `<repository-root>/docs` a separate docs application. Keep its configuration, dependencies, lockfile or workspace membership, pages, and assets there. Reuse the repository's package manager and version policy. Inspect workspace globs before installation. A standalone package may need the package manager's existing workspace opt-out convention. Do not add a conflicting lockfile or quietly expand root workspace configuration.

A repository's `docs/` directory does not imply that the website uses a `/docs` URL prefix. The starter serves its landing page at `/`. Configure a URL prefix only for an established hosting requirement and verify resulting routes and search asset URLs.

Preserve an existing compatible Nextra application. If it uses `content/` with a catch-all route, keep that convention and consult the [content directory reference](https://nextra.site/docs/file-conventions/content-directory) when changing its routing. Do not create a second competing route for the same page. If an incompatible generator or maintained package occupies the required location, settle the layout before replacing it.

## Create a new docs package

Copy [the starter](../templates/nextra/) into `docs/` without overwriting maintained files. It provides a package manifest, Next.js configuration, theme component registration, root layout, and generated-output ignore rules. Replace the generic title in `docs.config.js` with the repository's actual name. Generate real page content separately. The starter intentionally supplies no invented project overview or generic documentation pages.

Run dependency installation from `docs/`. The following commands are the npm variant for a new standalone package. Use the equivalent operations for the repository's selected manager, and report the commands actually used.

```sh
npm install next react react-dom nextra nextra-theme-docs
npm install --save-dev pagefind
npm run dev
```

Resolve versions compatible with one another, the selected Node.js runtime, and repository constraints. Capture the resolved versions in the package manifest and lockfile. Do not promise that an arbitrary newer Next.js version works with a locked Nextra release. If installation fails, inspect the peer-dependency error and engine requirements. Do not hide incompatibility with force flags or upgrade application dependencies to make docs install.

The starter wraps Next.js configuration with `nextra()` and registers the Docs Theme's MDX components through a named `useMDXComponents` export. Its root layout loads the theme stylesheet and supplies `getPageMap()` to `Layout`. Keep `dir`, language, and theme hydration settings intact, adjusting language and direction for the generated content. These are the current [Docs Theme setup](https://nextra.site/docs/docs-theme/start) and [MDX registration](https://nextra.site/docs/file-conventions/mdx-components-file) conventions.

If a Turbopack build cannot resolve `next-mdx-import-source-file`, point its `resolveAlias` entry at the package's actual MDX components file using the configuration namespace supported by the installed Next.js version. Consult the MDX registration reference for that error rather than applying an unrelated webpack workaround.

## Build the page structure

The starter uses App Router files. `app/page.mdx` becomes `/`. `app/how-to/run-locally/page.mdx` becomes `/how-to/run-locally`. Nextra recognizes Markdown page extensions alongside Next.js page files. See [page conventions](https://nextra.site/docs/file-conventions/page-file).

The following is an illustrative structure for a project with contributor and integrator needs. Generate only the groups and pages justified by source evidence and reader outcomes.

```text
docs/
  package.json
  next.config.mjs
  mdx-components.js
  docs.config.js
  app/
    layout.jsx
    page.mdx
    _meta.js
    tutorials/
      _meta.js
      first-result/
        page.mdx
    how-to/
      run-locally/
        page.mdx
    reference/
      configuration/
        page.mdx
    explanation/
      architecture/
        page.mdx
  public/
    images/
```

Use `_meta.js` files beside the corresponding route folders to set readable titles and deliberate ordering. Keys name actual route segments. Include only existing destinations. The root landing page uses the `index` navigation key. Follow the [metadata convention](https://nextra.site/docs/file-conventions/meta-file). Frontmatter can supply a page title and description. Keep one useful main heading, and keep prose in the reader's documentation mode.

Use route links such as `/reference/configuration` between pages, adjusted for an actual configured prefix. A filesystem link ending in `page.mdx` is not the published route. Store public assets under `docs/public/` and reference them through their URL path. Link implementation sources to a verified repository URL and revision where useful. Filesystem-relative links that escape the docs app do not automatically become accessible web pages. Omit edit and feedback links when no valid repository destination is established.

## Configure design and components

Use the theme's navigation, sidebar, table of contents, theme switch, and responsive layout. Keep the landing page focused on reader tasks and the first useful result. Use the target project's established identity where available. Keep typography readable, tables usable on narrow screens, and focus visible. Avoid adding a separate marketing layout or decorative hero before readers can find the docs.

`Layout` accepts the page map and theme configuration. Set a project navbar and optional meaningful footer through its props. Add repository edit links only after verifying their content location. Do not copy upstream license text, release announcements, branding, or repository paths. See [Layout configuration](https://nextra.site/docs/docs-theme/built-ins/layout).

Use content components when they help readers:

| Component | Appropriate use | Official reference |
| --- | --- | --- |
| `Cards` and `Cards.Card` | A few task or audience entry points with descriptive titles and valid routes. | [Cards](https://nextra.site/docs/built-ins/cards) |
| `Callout` | A relevant caution or exception beside the affected action. | [Callout](https://nextra.site/docs/built-ins/callout) |
| `Steps` | An ordered procedure whose headings mark distinct actions. | [Steps](https://nextra.site/docs/built-ins/steps) |
| `Tabs` and `Tabs.Tab` | Genuine variants, with a complete usable procedure in each tab. | [Tabs](https://nextra.site/docs/built-ins/tabs) |

Import these components from `nextra/components` in the MDX page that uses them. For cards, supply `title` and `href` on `Cards.Card`. For tabs, supply matching `items` on `Tabs` and one `Tabs.Tab` per item. Do not create package-manager variants the target project does not support. Keep essential prerequisites visible outside collapsed or alternate content.

Interactive means the Nextra reading experience and useful MDX components. It does not require custom live examples, API calls, analytics, an AI assistant, or authentication. Add live execution only when explicitly requested and supported by safe, verified examples.

## Enable and verify search

Nextra search uses Pagefind to index generated HTML. The starter's `postbuild` script indexes a server build into `public/_pagefind`. See the [search setup](https://nextra.site/docs/guide/search).

From `docs/`, using npm:

```sh
npm run build
npm run start
```

Confirm that the selected package manager ran `postbuild`. If it does not run lifecycle hooks automatically, execute the indexing script explicitly and document the actual build command. Confirm `public/_pagefind` contains the generated index. Test a distinctive term from a generated page in the production preview and follow its result. A search box rendered in development does not establish that indexing works.

The starter uses a server build. Do not enable static export by default. If an established hosting requirement calls for static export, configure Next.js accordingly and change the index output to `out/_pagefind`, following the search reference. Confirm exported routes and asset paths in the actual preview. Keep `.next/`, `out/`, and generated search files out of version control.

## Verify and hand off

Build from the actual docs package with its resolved dependencies. Inspect representative rendered pages, direct nested URLs, sidebar ordering, links and fragments, images, code copy behavior, keyboard navigation, narrow screens, and light/dark modes. Verify search after indexing. Record build errors and unavailable browser checks accurately.

Keep an operating guide for the docs package in the project's appropriate contributor documentation. State its working directory, runtime requirements, package manager, install command, dev/build/start commands, content locations, navigation convention, and how Pagefind is regenerated. Distinguish maintaining the documentation application from using the documented product. Return to Create Docs for source agreement, reader-task verification, and its objective handoff. Do not deploy as part of generation.
