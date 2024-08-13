import {
  Grid,
  Box,
  CssBaseline,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  Autocomplete,
  TextField,
  Slider,
  Typography,
  FilterOptionsState,
} from '@mui/material'
import { matchSorter } from 'match-sorter'
import * as React from 'react'
import { useSearchParams } from 'react-router-dom'
import {
  useBooksPerPage,
  useBooksGenres,
  useBooksAuthors,
  useBooksPublishers,
} from '/src/books/rquery'

import BooksGrid from '../booksGrid'
import { Loading } from '../loading'

interface BooksGridWithFilters {
  prevPage: number
  booksPerPage: number
  prevGenre: string | null
  prevAuthor: string | null
  prevPublisher: string | null
  release_year_from: number
  release_year_to: number
  min_release_year: number
  max_release_year: number
}

interface AutocompleteOption {
  label: string
  value: string
}

function valueLabelFormat(value: number[]) {
  return `Lata wydania: ${value[0]} – ${value[1]} r.`
}

const BooksGridWithFilters: React.FC<BooksGridWithFilters> = ({
  prevPage,
  booksPerPage,
  prevGenre,
  prevAuthor,
  prevPublisher,
  release_year_from,
  release_year_to,
  min_release_year,
  max_release_year,
}) => {
  const [genre, setGenre] = React.useState<string | null>(prevGenre)
  const [page, setPage] = React.useState<number>(prevPage)
  const [author, setAuthor] = React.useState<string | null>(prevAuthor)
  const [publisher, setPublisher] = React.useState<string | null>(prevPublisher)
  const [releaseYears, setReleaseYears] = React.useState<number[]>([
    release_year_from,
    release_year_to,
  ])
  const [releaseYearsDisplay, setReleaseYearsDisplay] = React.useState<
    number[]
  >([release_year_from, release_year_to])

  const [authorACValue, setAuthorACValue] = React.useState<string | null>(
    prevAuthor
  )
  const [publisherACValue, setPublisherACValue] = React.useState<string | null>(
    prevPublisher
  )

  const books = useBooksPerPage({
    page: prevPage,
    limit: booksPerPage,
    genre,
    author: prevAuthor,
    publisher: prevPublisher,
    release_year_from,
    release_year_to,
  })
  const authors = useBooksAuthors()
  const genres = useBooksGenres()
  const publishers = useBooksPublishers()

  const [, setSearchParams] = useSearchParams()

  const filterPublishersOptions = (
    options: AutocompleteOption[],
    { inputValue }: FilterOptionsState<AutocompleteOption>
  ) => {
    const terms = inputValue.split(' ')
    let sorted: AutocompleteOption[] = []
    if (!terms)
      sorted = matchSorter(options, inputValue, {
        keys: ['label'],
        threshold: matchSorter.rankings.WORD_STARTS_WITH,
      }).slice(0, 29)
    else
      sorted = terms
        .reduceRight(
          (results, term) =>
            matchSorter(results, term, {
              keys: ['label'],
              threshold: matchSorter.rankings.WORD_STARTS_WITH,
            }),
          options
        )
        .slice(0, 29)
    return [{ label: 'Wszystkie', value: '' }, ...sorted]
  }

  const filterAuthorsOptions = (
    options: AutocompleteOption[],
    { inputValue }: FilterOptionsState<AutocompleteOption>
  ) => {
    const terms = inputValue.split(' ')
    let sorted: AutocompleteOption[] = []
    if (!terms)
      sorted = matchSorter(options, inputValue, {
        keys: ['label'],
        threshold: matchSorter.rankings.WORD_STARTS_WITH,
      }).slice(0, 29)
    else
      sorted = terms
        .reduceRight(
          (results, term) =>
            matchSorter(results, term, {
              keys: ['label'],
              threshold: matchSorter.rankings.WORD_STARTS_WITH,
            }),
          options
        )
        .slice(0, 29)
    return [{ label: 'Wszyscy', value: '' }, ...sorted]
  }

  const onAuthorChange = (
    _: React.SyntheticEvent<Element, Event>,
    value: unknown
  ) => {
    if (value !== null) {
      setAuthor((value as AutocompleteOption).value)
    }
  }

  const onPublisherChange = (
    _: React.SyntheticEvent<Element, Event>,
    value: unknown
  ) => {
    if (value !== null) {
      setPublisher((value as AutocompleteOption).value)
    }
  }
  const handleReleaseYearsChange = (
    event: React.SyntheticEvent | Event,
    newValue: number | number[]
  ) => {
    if (event.type === 'input') return
    setReleaseYears(newValue as number[])
  }

  const handleReleaseYearsChangeDisplay = (
    event: React.SyntheticEvent | Event,
    newValue: number | number[]
  ) => {
    if (event.type === 'input') return
    setReleaseYearsDisplay(newValue as number[])
  }

  React.useEffect(() => {
    setSearchParams(
      {
        genre: genre as string,
        page: page.toString() as string,
        author: author as string,
        publisher: publisher as string,
        release_year_from: releaseYears[0].toString(),
        release_year_to: releaseYears[1].toString(),
      },
      { replace: true }
    )
  }, [genre, author, publisher, releaseYears])

  React.useEffect(() => {
    setPage(1)
  }, [genre, author, publisher, releaseYears])

  return (
    <>
      <Box sx={{ p: 2 }}>
        <CssBaseline />
        <FormControl variant="outlined" sx={{ width: 1 }}>
          <Grid
            container
            sx={{
              display: 'grid',
              gridAutoFlow: 'column',
              gap: 1,
            }}
          >
            <Grid item>
              <InputLabel id="select-genre-label">Gatunek</InputLabel>
              <Select
                labelId="select-genre-label"
                label="Gatunek"
                value={genre}
                onChange={(event) => {
                  setGenre(event.target.value as string)
                }}
                sx={{ width: 1 }}
              >
                <MenuItem value={''}>
                  <em>Wszystkie</em>
                </MenuItem>
                {genres.isSuccess ? (
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
            </Grid>
            <Autocomplete
              disablePortal
              id="authors"
              filterOptions={filterAuthorsOptions}
              value={null}
              inputValue={
                (authorACValue as string) === 'Wszyscy'
                  ? ''
                  : (authorACValue as string)
              }
              onInputChange={(_, value) => setAuthorACValue(value)}
              clearOnBlur={false}
              clearOnEscape={false}
              renderInput={(params) => <TextField {...params} label="Autor" />}
              options={
                authors.isSuccess
                  ? authors.data.authors
                      .filter((option) => option !== '')
                      .map((option) => ({
                        label: option,
                        value: option,
                      }))
                  : [{ label: 'Ładowanie', value: '' }]
              }
              readOnly={!authors.isSuccess}
              onChange={onAuthorChange}
              disableClearable={false}
            />
            <Autocomplete
              disablePortal
              id="publishers"
              filterOptions={filterPublishersOptions}
              value={null}
              inputValue={
                (publisherACValue as string) === 'Wszystkie'
                  ? ''
                  : (publisherACValue as string)
              }
              onInputChange={(_, value) => setPublisherACValue(value)}
              clearOnBlur={false}
              clearOnEscape={false}
              renderInput={(params) => (
                <TextField {...params} label="Wydawnictwo" />
              )}
              options={
                publishers.isSuccess
                  ? publishers.data.publishers
                      .filter((option) => option !== '')
                      .map((option) => ({
                        label: option,
                        value: option,
                      }))
                  : [{ label: 'Ładowanie', value: '' }]
              }
              readOnly={!publishers.isSuccess}
              onChange={onPublisherChange}
              disableClearable={false}
            />
          </Grid>
          <Typography id="non-linear-slider" gutterBottom sx={{ pt: 4 }}>
            {valueLabelFormat(releaseYears)}
          </Typography>
          <Slider
            getAriaLabel={() => 'Lata wydania'}
            value={releaseYearsDisplay}
            onChangeCommitted={handleReleaseYearsChange}
            onChange={handleReleaseYearsChangeDisplay}
            valueLabelDisplay="auto"
            min={min_release_year}
            max={max_release_year}
            sx={{ width: 1, pb: 2 }}
          />
        </FormControl>
      </Box>

      {books.isSuccess ? <BooksGrid books={books.data} /> : <Loading />}
    </>
  )
}

export default BooksGridWithFilters
