// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// IMPORTANT: change `site` to your GitHub Pages URL.
// - For a personal site repo named  <username>.github.io  -> keep base as '/'
//   e.g. site: 'https://janedoe.github.io'
// - For a normal project repo named  my-blog  -> set base: '/my-blog'
//   e.g. site: 'https://janedoe.github.io', base: '/my-blog'
export default defineConfig({
  site: 'https://vpccb.github.io',
  // base: '/my-blog',
  integrations: [sitemap()],
});
