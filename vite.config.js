import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';
import FullReload from 'vite-plugin-full-reload';

export default defineConfig({
  base: '/tester-a11y/', // Nom du repo GitHub
  plugins: [
    FullReload(
      [
        'src/pages/**',
        'src/components/**',
        'style.scss',
        'index.js',
        'index.html',
        '404.html',
      ],
      { delay: 100 }
    ),
    viteStaticCopy({
      targets: [
        {
          src: 'src/pages', // Le dossier à copier
          dest: '', // Copie à la racine de /dist
        },
        {
          src: '404.html',
          dest: '',
        },
        {
          src: 'public/.nojekyll',
          dest: '',
        },
        {
          src: 'src/components',
          dest: '',
        },
        {
          src: 'src/assets/img',
          dest: 'src/assets/',
        },
        {
          src: 'src/assets/fonts',
          dest: 'src/assets/',
        },
      ],
    }),
  ],
});
