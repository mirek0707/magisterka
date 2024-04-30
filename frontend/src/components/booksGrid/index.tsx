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
  page: number
  booksPerPage: number
  prevGenre: string | null
}

const BooksGrid: React.FC<BooksGridProps> = ({
  page,
  booksPerPage,
  prevGenre,
}) => {
  const [genre, setGenre] = React.useState<string | null>(prevGenre)

  const books = useBooksPerPage({
    page,
    limit: booksPerPage,
    genre,
  })
  const genres = useBooksGenres()

  const [searchParams, setSearchParams] = useSearchParams()

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
              searchParams.set('genre', event.target.value as string)
              setSearchParams(searchParams)
            }}
          >
            {genres.status === 'success' ? (
              genres.data.genres.map((item, index) => (
                <MenuItem key={index} value={item}>
                  {item}
                </MenuItem>
              ))
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
