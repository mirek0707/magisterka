const host = import.meta.env.VITE_BACKEND_URL

if (!host) throw new Error('VITE_BACKEND_URL missing.')

export { host }

export const apiBaseUrl = `${host}`
