import NoAccountsIcon from '@mui/icons-material/NoAccounts'
import { Typography, Modal, Box, Grid, Button } from '@mui/material'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { useAuthSignOutAndRedirect } from '/src/auth/hooks'
import { deleteUser } from '/src/user/api'
interface Props {
  user_id: string
}

const DeleteUserButton: React.FC<Props> = ({ user_id }) => {
  const signOutAndRedirect = useAuthSignOutAndRedirect()
  const [open, setOpen] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => {
    setOpen(false)
  }
  const { handleSubmit } = useForm()
  const onSubmit = async () => {
    try {
      await deleteUser(user_id)
      signOutAndRedirect()
    } catch (e) {
      alert('Operacja nie powiodła się.')
    }
  }
  return (
    <>
      <Button
        onClick={handleOpen}
        variant="contained"
        startIcon={<NoAccountsIcon fontSize="large" />}
      >
        Usuń konto
      </Button>

      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Czy na pewno chcesz usunąć swoje konto?'}
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Utracisz bezpowrotnie swoje konto wraz z półkami. Czy chcesz
            kontynuować?
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit(onSubmit)}>
            <Grid
              container
              direction="row"
              justifyContent="flex-end"
              alignItems="center"
              columnSpacing={1}
              sx={{ p: 1, pt: 2 }}
            >
              <Grid item>
                <Button type="submit" variant="contained">
                  Usuń
                </Button>
              </Grid>
              <Grid item>
                <Button variant="contained" onClick={handleClose}>
                  Anuluj
                </Button>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Modal>
    </>
  )
}
export default DeleteUserButton

const style = {
  position: 'absolute' as const,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 430,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
}
