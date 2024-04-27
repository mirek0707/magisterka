import * as React from 'react'
import { useParams } from 'react-router-dom'
import { useBook } from 'src/books/rquery'

import ErrorPage from '../error'
const BookPage: React.FC = () => {
  const { isbn = '' } = useParams()
  const book = useBook(isbn)
  if (book.status !== 'success') {
    return <ErrorPage />
  }
  console.log(book.data)
  return <>Book </>
}

export default BookPage
