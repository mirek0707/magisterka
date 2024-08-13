import * as React from 'react'
import { Navigate } from 'react-router-dom'
import { useIsAuthenticated } from 'src/auth/hooks'
import { Routes } from 'src/routes'

type Props = {
  children: React.ReactElement
}

const ProtectedRoute: React.FC<Props> = ({ children }) => {
  const isAuthenticated = useIsAuthenticated()

  if (isAuthenticated) return children

  return <Navigate to={Routes.LoginUrl()} replace />
}

export default ProtectedRoute
