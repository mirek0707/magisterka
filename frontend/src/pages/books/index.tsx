import { Box, CssBaseline, Divider, PaginationItem, Stack } from '@mui/material'
import Pagination from '@mui/material/Pagination'
import * as React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useBookCount } from 'src/books/rquery'
import BooksGrid from 'src/components/booksGrid'

const BooksPage: React.FC = () => {
  const location = useLocation()
  const query = new URLSearchParams(location.search)
  const page = parseInt(query.get('page') || '1', 10)

  const bookCountObject = useBookCount()
  const booksPerPage = 60
  console.log(bookCountObject)
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
        <BooksGrid page={page} booksPerPage={booksPerPage} />
        <Divider sx={{ color: 'success.dark', m: 2 }} />
        {bookCountObject.status === 'success' ? (
          <Stack spacing={2}>
            <Pagination
              count={Math.ceil(bookCountObject.data.count / booksPerPage)}
              variant="outlined"
              shape="rounded"
              page={page}
              renderItem={(item) => (
                <PaginationItem
                  component={Link}
                  to={`/app/books${
                    item.page === 1 ? '' : `?page=${item.page}`
                  }`}
                  {...item}
                />
              )}
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
