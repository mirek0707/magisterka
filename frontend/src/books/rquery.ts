import { get } from 'src/api'
import { useReactQuery } from 'src/rquery'

import { getBooksPerPagePath, getBookPath, getBooksCount } from './api'
import { BooksPerPageReq, Book, BookCount } from './types'

export const useBooksPerPage = (data: BooksPerPageReq) =>
  useReactQuery<Book[]>(get, getBooksPerPagePath(data))

export const useBook = (isbn: string) =>
  useReactQuery<Book>(get, getBookPath(isbn))

export const useBookCount = () => useReactQuery<BookCount>(get, getBooksCount())
