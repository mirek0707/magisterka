import Divider from '@mui/material/Divider'
import MuiDrawer from '@mui/material/Drawer'
import { styled } from '@mui/material/styles'
import * as React from 'react'

import LayoutBar from '../bar'

import DrawerHeader from './header'
import LayoutDrawerNav from './nav'
import { openedMixin, closedMixin } from './transitions'

export const drawerWidth = 240

const LayoutDrawer: React.FC = () => {
  const [open, setOpen] = React.useState(false)

  const handleDrawerClose = () => {
    setOpen(false)
  }

  const handleDrawerOpen = () => {
    setOpen(true)
  }
  return (
    <>
      <LayoutBar open={open} handleDrawerOpen={handleDrawerOpen} />
      <StyledDrawer variant="permanent" open={open}>
        <DrawerHeader open={open} handleDrawerClose={handleDrawerClose} />
        <Divider />
        <LayoutDrawerNav open={open} />
        <Divider />
      </StyledDrawer>
    </>
  )
}

export default LayoutDrawer

const StyledDrawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: 'nowrap',
  boxSizing: 'border-box',
  ...(open && {
    ...openedMixin(theme),
    '& .MuiDrawer-paper': openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    '& .MuiDrawer-paper': closedMixin(theme),
  }),
}))
