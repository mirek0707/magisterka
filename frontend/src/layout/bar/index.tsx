import ArrowBackIcon from '@mui/icons-material/ArrowBack'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import MenuIcon from '@mui/icons-material/Menu'
import { Grid, Tooltip } from '@mui/material'
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar'
import IconButton from '@mui/material/IconButton'
import { styled } from '@mui/material/styles'
import Toolbar from '@mui/material/Toolbar'
import * as React from 'react'
import { useNavigate } from 'react-router-dom'
import { drawerWidth } from 'src/layout/drawer'

import SearchBar from './searchBar'
import UserMenu from './userMenu'

interface LayoutBarProps extends MuiAppBarProps {
  open?: boolean
  handleDrawerOpen: () => void
}

const LayoutBar: React.FC<LayoutBarProps> = ({ open, handleDrawerOpen }) => {
  const navigate = useNavigate()
  return (
    <AppBar position="fixed" open={open}>
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          onClick={handleDrawerOpen}
          edge="start"
          sx={{
            marginRight: 5,
            borderRadius: 0,

            ...(open && { display: 'none' }),
          }}
        >
          <MenuIcon />
        </IconButton>
        <Grid
          container
          spacing={2}
          sx={{
            flexGrow: 1,
          }}
        >
          <Grid item>
            <Tooltip enterDelay={400} title="Wróć">
              <IconButton
                onClick={() => {
                  navigate(-1)
                }}
                color="inherit"
                edge="start"
                sx={{
                  borderRadius: 0,
                }}
              >
                <ArrowBackIcon />
              </IconButton>
            </Tooltip>
          </Grid>
          <Grid item>
            <Tooltip enterDelay={400} title="Do przodu">
              <IconButton
                onClick={() => {
                  navigate(1)
                }}
                color="inherit"
                edge="start"
                sx={{
                  borderRadius: 0,
                }}
              >
                <ArrowForwardIcon />
              </IconButton>
            </Tooltip>
          </Grid>
        </Grid>
        <SearchBar />
        <UserMenu />
      </Toolbar>
    </AppBar>
  )
}

export default LayoutBar

interface AppBarProps extends MuiAppBarProps {
  open?: boolean
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}))
