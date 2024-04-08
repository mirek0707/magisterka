import { createBrowserRouter, Navigate } from 'react-router-dom'

import ProtectedRoute from './private'

import AppPage from '@/app/'
import LoginPage from '@/auth/login'
import RegisterPage from '@/auth/register'
import ErrorPage from '@/pages/error'
import { Routes } from '@/routes'

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
