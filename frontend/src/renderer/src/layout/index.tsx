import { Box, CssBaseline } from '@mui/material'
import * as React from 'react'

import LayoutDrawer from './drawer'
import { Header } from './drawer/header'

type Props = {
  children: React.ReactNode
}

const Layout: React.FC<Props> = ({ children }) => {
  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <LayoutDrawer />
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Header />
        <main>{children}</main>
      </Box>
    </Box>
  )
}

export default Layout
