# Existing website context

Snapshot of the implementation in `C:\Users\kiden\my-site`, inspected September 2026. This describes what exists, not a proposed redesign. `SITE_CONTEXT.md` separately contains researched biography, project background, and draft editorial content.

## Current product

A personal engineering portfolio for Kiden Scruton. The homepage introduces "Engineer // Systems & Hardware" and the header uses "ENGINEER + SYSTEM BUILDER." Its visual identity combines a dark background, teal circuitry, amber accents, futuristic headings, and a western science-fiction avatar.

There are two implemented page files: the homepage and a dedicated gyroscopic monorail page. Most other destinations are links awaiting implementation. There is no CMS interface, login, database, contact form, or backend service in the inspected source tree.

## Runtime and commands

- Astro with React integration, configured in `astro.config.mjs`.
- Package declarations: Astro `^5.12.9`, React/React DOM `^19.2.4`, `@astrojs/react` `^5.0.0`. These are declared ranges, not verified installed versions.
- `npm run dev` starts Astro development mode; the observed site address is `http://localhost:4321/`.
- `npm run build` builds the site; `npm run preview` previews a build.
- `OPENSITE.bat` changes to the hardcoded workspace path, launches the dev command, waits five seconds, then opens localhost.
- `README.md` remains the generic minimal Astro starter documentation.
- No test script or deployment configuration is declared in the inspected package/config files. No build or tests were run for this documentation task.

## Routes and navigation

| Destination | Implementation | Earlier live browser observation |
| --- | --- | --- |
| `/` | `src/pages/index.astro` | Loaded |
| `/projects/brennan-gyro-monorail/` | Dedicated Astro page | Loaded with simulation controls |
| `/projects` | No page file | 404 |
| `/resources` | No page file | 404 |
| `/about` | No page file | 404 |
| `/resume` | No page file or resume asset | 404 |
| FTC, Shelby Cobra, PCB detail URLs | Generated card links, no matching page files | 404 |

There is no dynamic project route such as `[slug].astro`. Markdown content entries alone do not currently create the linked project detail pages. Browser observations were made earlier in this conversation; this snapshot rechecked source, not browser behavior.

## Homepage composition

`src/pages/index.astro` loads both content collections. Projects are sorted newest first using JavaScript Date conversion and limited to four. Resources are sorted the same way, then filtered to at most two YouTube entries and two Game entries. Other supported resource kinds do not appear here.

Rendering order:

1. `BaseLayout` provides the document shell, background, header, main wrapper, and footer.
2. `HeroIntro` supplies the avatar, name, biography, and Projects/Resume/About buttons.
3. Four `ProjectCard` instances display the current project entries.
4. "Recent Helpful Links" displays video cards, followed by a Games label and game cards.

The hero biography is hardcoded as a default component prop. It mentions signal processing, analog PCBs, monorail, EKG, RockSat-C, FTC, ARSH, and HSR. It remains a long paragraph with spelling and grammar issues. These mentions do not mean matching project pages exist.

## Visual system

`src/layouts/BaseLayout.astro` contains most shared styles:

- Background `#0b0d0f`, primary text `#e2eef0`, muted text `#90a2a6`.
- Teal `#1de9b6`, amber `#ffb74d`, translucent dark panels and teal borders.
- Orbitron headings/navigation and Inter body text, loaded through Google Fonts.
- Main width `min(1200px, 92%)`, rounded panels, shadows, sticky blurred header.
- Four-column project grid with intended two-column and one-column media queries.

The hero defaults to a 380 by 420 pixel rounded rectangular avatar with text beside it. At 860 pixels it stacks and caps the image at 260 by 260 pixels. Its current image is `/assets/Post-Nuke_Western.jpg`, an illustrated character, while alt text calls it a portrait.

The active background is `ParallaxGrid.jsx`, hydrated with `client:load`. It draws a 22 by 12 canvas node grid, animates with requestAnimationFrame, and responds to pointer movement and resize. It cleans up its animation and listeners on unmount. No reduced-motion branch is present in this component.

Alternative background files include CssGradient, HexMesh, AuroraFlow, and CircuitTraces. CircuitTraces exists in both JSX and Astro forms with a CSS file. These alternatives are not active in the layout markup.

## Components and responsibility

| Component | Responsibility |
| --- | --- |
| `HeroIntro.astro` | Default identity copy, avatar configuration, call-to-action links, hero styling |
| `ProjectCard.astro` | Thumbnail, title, summary, date; constructs `/projects/${entry.slug}/` |
| `ResourceVideoCard.astro` | Video thumbnail, YouTube label, external title link, channel |
| `ResourceGameCard.astro` | Game thumbnail, external title link, game type |
| `ResourceCard.astro` | Generic resource kind, link, optional blurb; not used by homepage |
| `GyroSim.jsx` | Simulation calculation, controls, canvas plots, playback |
| `bg/ParallaxGrid.jsx` | Active animated page background |

Resource links open a new tab with `rel="noopener"`. Card styles are largely inline. Shared layout styles are in an Astro style block rather than a dedicated global stylesheet; cross-component style scope needs consideration when extending the site.

## Content collections

`src/content/config.ts` defines two content collections with schemas.

Projects require `title` and string `date`; optional fields are `summary`, string-array `tags`, and `thumbnail`. Resources require `title`, string `date`, and URL `href`; optional fields are `blurb`, `thumbnail`, `channel`, and `gameType`. Resource `kind` allows YouTube, Game, Article, Talk, Tool, and Other, defaulting to Other.

Dates are strings, with no explicit date validation. Tags exist in project data but are not rendered by the current project card.

| Entry | Date | Body and image status |
| --- | --- | --- |
| Monorail | 2026-03-11 | Descriptive Markdown paragraph; valid `/assets/Brennon_Monorail.jpg` reference |
| FTC Robotics | 2026-02-10 | Placeholder body; thumbnail lacks `/assets/` prefix |
| Shelby Cobra Cutaway | 2026-02-10 | Placeholder body; references existing cutaway JPEG |
| Precision PCB Demo | 2025-08-12 | Placeholder body; references existing PCB JPEG |
| Signal Windows FFT vs STFT | 2025-08-12 | YouTube `watch?v=xxxxx` placeholder; missing `/assets/yt1.jpg` |
| Opus Magnum | 2025-08-12 | Zachtronics link; references missing `/assets/opus.jpg` |

The FTC entry lives in `2025-08-12-pcb-demo - Copy (3).md`, producing an unrelated-looking slug. The Shelby filename spells Cobra as "Corba." Renaming entries changes their slug-derived card destinations, so update routes consistently.

Some tags say `threejs`, and the PCB summary promises a 3D interactive preview. No corresponding preview implementation or Three.js dependency appears in the inspected source. Treat these as unfinished content, not existing functionality.

## Monorail page and simulator

`src/pages/projects/brennan-gyro-monorail.astro` has its own HTML document and styles rather than using BaseLayout. It uses Arial, blue accents, a maximum width of 1100 pixels, and a Back to home link. It therefore differs from the homepage's typography and navigation.

Sections cover project overview, system concept, dynamic modeling, interactive simulation, control implementation, hardware, DIY decisions, testing, design shortfalls, skills, and documentation. The page prose is hardcoded separately from the monorail Markdown entry. Editing one does not update the other.

`GyroSim.jsx` integrates angle and angular velocity using fourth-order Runge-Kutta. The current acceleration expression is:

```text
phiDDot = (mgh / Ib) * sin(phi)
           - (2 * Is * omega * Kd / Ib) * phiDot
           - (2 * Is * omega * Kp / Ib) * phi
```

Controls include initial angle/velocity, proportional and damping gains, flywheel speed, vehicle/flywheel inertia, gravity term, time step, and duration. It includes Run and Reset, prototype/top views, angle and velocity time plots, and a phase plot. Classification uses a 90-degree angle threshold plus linearized stiffness/damping checks.

Important implementation boundaries:

- The page's displayed equation uses a positive `mgh` contribution alongside control stiffness, while the code's small-angle net stiffness subtracts `mgh`. Reconcile the explanation and code before treating the simulator as a validated technical reference.
- The simulation uses Kp and Kd; surrounding PID discussion also introduces Ki, which is not a simulation control.
- Text input commits parsed numbers without applying the slider bounds. Range controls and wheel adjustment clamp values, so validation behavior differs by input method.
- A response label is a heuristic, not experimental validation of the actual vehicle.
- The documentation section describes supporting files but does not offer those files as downloads.

## Static assets

`public/assets` contains seven files: the western avatar JPEG, another western helmet WebP, monorail JPEG, PCB JPEG, Shelby cutaway JPEG, FTC GIF, and `assetsopus.jpg`. Public files are served without `/public` in their URLs.

The Opus image filename is `assetsopus.jpg`, which does not match the content entry's `opus.jpg`. The YouTube thumbnail file is absent. The FTC GIF exists but its content reference omits the asset-directory prefix.

## Current issues and verification limits

Source inspection confirms that BaseLayout begins with `=---` instead of `---` and imports nonexistent `AuroraFlow.astro` while the available file is `AuroraFlow.jsx`. These remain source concerns even though the homepage previously loaded in the running browser. A fresh build has not been performed to establish the runtime consequence or explain that discrepancy.

The homepage has an inline four-column declaration that conflicts with the intended responsive rules. Mobile behavior has not been tested. The navigation and simulator also need narrow-screen review.

The footer contains literal replacement characters around the year/name, also observed in the earlier browser review. Missing route destinations and broken asset references should be addressed before expanding the project catalog.

## Editing map

- Change homepage intro: `src/components/HeroIntro.astro`.
- Change branding, navigation, footer, active background: `src/layouts/BaseLayout.astro`.
- Change ordering and displayed content types: `src/pages/index.astro`.
- Edit project card data: `src/content/projects`.
- Add functional project pages: `src/pages/projects` plus routing decisions.
- Edit resource links: `src/content/resources`.
- Edit monorail narrative: dedicated monorail Astro page.
- Edit simulation behavior: `src/components/GyroSim.jsx`.
- Add selected public media: `public/assets`.

Keep this snapshot separate from proposed content in `SITE_CONTEXT.md`. Neither context document is currently a public website route. This task only adds documentation and makes no application changes.
