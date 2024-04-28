import { Box, Divider } from '@mui/material'
import Pagination from '@mui/material/Pagination'
import * as React from 'react'
import { useBookCount } from 'src/books/rquery'
import BooksGrid from 'src/components/booksGrid'

const BooksPage: React.FC = () => {
  const bookCountObject = useBookCount()
  const bookCount = bookCountObject.data ?? 0
  const booksPerPage = 60
  const [page, setPage] = React.useState(1)

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <Box
        sx={{
          width: '100%',
          minWidth: '900px',
          maxWidth: '1600px',
        }}
      >
        <BooksGrid page={page} booksPerPage={booksPerPage} />
        <Divider sx={{ color: 'success.dark', m: 2 }} />

        <Pagination
          count={Math.ceil(bookCount / booksPerPage)}
          variant="outlined"
          shape="rounded"
          onChange={(_, value) => {
            setPage(value)
          }}
        />
      </Box>
    </Box>
  )
}

export default BooksPage
