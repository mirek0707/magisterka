import * as React from 'react'
import { useNavigate } from 'react-router-dom'
import { Routes } from 'src/routes'
import queryClient from 'src/rquery/client'
import { createContext } from 'src/utils/context'

import {
  removePersistentAuthData,
  setPersistentAuthData,
} from '../localStorage'
import { AuthData } from '../types'

import PersistentAuthTokenLoader from './loader'

export type AuthContext = {
  signIn: (data: AuthData) => void
  signOut: () => Promise<unknown>
  data: AuthData | undefined
}

const [useAuthContext, Provider] = createContext<AuthContext>()

// should not be used directly; use auth/login/hooks instead!
export { useAuthContext }

type Props = {
  children: React.ReactNode
}

const AuthProvider: React.FC<Props> = ({ children }) => {
  const [data, setData] = React.useState<AuthData>()
  const navigate = useNavigate()

  const signIn = async (data: AuthData) => {
    queryClient.clear() // clear all query caches to avoid flash of other user's data
    setPersistentAuthData(data)
    setData(data)
    navigate(Routes.AppUrl())
  }

  const signOut = () => {
    return new Promise(() => {
      removePersistentAuthData()

      setData(undefined)

      queryClient.clear() // clear all query caches to avoid flash of other user's data
    })
  }

  return (
    <Provider value={{ signIn, signOut, data }}>
      <PersistentAuthTokenLoader>{children}</PersistentAuthTokenLoader>
    </Provider>
  )
}

export default AuthProvider
