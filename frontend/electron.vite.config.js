import react from '@vitejs/plugin-react';
import { defineConfig } from "electron-vite";

export default defineConfig({
    publicDir: false,
    main: {},
    preload: {},
    renderer: {
        plugins: [react()]
    }
});