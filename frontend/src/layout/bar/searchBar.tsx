import SearchIcon from '@mui/icons-material/Search'
import InputBase from '@mui/material/InputBase'
import { styled, alpha } from '@mui/material/styles'
import * as React from 'react'
import { useNavigate, createSearchParams } from 'react-router-dom'
import { Routes } from 'src/routes'

const SearchBar: React.FC = () => {
  const navigate = useNavigate()
  const [searchInput, setSearchInput] = React.useState('')
  return (
    <Search>
      <SearchIconWrapper>
        <SearchIcon />
      </SearchIconWrapper>
      <StyledInputBase
        placeholder="Szukaj..."
        inputProps={{ 'aria-label': 'search' }}
        onChange={(e) => {
          setSearchInput(e.target.value)
        }}
        value={searchInput}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            const searchInputVal = searchInput
            setSearchInput('')
            navigate({
              pathname: Routes.SearchUrl(),
              search: createSearchParams({
                q: `${searchInputVal}`,
              }).toString(),
            })
          }
        }}
      />
    </Search>
  )
}

export default SearchBar

const Search = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  marginRight: theme.spacing(2),
  marginLeft: 0,
  width: '100%',
  [theme.breakpoints.up('sm')]: {
    marginLeft: theme.spacing(3),
    width: 'auto',
  },
}))

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}))

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
}))
