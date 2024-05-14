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
import { deleteShelf } from 'src/shelves/api'

interface Props {
  shelf_id: string
  default_shelf: boolean
  refetch: () => void
}

const DeleteShelfButton: React.FC<Props> = ({
  shelf_id,
  default_shelf,
  refetch,
}) => {
  const [open, setOpen] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => {
    setOpen(false)
  }
  const { handleSubmit } = useForm()
  const onSubmit = async () => {
    try {
      await deleteShelf(shelf_id)
      handleClose()
      refetch()
    } catch (e) {
      alert('Operacja nie powiodła się.')
    }
  }
  return (
    <>
      {default_shelf ? (
        <Tooltip
          title="Domyślna półka nie może zostać usunięta!"
          placement="bottom"
        >
          <span>
            <IconButton
              onClick={handleOpen}
              sx={{
                p: 0,
                borderRadius: 1,
              }}
              disabled
            >
              <DeleteForeverIcon fontSize="large" />
            </IconButton>
          </span>
        </Tooltip>
      ) : (
        <Tooltip title="Usuń półkę" placement="bottom">
          <IconButton
            onClick={handleOpen}
            sx={{
              p: 0,
              borderRadius: 1,
              '&:hover': {
                transform: 'scale(1.1)',
              },
            }}
            color="inherit"
          >
            <DeleteForeverIcon color="primary" fontSize="large" />
          </IconButton>
        </Tooltip>
      )}
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Czy na pewno chcesz usunąć półkę?'}
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
export default DeleteShelfButton

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
