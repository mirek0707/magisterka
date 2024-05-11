import DeleteForeverIcon from '@mui/icons-material/DeleteForever'
import {
  Typography,
  Modal,
  Box,
  IconButton,
  Tooltip,
  Grid,
  Button,
} from '@mui/material'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { deleteBook } from 'src/books/api'
import { Routes } from 'src/routes'
interface Props {
  isbn: string
}

const DeleteBookButton: React.FC<Props> = ({ isbn }) => {
  const navigate = useNavigate()
  const [open, setOpen] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => {
    setOpen(false)
  }
  const { handleSubmit } = useForm()
  const onSubmit = async () => {
    try {
      await deleteBook(isbn)
    } catch (e) {
      alert('Operacja nie powiodła się.')
    }
    navigate(Routes.AppUrl())
  }
  return (
    <>
      <Tooltip title="Usuń książkę" placement="bottom">
        <IconButton
          onClick={handleOpen}
          sx={{
            p: 0,
            borderRadius: 1,
            backgroundColor: 'text.primary',
            '&:hover': {
              backgroundColor: 'text.primary',
              transform: 'scale(1.2)',
            },
          }}
          color="inherit"
        >
          <DeleteForeverIcon color="primary" fontSize="large" />
        </IconButton>
      </Tooltip>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Czy na pewno chcesz usunąć książkę?'}
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
export default DeleteBookButton

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
