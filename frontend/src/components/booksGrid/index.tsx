import {
  Grid,
  Box,
  CssBaseline,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
} from '@mui/material'
import * as React from 'react'
import { useSearchParams } from 'react-router-dom'
import { useBooksPerPage, useBooksGenres } from 'src/books/rquery'
import { convertBookToCarouselItem } from 'src/utils/convertBookToCarouselItem'

import BookCard from '../carousel/card'
import { Loading } from '../loading'

interface BooksGridProps {
  prevPage: number
  booksPerPage: number
  prevGenre: string | null
}

const BooksGrid: React.FC<BooksGridProps> = ({
  prevPage,
  booksPerPage,
  prevGenre,
}) => {
  const [genre, setGenre] = React.useState<string | null>(prevGenre)
  const [page, setPage] = React.useState<number>(prevPage)

  const books = useBooksPerPage({
    page: prevPage,
    limit: booksPerPage,
    genre,
  })
  const genres = useBooksGenres()

  const [, setSearchParams] = useSearchParams()

  React.useEffect(() => {
    setSearchParams({
      genre: genre as string,
      page: page.toString() as string,
    })
  }, [genre])

  return (
    <>
      <Box sx={{ p: 2 }}>
        <CssBaseline />
        <FormControl variant="outlined">
          <InputLabel id="select-genre-label">Gatunek</InputLabel>
          <Select
            labelId="select-genre-label"
            label="Gatunek"
            value={genre}
            sx={{ width: 200 }}
            onChange={(event) => {
              setGenre(event.target.value as string)
              setPage(1)
            }}
          >
            <MenuItem value={''}>
              <em>Wszystkie</em>
            </MenuItem>
            {genres.status === 'success' ? (
              genres.data.genres.map((item: string, index: number) => {
                if (item !== '')
                  return (
                    <MenuItem key={index} value={item}>
                      {item}
                    </MenuItem>
                  )
              })
            ) : (
              <MenuItem value={''}>
                <em>Ładowanie</em>
              </MenuItem>
            )}
          </Select>
        </FormControl>
      </Box>
      <Grid container spacing={1} alignItems="">
        {books.status === 'success' ? (
          books.data.map((item, index) => (
            <Grid item xs={12 / 10} key={index}>
              <BookCard {...convertBookToCarouselItem(item)} />
            </Grid>
          ))
        ) : (
          <Loading />
        )}
      </Grid>
    </>
  )
}

export default BooksGrid
