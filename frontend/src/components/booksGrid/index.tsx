import { Grid } from '@mui/material'
import * as React from 'react'
import { useBooksPerPage } from 'src/books/rquery'
import { Book } from 'src/books/types'
import { CarouselItemProps } from 'src/components/carousel/types'

import BookCard from '../carousel/card'

interface BooksGridProps {
  page: number
  booksPerPage: number
}

const BooksGrid: React.FC<BooksGridProps> = ({ page, booksPerPage }) => {
  const books = useBooksPerPage({ page, limit: booksPerPage })
  const convertBookToCarouselItem = (book: Book): CarouselItemProps => {
    return {
      title: book.title[0],
      img_src:
        book.img_src && book.img_src[0]
          ? book.img_src[0]
          : 'https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg',
      author: book.author[0],
      isbn: book.isbn,
    }
  }
  return (
    <Grid container spacing={1} alignItems="">
      {books.status === 'success' ? (
        books.data.map((item) => (
          <Grid item xs={12 / 10}>
            <BookCard {...convertBookToCarouselItem(item)} />
          </Grid>
        ))
      ) : (
        <Loading />
      )}
    </Grid>
  )
}
function Loading() {
  return <h2>🌀 Ładowanie...</h2>
}

export default BooksGrid
