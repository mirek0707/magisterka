import { createBrowserRouter, Navigate, Outlet } from 'react-router-dom'
import AppPage from 'src/application'
import LoginPage from 'src/auth/login'
import RegisterPage from 'src/auth/register'
import Layout from 'src/layout'
import BooksPage from 'src/pages/books'
import ErrorPage from 'src/pages/error'
import LibraryPage from 'src/pages/library'
import ProfilePage from 'src/pages/profile'
import { Routes } from 'src/routes'

import ProtectedRoute from './private'

export const BrowserRouter = createBrowserRouter([
  {
    path: Routes.HomeUrl(),
    element: <Navigate to="/app" />,
  },
  {
    path: Routes.AppUrl(),
    element: (
      <ProtectedRoute>
        <Layout>
          <Outlet />
        </Layout>
      </ProtectedRoute>
    ),
    children: [
      {
        path: Routes.AppUrl(),
        element: (
          <ProtectedRoute>
            <AppPage />
          </ProtectedRoute>
        ),
      },
      {
        path: Routes.ProfileUrl(),
        element: (
          <ProtectedRoute>
            <ProfilePage />
          </ProtectedRoute>
        ),
      },
      {
        path: Routes.BooksUrl(),
        element: (
          <ProtectedRoute>
            <BooksPage />
          </ProtectedRoute>
        ),
      },
      {
        path: Routes.LibraryUrl(),
        element: (
          <ProtectedRoute>
            <LibraryPage />
          </ProtectedRoute>
        ),
      },
      {
        path: `*`,
        element: (
          <ProtectedRoute>
            <ErrorPage />
          </ProtectedRoute>
        ),
      },
    ],
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
    element: <ErrorPage />,
  },
])
