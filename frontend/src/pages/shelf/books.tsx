import { Divider, Pagination, Stack } from '@mui/material'
import * as React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { useBooksByIsbnsList } from 'src/books/rquery'
import BooksGrid from 'src/components/booksGrid'
import { Loading } from 'src/components/loading'
import ErrorPage from 'src/pages/error'

interface Props {
  isbns: string[]
}

const BooksOnShelf: React.FC<Props> = ({ isbns }) => {
  const location = useLocation()
  const navigate = useNavigate()
  const query = new URLSearchParams(location.search)
  const page = parseInt(query.get('page') || '1', 10)
  const books = useBooksByIsbnsList(isbns)

  if (books.isError || books.isIdle) {
    return <ErrorPage />
  }
  if (books.isLoading) {
    return <Loading />
  }
  const handleChange = (_: React.ChangeEvent<unknown>, value: number) => {
    query.set('page', value.toString() as string)
    navigate(`/app/books?${query.toString()}`)
  }
  const booksPerPage = 60
  return (
    <>
      <BooksGrid
        books={books.data.slice(booksPerPage * (page - 1), booksPerPage * page)}
      />
      <Divider sx={{ color: 'success.dark', m: 2 }} />
      <Stack spacing={2}>
        <Pagination
          onChange={handleChange}
          count={Math.ceil(books.data.length)}
          variant="outlined"
          shape="rounded"
          page={page}
        />
      </Stack>
    </>
  )
}

export default BooksOnShelf
