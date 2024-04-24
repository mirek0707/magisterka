import { zodResolver } from '@hookform/resolvers/zod'
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Grid'
import Link from '@mui/material/Link'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { useLocation, useNavigate } from 'react-router-dom'
import { postLogin } from 'src/auth/api'
import { useAuthContext } from 'src/auth/context'
import { useIsAuthenticated } from 'src/auth/hooks'
import { Routes } from 'src/routes'

import { LoginFormData, LoginFormSchema } from '../schema'

export default function Login() {
  const { signIn } = useAuthContext()
  const isAuthenticated = useIsAuthenticated()
  const navigate = useNavigate()
  const location = useLocation()

  const {
    register,
    handleSubmit,
    formState: { errors, touchedFields },
  } = useForm<LoginFormData>({
    mode: 'onBlur',
    reValidateMode: 'onBlur',
    resolver: zodResolver(LoginFormSchema),
    defaultValues: {
      username: '',
      password: '',
    },
  })
  const onSubmit = async (data: LoginFormData) => {
    try {
      const response = await postLogin(data)
      signIn({
        token: response.access_token,
      })
    } catch (e) {
      alert('Login failed')
    }
  }

  React.useEffect(() => {
    if (isAuthenticated) {
      const redirectUrl = location.state?.from || Routes.HomeUrl()
      navigate(redirectUrl, { replace: true })
    }
  }, [isAuthenticated])

  return (
    <Container
      component="main"
      maxWidth="xs"
      sx={{
        display: 'flex',
        flexDirection: 'column',
        height: '100vh',
        justifyContent: 'center',
      }}
    >
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{ mb: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Logowanie
        </Typography>
        <Box
          component="form"
          onSubmit={handleSubmit(onSubmit)}
          noValidate
          sx={{ mt: 1 }}
        >
          <TextField
            autoComplete="username"
            required
            fullWidth
            id="username"
            label="Nazwa użytkownika"
            autoFocus
            {...register('username')}
            error={!!errors.username && touchedFields.username}
            helperText={errors.username?.message}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            label="Hasło"
            type="password"
            id="password"
            autoComplete="current-password"
            {...register('password')}
            error={!!errors.password && touchedFields.password}
            helperText={errors.password?.message}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Zaloguj się
          </Button>
          <Grid container justifyContent={'center'}>
            <Grid item>
              <Link href={Routes.RegisterUrl()} variant="body2">
                {'Nie posiadasz jeszcze konta? Zarejestruj się'}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  )
}
