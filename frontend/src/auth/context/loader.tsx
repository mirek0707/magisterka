import LoopIcon from '@mui/icons-material/Loop'
import * as React from 'react'

import { getPersistentAuthData } from '../localStorage'

import { useAuthContext } from '.'

type Props = {
  children: React.ReactNode
}

const PersistentAuthTokenLoader: React.FC<Props> = ({ children }) => {
  const [loading, setLoading] = React.useState(true)

  const { signIn } = useAuthContext()

  React.useEffect(() => {
    const data = getPersistentAuthData()

    if (data) signIn(data)

    setLoading(false)
  }, [])

  return <>{loading ? <LoopIcon /> : children}</>
}

export default PersistentAuthTokenLoader
