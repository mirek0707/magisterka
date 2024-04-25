import AccountCircle from '@mui/icons-material/AccountCircle'
import { IconButton, Menu, MenuItem, Tooltip, Typography } from '@mui/material'
import Box from '@mui/material/Box'
import * as React from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthSignOutAndRedirect } from 'src/auth/hooks'
import { Routes } from 'src/routes'

type MenuItemConfig = {
  name: string
  onClick: () => void
}

const UserMenu: React.FC = () => {
  const navigate = useNavigate()
  const signOutAndRedirect = useAuthSignOutAndRedirect()
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(
    null
  )

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget)
  }

  const handleCloseUserMenu = () => {
    setAnchorElUser(null)
  }
  const LayoutDrawerNavConfig: Array<MenuItemConfig> = [
    {
      name: 'Profil',
      onClick: () => navigate(Routes.ProfileUrl()),
    },
    {
      name: 'Wyloguj',
      onClick: () => signOutAndRedirect(),
    },
  ]

  return (
    <Box sx={{ flexGrow: 0 }}>
      <Tooltip title="Open settings">
        <IconButton
          onClick={handleOpenUserMenu}
          sx={{ p: 0 }}
          size="large"
          color="inherit"
        >
          <AccountCircle />
        </IconButton>
      </Tooltip>
      <Menu
        sx={{ mt: '45px' }}
        id="menu-appbar"
        anchorEl={anchorElUser}
        anchorOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        keepMounted
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        open={Boolean(anchorElUser)}
        onClose={handleCloseUserMenu}
        disableScrollLock={true}
      >
        {LayoutDrawerNavConfig.map((item, index) => (
          <MenuItem key={index} onClick={item.onClick}>
            <Typography textAlign="center">{item.name}</Typography>
          </MenuItem>
        ))}
      </Menu>
    </Box>
  )
}

export default UserMenu
