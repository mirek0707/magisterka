import path from 'path'

import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      src: path.resolve('src/'),
    },
  },
  server: {
    watch: {
      usePolling: true,
    },
  },
})
