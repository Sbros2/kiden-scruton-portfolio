import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { dirname, extname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = dirname(fileURLToPath(import.meta.url));
const distDir = join(scriptDir, '..', 'dist');
const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1];
const base = repoName ? `/${repoName}/` : process.env.PAGES_BASE_PATH || '/kiden-scruton-portfolio/';

const extensions = new Set(['.html', '.css', '.js', '.svg', '.xml', '.json']);
const attrs = ['href', 'src', 'poster', 'content'];

function walk(dir) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    const info = statSync(full);
    if (info.isDirectory()) walk(full);
    else if (extensions.has(extname(full))) rewriteFile(full);
  }
}

function prefixRootPath(path) {
  if (!path.startsWith('/')) return path;
  if (path.startsWith(base)) return path;
  if (path.startsWith('//')) return path;
  return `${base}${path.slice(1)}`;
}

function rewriteFile(file) {
  let text = readFileSync(file, 'utf8');
  const original = text;

  for (const attr of attrs) {
    text = text.replace(new RegExp(`${attr}="/(?!/)([^"]*)"`, 'g'), (_match, path) => `${attr}="${prefixRootPath(`/${path}`)}"`);
    text = text.replace(new RegExp(`${attr}='/(?!/)([^']*)'`, 'g'), (_match, path) => `${attr}='${prefixRootPath(`/${path}`)}'`);
  }

  text = text.replace(/srcset="([^"]*)"/g, (_match, value) => `srcset="${rewriteSrcset(value)}"`);
  text = text.replace(/srcset='([^']*)'/g, (_match, value) => `srcset='${rewriteSrcset(value)}'`);

  text = text.replace(/url\(\/(?!\/)([^)"']*)\)/g, (_match, path) => `url(${prefixRootPath(`/${path}`)})`);
  text = text.replace(/url\("\/(?!\/)([^")]*)"\)/g, (_match, path) => `url("${prefixRootPath(`/${path}`)}")`);
  text = text.replace(/url\('\/(?!\/)([^')]*)'\)/g, (_match, path) => `url('${prefixRootPath(`/${path}`)}')`);

  if (text !== original) writeFileSync(file, text);
}

function rewriteSrcset(value) {
  return value
    .split(',')
    .map((candidate) => {
      const leadingWhitespace = candidate.match(/^\s*/)?.[0] ?? '';
      const trimmed = candidate.trim();
      if (!trimmed) return candidate;

      const [url, ...descriptor] = trimmed.split(/\s+/);
      return `${leadingWhitespace}${[prefixRootPath(url), ...descriptor].join(' ')}`;
    })
    .join(',');
}

walk(distDir);
console.log(`Applied GitHub Pages base path: ${base}`);
