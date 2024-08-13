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
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { postRegister } from '/src/auth/api'
import { Routes } from '/src/routes'

import { RegisterFormData, RegisterFormSchema } from '../schema'

export default function Register() {
  const navigate = useNavigate()
  const {
    register,
    handleSubmit,
    resetField,
    formState: { errors, touchedFields },
  } = useForm<RegisterFormData>({
    mode: 'onBlur',
    reValidateMode: 'onBlur',
    resolver: zodResolver(RegisterFormSchema),
    defaultValues: {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
    },
  })
  const onSubmit = async (data: RegisterFormData) => {
    try {
      const { username, email, password } = data
      const role = 'USER'

      await postRegister({ username, email, password, role })
      alert('Registration successful')
      navigate(Routes.LoginUrl(), { replace: true })
    } catch (e) {
      alert('Istnieje już konto z podaną nazwą użytkownika lub adresem e-mail')
    }
  }

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
          Rejestracja
        </Typography>
        <Box
          component="form"
          noValidate
          onSubmit={handleSubmit(onSubmit)}
          sx={{ mt: 3 }}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
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
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                id="email"
                label="Adres e-mail"
                autoComplete="email"
                {...register('email')}
                error={!!errors.email && touchedFields.email}
                helperText={errors.email?.message}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                label="Hasło"
                type="password"
                id="password"
                autoComplete="new-password"
                {...register('password')}
                error={!!errors.password && touchedFields.password}
                helperText={errors.password?.message}
                onChange={() => {
                  resetField('confirmPassword')
                }}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                label="Potwierdź hasło"
                type="password"
                id="confirmPassword"
                autoComplete="new-password"
                {...register('confirmPassword')}
                error={
                  !!errors.confirmPassword && touchedFields.confirmPassword
                }
                helperText={errors.confirmPassword?.message}
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Zarejestruj się
          </Button>
          <Grid container justifyContent="center">
            <Grid item>
              <Link href={Routes.LoginUrl()} variant="body2">
                {'Posiadasz już konto? Zaloguj się'}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  )
}
