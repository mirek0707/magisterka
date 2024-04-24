import qs from 'qs'
import { post } from 'src/api'

import { RegisterFormData, LoginFormData } from './schema'
import { LoginResponse } from './types'

export const API_ROOT_PATH = '/user'

export const postLogin = (data: LoginFormData) =>
  post<LoginResponse>(API_ROOT_PATH + `/login`, qs.stringify(data)).then(
    (response) => response.data
  )

export const postRegister = (data: RegisterFormData) =>
  post<LoginResponse>(API_ROOT_PATH + `/register`, data).then(
    (response) => response.data
  )
