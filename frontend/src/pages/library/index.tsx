import * as React from 'react'
import Library from 'src/components/library'
import { Loading } from 'src/components/loading'
import { useUserShelves } from 'src/shelves/rquery'
import { useUserSession } from 'src/user/rquery'

import ErrorPage from '../error'
const LibraryPage: React.FC = () => {
  const user = useUserSession()
  const shelves = useUserShelves(user.data?.id as string)

  if (user.isError || user.isIdle || shelves.isError || shelves.isIdle) {
    return <ErrorPage />
  }
  if (user.isLoading || shelves.isLoading) {
    return <Loading />
  }

  return (
    <div className="flex flex-col items-center justify-center w-100 space-y-5">
      <Library shelves={shelves.data} />
    </div>
  )
}

export default LibraryPage
