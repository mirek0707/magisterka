import { Grid } from '@mui/material'
import { Book } from 'src/books/types'
import { convertBookToCarouselItem } from 'src/utils/convertBookToCarouselItem'

import BookCard from '../carousel/card'

interface BooksGridProps {
  books: Book[]
  refetchShelf?: () => void
}

const BooksGrid: React.FC<BooksGridProps> = ({ books, refetchShelf }) => {
  return (
    <Grid container spacing={1} alignItems="">
      {books.map((item, index) => (
        <Grid item xs={12 / 10} key={index}>
          <BookCard
            {...convertBookToCarouselItem(item)}
            bookAdd={true}
            refetchShelf={refetchShelf}
          />
        </Grid>
      ))}
    </Grid>
  )
}

export default BooksGrid
