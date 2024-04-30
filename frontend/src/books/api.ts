import * as qs from 'qs'

import { BooksPerPageReq } from './types'

export const API_ROOT_PATH = '/books'

export const getBooksPerPagePath = (data: BooksPerPageReq) =>
  `${API_ROOT_PATH}?${qs.stringify(data)}`

export const getBookPath = (isbn: string) => `${API_ROOT_PATH}/${isbn}`

export const getBooksCount = () => `${API_ROOT_PATH}/count`

export const getBooksGenres = () => `${API_ROOT_PATH}/genres`
