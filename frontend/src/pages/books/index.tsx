import { Box, CssBaseline, Divider, Stack } from '@mui/material'
import Pagination from '@mui/material/Pagination'
import * as React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { useBooksCount, useBooksMinMaxYears } from 'src/books/rquery'
import BooksGridWithFilters from 'src/components/booksGridWithFilters'
import { Loading } from 'src/components/loading'

const BooksPage: React.FC = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const query = new URLSearchParams(location.search)
  const page = parseInt(query.get('page') || '1', 10)
  const genre = query.get('genre') || ''
  const author = query.get('author') || ''
  const publisher = query.get('publisher') || ''
  const minmax_year = useBooksMinMaxYears()
  const min_release_year = minmax_year.data?.min_year as number
  const max_release_year = minmax_year.data?.max_year as number

  let release_year_from = parseInt(
    query.get('release_year_from') || '-9999',
    10
  )
  let release_year_to = parseInt(query.get('release_year_to') || '-9999', 10)
  if (release_year_from === -9999 || release_year_to === -9999) {
    release_year_from = minmax_year.data?.min_year as number
    release_year_to = minmax_year.data?.max_year as number
  }

  const bookCountObject = useBooksCount({
    genre,
    author,
    publisher,
    release_year_from,
    release_year_to,
  })
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
        {minmax_year.isSuccess ? (
          <>
            <BooksGridWithFilters
              prevPage={page}
              booksPerPage={booksPerPage}
              prevGenre={genre}
              prevAuthor={author}
              prevPublisher={publisher}
              release_year_from={release_year_from}
              release_year_to={release_year_to}
              min_release_year={min_release_year}
              max_release_year={max_release_year}
            />
            <Divider sx={{ color: 'success.dark', m: 2 }} />
            {bookCountObject.isSuccess ? (
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
              <Loading />
            )}
          </>
        ) : (
          <Loading />
        )}
      </Box>
    </Box>
  )
}

export default BooksPage
