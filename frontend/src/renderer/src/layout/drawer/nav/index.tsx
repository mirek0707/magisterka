import List from '@mui/material/List'
import * as React from 'react'
import { LayoutDrawerNavConfig } from '/src/layout/drawer/nav/config'
import LayoutDrawerNavItem from '/src/layout/drawer/nav/item'
import { ListItemConfig } from '/src/layout/drawer/nav/types'

interface Props {
  open: boolean
}

const LayoutDrawerNav: React.FC<Props> = ({ open }) => {
  return (
    <List>
      {LayoutDrawerNavConfig.map((item: ListItemConfig) => (
        <LayoutDrawerNavItem open={open} key={item.name} {...item} />
      ))}
    </List>
  )
}

export default LayoutDrawerNav
