# Proposed engineering portfolio

Independent source copy of the original site, with expanded project pages and navigation fixes. Original files remain in the parent directory.

Run `npm ci`, then `npm run dev -- --port 4322`. Build with `npm run build`.

The resume route is a curated HTML summary. The older PDF has not been published because its dates and future plans need updating. Selected project images were extracted from the user's presentations and testing archive; full academic documents and receipts are not published. The simulation remains illustrative, not physically validated.

Media and results update, September 13, 2026:
- FTC keeps its animated GIF card and adds a WebM/MP4 player plus three clearly captioned video stills.
- RockSat-C includes six original build/test photographs, linked mission confirmation, and a chart/table/download of the earlier IMU reference record.
- The reference record contains 13,577 rows over 496.239 seconds. It is not 2025 flight data. Electrical output and harvested energy are not established by the available files.
- Shared responsive project layouts, optimized WebP images, keyboard-accessible enlargement, and shorter project descriptions.

Source provenance is recorded in `MEDIA_SOURCES.md`. `.review/` contains private extraction and inspection artifacts and is excluded from git. Scripts named `build_proposal.py`, `polish_site.py`, and `finish_media.py` are historical one-time migrations: do not rerun them against the edited site. The source files are authoritative.
