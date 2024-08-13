import * as qs from 'qs'
import { patch, put, del, post } from '/src/api'

import { ImportLCReq, AddShelfReq } from './types'

export const API_ROOT_PATH = '/shelf'

export const getUserShelves = (user_id: string) => `${API_ROOT_PATH}/${user_id}`
export const getUserShelf = (user_id: string, shelf_id: string) =>
  `${API_ROOT_PATH}/${user_id}/${shelf_id}`

export const patchAddBookToShelf = (user_id: string, isbn: string) =>
  patch(`${API_ROOT_PATH}/${user_id}/add/${isbn}`)
export const patchDelBookToShelf = (user_id: string, isbn: string) =>
  patch(`${API_ROOT_PATH}/${user_id}/del/${isbn}`)

export const putImportLC = (data: ImportLCReq) =>
  put(`${API_ROOT_PATH}/importLC?${qs.stringify(data)}`)

export const putImportGR = (data: FormData) =>
  put(`${API_ROOT_PATH}/importGR`, data)

export const deleteShelf = (shelf_id: string) =>
  del(`${API_ROOT_PATH}/${shelf_id}`)

export const addShelf = (data: AddShelfReq) =>
  post(`${API_ROOT_PATH}/add?${qs.stringify(data)}`)
