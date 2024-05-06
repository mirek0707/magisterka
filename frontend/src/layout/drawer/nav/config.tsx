import BookIcon from '@mui/icons-material/Book'
import HomeIcon from '@mui/icons-material/Home'
import LibraryBooksIcon from '@mui/icons-material/LibraryBooks'
import PageviewIcon from '@mui/icons-material/Pageview'
import PersonIcon from '@mui/icons-material/Person'
import { Routes } from 'src/routes'

import { ListItemConfig } from './types'

export const LayoutDrawerNavConfig: Array<ListItemConfig> = [
  {
    name: 'Strona główna',
    path: Routes.AppUrl(),
    icon: <HomeIcon />,
  },
  {
    name: 'Wyszukaj',
    path: Routes.SearchUrl(),
    icon: <PageviewIcon />,
  },
  {
    name: 'Katalog',
    path: Routes.BooksUrl(),
    icon: <BookIcon />,
  },
  {
    name: 'Biblioteczka',
    path: Routes.LibraryUrl(),
    icon: <LibraryBooksIcon />,
  },
  {
    name: 'Profil',
    path: Routes.ProfileUrl(),
    icon: <PersonIcon />,
  },
]
