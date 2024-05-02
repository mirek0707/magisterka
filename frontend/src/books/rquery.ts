import { get } from 'src/api'
import { useReactQuery } from 'src/rquery'

import {
  getBooksPerPagePath,
  getBookPath,
  getBooksCount,
  getBooksGenres,
  getBooksAuthors,
  getBooksPublishers,
  getBooksMinMaxYears,
} from './api'
import {
  BooksPerPageReq,
  Book,
  BooksCount,
  BooksCountFiltersReq,
  BooksGenres,
  BooksAuthors,
  BooksPublishers,
  BooksMinMaxYears,
} from './types'

export const useBooksPerPage = (data: BooksPerPageReq) =>
  useReactQuery<Book[]>(get, getBooksPerPagePath(data))

export const useBook = (isbn: string) =>
  useReactQuery<Book>(get, getBookPath(isbn))

export const useBooksCount = (data: BooksCountFiltersReq) =>
  useReactQuery<BooksCount>(get, getBooksCount(data))

export const useBooksAuthors = () =>
  useReactQuery<BooksAuthors>(get, getBooksAuthors())

export const useBooksGenres = () =>
  useReactQuery<BooksGenres>(get, getBooksGenres())

export const useBooksPublishers = () =>
  useReactQuery<BooksPublishers>(get, getBooksPublishers())

export const useBooksMinMaxYears = () =>
  useReactQuery<BooksMinMaxYears>(get, getBooksMinMaxYears())
