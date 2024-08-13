import axios from 'axios'

import { getAxiosAuthorizationHeader } from './headers'

export const axiosDefault = (function () {
  const instance = axios.create()

  instance.interceptors.request.use((config) => {
    config.headers['Authorization'] = 'Bearer ' + getAxiosAuthorizationHeader()
    return config
  })

  return instance
})()

export default axiosDefault
