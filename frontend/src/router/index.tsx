import { createBrowserRouter, Navigate } from 'react-router-dom'
import AppPage from 'src/application'
import LoginPage from 'src/auth/login'
import RegisterPage from 'src/auth/register'
import ErrorPage from 'src/pages/error'
import { Routes } from 'src/routes'

import ProtectedRoute from './private'

export const BrowserRouter = createBrowserRouter([
  {
    path: Routes.AppUrl(),
    element: (
      <ProtectedRoute>
        <AppPage />
      </ProtectedRoute>
    ),
  },
  {
    path: Routes.HomeUrl(),
    element: <Navigate to="/app" />,
  },
  {
    path: Routes.LoginUrl(),
    element: <LoginPage />,
  },
  {
    path: Routes.RegisterUrl(),
    element: <RegisterPage />,
  },
  {
    path: `*`,
    element: (
      <ProtectedRoute>
        <ErrorPage />
      </ProtectedRoute>
    ),
  },
])
