import * as React from 'react'
import { useBooksByIsbnsList } from 'src/books/rquery'
import ErrorPage from 'src/pages/error'
import { Shelf } from 'src/shelves/types'
import { convertBookToCarouselItem } from 'src/utils/convertBookToCarouselItem'

import BooksCarousel from '../carousel'
import { Loading } from '../loading'
interface Props {
  shelf: Shelf
}
const ShelfComp: React.FC<Props> = ({ shelf }) => {
  const books = useBooksByIsbnsList(shelf.books)
  if (books.isError || books.isIdle) {
    return <ErrorPage />
  }
  if (books.isLoading) {
    return <Loading />
  }
  return (
    <BooksCarousel
      title={shelf.name}
      items={books.data.map(convertBookToCarouselItem)}
      shelf_id={shelf._id}
    />
  )
}
export default ShelfComp
