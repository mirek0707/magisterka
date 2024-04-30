import { get } from 'src/api'
import { useReactQuery } from 'src/rquery'

import {
  getBooksPerPagePath,
  getBookPath,
  getBooksCount,
  getBooksGenres,
} from './api'
import { BooksPerPageReq, Book, BookCount, BooksGenres } from './types'

export const useBooksPerPage = (data: BooksPerPageReq) =>
  useReactQuery<Book[]>(get, getBooksPerPagePath(data))

export const useBook = (isbn: string) =>
  useReactQuery<Book>(get, getBookPath(isbn))

export const useBooksCount = () =>
  useReactQuery<BookCount>(get, getBooksCount())

export const useBooksGenres = () =>
  useReactQuery<BooksGenres>(get, getBooksGenres())
