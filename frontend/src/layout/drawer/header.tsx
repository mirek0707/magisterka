import ChevronLeftIcon from '@mui/icons-material/ChevronLeft'
import IconButton from '@mui/material/IconButton'
import { styled } from '@mui/material/styles'
import * as React from 'react'

interface DrawerHeaderProps {
  open: boolean
  handleDrawerClose: () => void
}
const DrawerHeader: React.FC<DrawerHeaderProps> = ({
  open,
  handleDrawerClose,
}) => {
  return (
    <Header>
      <IconButton
        color="inherit"
        aria-label="close drawer"
        onClick={handleDrawerClose}
        sx={{
          ...(!open && { display: 'none' }),
        }}
      >
        <ChevronLeftIcon />
      </IconButton>
    </Header>
  )
}

export default DrawerHeader

export const Header = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
}))
