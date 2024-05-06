import { createBrowserRouter, Navigate, Outlet } from 'react-router-dom'
import AppPage from 'src/application'
import LoginPage from 'src/auth/login'
import RegisterPage from 'src/auth/register'
import Layout from 'src/layout'
import BookPage from 'src/pages/book'
import BooksPage from 'src/pages/books'
import ErrorPage from 'src/pages/error'
import LibraryPage from 'src/pages/library'
import ProfilePage from 'src/pages/profile'
import SearchPage from 'src/pages/search'
import Providers from 'src/providers'
import { Routes } from 'src/routes'

import ProtectedRoute from './private'

export const BrowserRouter = createBrowserRouter([
  {
    path: Routes.HomeUrl(),
    element: <Navigate to={Routes.AppUrl()} replace />,
  },
  {
    path: Routes.HomeUrl(),
    element: (
      <Providers>
        <Outlet />
      </Providers>
    ),
    children: [
      {
        path: Routes.AppUrl(),
        element: (
          <Layout>
            <Outlet />
          </Layout>
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
            path: Routes.SearchUrl(),
            element: (
              <ProtectedRoute>
                <SearchPage />
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
            path: Routes.BookUrl(':isbn'),
            element: (
              <ProtectedRoute>
                <BookPage />
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
    ],
  },
  {
    path: `*`,
    element: <ErrorPage />,
  },
])
