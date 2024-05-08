import { Pagination, Stack } from '@mui/material'
import Box from '@mui/material/Box'
import Divider from '@mui/material/Divider'
import { useLocation, useNavigate } from 'react-router-dom'
import { useBooksSearch } from 'src/books/rquery'
import BooksGrid from 'src/components/booksGrid'
import { Loading } from 'src/components/loading'

const SearchPage = () => {
  const location = useLocation()
  const navigate = useNavigate()

  const query = new URLSearchParams(location.search)
  const searchInput = query.get('q') || ''
  const page = parseInt(query.get('page') || '1', 10)
  const books = useBooksSearch({
    query: searchInput,
    num_of_books: 300,
  })
  const booksPerPage = 60
  const handleChange = (_: React.ChangeEvent<unknown>, value: number) => {
    query.set('page', value.toString() as string)
    navigate(`/app/search?${query.toString()}`)
  }
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
    </Box>
  )
}

export default SearchPage
