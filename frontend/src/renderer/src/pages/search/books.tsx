import { Box, Pagination, Stack } from '@mui/material'
import Divider from '@mui/material/Divider'
import * as React from 'react'
import { UseQueryResult } from 'react-query'
import { useNavigate } from 'react-router-dom'
import { Book } from '/src/books/types'
import BooksGrid from '/src/components/booksGrid'
import { Loading } from '/src/components/loading'
type Props = {
  query: URLSearchParams
  page: number
  books: UseQueryResult<Book[], unknown>
}

const SearchResultBooks: React.FC<Props> = ({ query, page, books }) => {
  const navigate = useNavigate()

  const booksPerPage = 60
  const handleChange = (_: React.ChangeEvent<unknown>, value: number) => {
    query.set('page', value.toString() as string)
    navigate(`/app/search?${query.toString()}`)
  }
  return (
    <Box
      sx={{
        width: '100%',
        minWidth: '900px',
        maxWidth: '1600px',
      }}
    >
      {books.isSuccess ? (
        <BooksGrid
          books={books.data.slice(
            booksPerPage * (page - 1),
            booksPerPage * page
          )}
        />
      ) : (
        <Loading />
      )}
      <Divider sx={{ color: 'success.dark', m: 2 }} />
      {books.isSuccess ? (
        <Stack spacing={2}>
          <Pagination
            onChange={handleChange}
            count={Math.ceil(books.data.length / booksPerPage)}
            variant="outlined"
            shape="rounded"
            page={page}
          />
        </Stack>
      ) : (
        <Loading />
      )}
    </Box>
  )
}

export default SearchResultBooks
