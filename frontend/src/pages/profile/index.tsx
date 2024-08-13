import {
  Box,
  CssBaseline,
  Grid,
  List,
  ListItem,
  ListItemText,
  Typography,
} from '@mui/material'
import * as React from 'react'
import DeleteUserButton from 'src/components/deleteUser'
import ImportGRButton from 'src/components/importGR'
import ImportLCButton from 'src/components/importLC'
import { Loading } from 'src/components/loading'
import { useUserSession } from 'src/user/rquery'

import ErrorPage from '../error'

const ProfilePage: React.FC = () => {
  const user = useUserSession()

  if (user.isError || user.isIdle) {
    return <ErrorPage />
  }
  if (user.isLoading) {
    return <Loading />
  }

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <CssBaseline />
      <Box
        sx={{
          width: '100%',
          minWidth: '900px',
          maxWidth: '1600px',
        }}
      >
        <Grid container direction={'column'}>
          <Grid item>
            <Typography variant="h4">
              Profil użytkownika <em>{user.data.username}</em>
            </Typography>
          </Grid>
          <Grid
            item
            container
            direction="row"
            justifyContent="flex-start"
            alignItems="center"
          >
            <Grid item sx={{ p: 1, pl: 0 }}>
              <DeleteUserButton user_id={user.data.id} />
            </Grid>
          </Grid>
        </Grid>
        <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
          <ListItem>
            <ListItemText
              primary="Nazwa użytkownika"
              secondary={user.data.username}
            />
          </ListItem>
          <ListItem>
            <ListItemText primary="Adres e-mail" secondary={user.data.email} />
          </ListItem>
          <ListItem>
            <ListItemText
              primary="Rola"
              secondary={
                user.data.role === 'ADMIN' ? 'Administrator' : 'Użytkownik'
              }
            />
          </ListItem>
        </List>
        <Grid
          container
          direction="row"
          justifyContent="flex-start"
          alignItems="center"
        >
          <Grid item sx={{ p: 1, pl: 0 }}>
            <ImportLCButton />
          </Grid>
          <Grid item sx={{ p: 1, pl: 0 }}>
            <ImportGRButton />
          </Grid>
        </Grid>
      </Box>
    </Box>
  )
}

export default ProfilePage
