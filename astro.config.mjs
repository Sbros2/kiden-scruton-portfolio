import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1];
const isGitHubPages = process.env.GITHUB_ACTIONS === 'true' && repoName;

export default defineConfig({
  site: isGitHubPages ? `https://${process.env.GITHUB_REPOSITORY_OWNER}.github.io` : undefined,
  base: isGitHubPages ? `/${repoName}` : '/',
  integrations: [react()],
});