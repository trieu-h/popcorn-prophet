import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import tailwindcss from '@tailwindcss/vite'
import path from "path";
import { router } from 'sv-router/vite-plugin';

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte(), tailwindcss(), router()],
  resolve: {
    alias: {
      $lib: path.resolve("./src/lib"),
    },
  },
  base: "/popcorn-prophet/"
})
