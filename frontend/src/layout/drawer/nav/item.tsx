import { Tooltip } from '@mui/material'
import ListItem from '@mui/material/ListItem'
import ListItemButton from '@mui/material/ListItemButton'
import ListItemIcon from '@mui/material/ListItemIcon'
import ListItemText from '@mui/material/ListItemText'
import * as React from 'react'
import { NavLink } from 'react-router-dom'
import { ListItemProps } from 'src/layout/drawer/nav/types'

const LayoutDrawerNavItem: React.FC<ListItemProps> = ({
  open,
  name,
  path,
  icon,
}) => {
  return (
    <ListItem disablePadding sx={{ display: 'block' }}>
      <Tooltip title={open ? '' : name} placement="right">
        <ListItemButton
          component={NavLink}
          to={path}
          sx={{
            minHeight: 48,
            justifyContent: open ? 'initial' : 'center',
            px: 2.5,
          }}
        >
          <ListItemIcon
            sx={{
              minWidth: 0,
              mr: open ? 3 : 'auto',
              justifyContent: 'center',
            }}
          >
            {icon}
          </ListItemIcon>
          <ListItemText primary={name} sx={{ opacity: open ? 1 : 0 }} />
        </ListItemButton>
      </Tooltip>
    </ListItem>
  )
}

export default LayoutDrawerNavItem
