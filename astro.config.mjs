import { defineConfig } from 'astro/config';

const isVercel = Boolean(process.env.VERCEL);

// https://astro.build/config
export default defineConfig({
  site: isVercel ? 'https://moezaq.vercel.app' : 'https://mjurran-zaba.github.io',
  base: isVercel ? '/' : '/MOEZAQ',
});
