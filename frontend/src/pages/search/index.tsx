import {
  Divider,
  FormControlLabel,
  Grid,
  Switch,
  TextField,
  Tooltip,
} from '@mui/material'
import Box from '@mui/material/Box'
import * as React from 'react'
import { createSearchParams, useLocation, useNavigate } from 'react-router-dom'
import { Routes } from 'src/routes'

import SearchDef from './searchDef'
import SearchFts from './searchFts'

const SearchPage = () => {
  const location = useLocation()
  const navigate = useNavigate()

  const query = React.useMemo(
    () => new URLSearchParams(location.search),
    [location.search]
  )
  const searchInput = query.get('q') || ''
  const page = parseInt(query.get('page') || '1', 10)
  const fts = parseInt(query.get('fts') || '0', 10)

  const [isFts, setIsFts] = React.useState<boolean>(fts !== 0)
  const [currentInput, setCurrentInput] = React.useState<string>(searchInput)

  React.useEffect(() => {
    const newSearchInput = query.get('q') || ''

    setCurrentInput(newSearchInput)
  }, [query])

  const [isValid, setIsValid] = React.useState(false)

  React.useEffect(() => {
    setIsValid(currentInput.length > 2)
  }, [currentInput])

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <Grid container spacing={5} justifyContent={'center'}>
        <Grid item>
          <Tooltip title="Pełne wyszukiwanie polega na przeprowadzeniu wyszukiwania pełnotekstowego na tytułach, autorach, wydawnictwach oraz opisach książek. Może wydłużyć czas wyszukiwania!">
            <FormControlLabel
              control={
                <Switch
                  checked={isFts}
                  value={isFts}
                  onChange={() => {
                    setIsFts(!isFts)
                  }}
                />
              }
              label="Pełne wyszukiwanie"
              labelPlacement="bottom"
            />
          </Tooltip>
        </Grid>
        <Grid item>
          <TextField
            id="book-search-input"
            label="Szukaj..."
            variant="outlined"
            value={currentInput}
            error={!isValid}
            onChange={(e) => {
              setCurrentInput(e.target.value)
            }}
            helperText={!isValid ? 'Wpisz przynajmniej 3 znaki' : ''}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && isValid) {
                const searchInputVal = currentInput
                navigate({
                  pathname: Routes.SearchUrl(),
                  search: createSearchParams({
                    q: `${searchInputVal}`,
                    fts: `${isFts ? 1 : 0}`,
                  }).toString(),
                })
              }
            }}
          />
        </Grid>
      </Grid>

      {searchInput !== '' ? (
        <>
          <Divider sx={{ color: 'success.dark', m: 2 }} />
          {fts ? (
            <SearchFts query={query} searchInput={searchInput} page={page} />
          ) : (
            <SearchDef query={query} searchInput={searchInput} page={page} />
          )}
        </>
      ) : (
        <></>
      )}
    </Box>
  )
}

export default SearchPage
