import { Box, CssBaseline, Divider, Typography } from '@mui/material'
import * as React from 'react'
import { useParams } from 'react-router-dom'
import { Loading } from 'src/components/loading'
import ErrorPage from 'src/pages/error'
import { useShelf } from 'src/shelves/rquery'
import { useUserSession } from 'src/user/rquery'

import BooksOnShelf from './books'
const ShelfPage: React.FC = () => {
  const { shelf_id = '' } = useParams()
  const user = useUserSession()
  const shelf = useShelf(user.data?.id as string, shelf_id)

  if (user.isError || user.isIdle || shelf.isError || shelf.isIdle) {
    return <ErrorPage />
  }
  if (user.isLoading || shelf.isLoading) {
    return <Loading />
  }
  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <CssBaseline />
      <Box
        sx={{
          width: '100%',
          minWidth: '900px',
          maxWidth: '1600px',
        }}
      >
        <Typography variant="h4">
          Półka <em>{shelf.data.name}</em>
        </Typography>
        <Divider sx={{ color: 'success.dark', m: 2 }} />
        <BooksOnShelf isbns={shelf.data.books} />
      </Box>
    </Box>
  )
}

export default ShelfPage
