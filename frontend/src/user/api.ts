import { get, del } from '../api'
import { API_ROOT_PATH } from '../auth/api'

import { User } from './types'

export const USER_SESSION_API_PATH = API_ROOT_PATH

export const getUserSession = () =>
  get<User>(USER_SESSION_API_PATH).then((response) => response.data)

export const deleteUser = (user_id: string) =>
  del(`${API_ROOT_PATH}/${user_id}`)
