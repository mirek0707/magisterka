import { get } from 'src/api'
import { useReactQuery } from 'src/rquery'

import { getBooksPerPagePath } from './api'
import { BooksPerPageReq, Book } from './types'

export const useBooksPerPage = (data: BooksPerPageReq) =>
  useReactQuery<Book[]>(get, getBooksPerPagePath(data))
