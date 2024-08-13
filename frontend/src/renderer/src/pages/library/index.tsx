import { Box } from '@mui/material'
import * as React from 'react'
import AddShelfButton from '/src/components/addShelf'
import Library from '/src/components/library'
import { Loading } from '/src/components/loading'
import { useUserShelves } from '/src/shelves/rquery'
import { useUserSession } from '/src/user/rquery'

import ErrorPage from '../error'
const LibraryPage: React.FC = () => {
  const user = useUserSession()
  const shelves = useUserShelves(user.data?.id as string)
  const refetch = () => {
    shelves.refetch()
  }

  if (user.isError || user.isIdle || shelves.isError || shelves.isIdle) {
    return <ErrorPage />
  }
  if (user.isLoading || shelves.isLoading) {
    return <Loading />
  }

  return (
    <Box
      sx={{ flexDirection: 'column', alignItems: 'flex-start' }}
      className="flex flex-col items-center justify-center w-100 space-y-5"
    >
      <AddShelfButton refetch={refetch} />
      <Library shelves={shelves.data} refetch={refetch} />
    </Box>
  )
}

export default LibraryPage
