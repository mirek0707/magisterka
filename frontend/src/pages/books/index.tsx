import { Box, CssBaseline, Divider, Stack } from '@mui/material'
import Pagination from '@mui/material/Pagination'
import * as React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { useBooksCount } from 'src/books/rquery'
import BooksGrid from 'src/components/booksGrid'

const BooksPage: React.FC = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const query = new URLSearchParams(location.search)
  const page = parseInt(query.get('page') || '1', 10)
  const genre = query.get('genre') || ''

  const bookCountObject = useBooksCount({ genre })
  const booksPerPage = 60
  const handleChange = (_: React.ChangeEvent<unknown>, value: number) => {
    query.set('page', value.toString() as string)
    navigate(`/app/books?${query.toString()}`)
  }
  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <CssBaseline />
      <Box
        sx={{
          width: '100%',
          minWidth: '900px',
          maxWidth: '1600px',
        }}
      >
        <BooksGrid
          prevPage={page}
          booksPerPage={booksPerPage}
          prevGenre={genre}
        />
        <Divider sx={{ color: 'success.dark', m: 2 }} />
        {bookCountObject.status === 'success' ? (
          <Stack spacing={2}>
            <Pagination
              onChange={handleChange}
              count={Math.ceil(bookCountObject.data.count / booksPerPage)}
              variant="outlined"
              shape="rounded"
              page={page}
            />
          </Stack>
        ) : (
          <>czekam</>
        )}
      </Box>
    </Box>
  )
}

export default BooksPage
