import * as qs from 'qs'

import { BooksPerPageReq, BooksCountFiltersReq, BooksSearchData } from './types'

export const API_ROOT_PATH = '/books'

export const getBooksPerPagePath = (data: BooksPerPageReq) =>
  `${API_ROOT_PATH}?${qs.stringify(data)}`

export const getBookPath = (isbn: string) => `${API_ROOT_PATH}/${isbn}`

export const getBooksByIsbnsList = (isbns: string[]) => {
  const queryParams = { isbn: isbns }
  return `${API_ROOT_PATH}/list?${qs.stringify(queryParams, {
    arrayFormat: 'repeat',
  })}`
}

export const getBooksCount = (data: BooksCountFiltersReq) =>
  `${API_ROOT_PATH}/count?${qs.stringify(data)}`

export const getBooksAuthors = () => `${API_ROOT_PATH}/authors`
export const getBooksGenres = () => `${API_ROOT_PATH}/genres`
export const getBooksPublishers = () => `${API_ROOT_PATH}/publishers`
export const getBooksMinMaxYears = () => `${API_ROOT_PATH}/years`
export const getBooksSearch = (data: BooksSearchData) =>
  `${API_ROOT_PATH}/search?${qs.stringify(data)}`
export const getBooksSearchFt = (data: BooksSearchData) =>
  `${API_ROOT_PATH}/ftsearch?${qs.stringify(data)}`
