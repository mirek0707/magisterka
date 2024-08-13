import { zodResolver } from '@hookform/resolvers/zod'
import { Typography, Modal, Box, Grid, Button, TextField } from '@mui/material'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { addShelf } from '/src/shelves/api'
import { AddShelfReq } from '/src/shelves/types'

import { ImportAddBookFormData, ImportAddBookFormSchema } from './schema'

interface Props {
  refetch: () => void
}

const AddShelfButton: React.FC<Props> = ({ refetch }) => {
  const [open, setOpen] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => {
    setOpen(false)
  }
  const {
    register,
    handleSubmit,
    formState: { errors, touchedFields },
  } = useForm<ImportAddBookFormData>({
    mode: 'onBlur',
    reValidateMode: 'onBlur',
    resolver: zodResolver(ImportAddBookFormSchema),
    defaultValues: {
      name: '',
    },
  })
  const onSubmit = async (data: ImportAddBookFormData) => {
    try {
      const reqData: AddShelfReq = { name: data.name }
      await addShelf(reqData)
      handleClose()
      refetch()
    } catch (e) {
      alert('Operacja nie powiodła się')
    }
  }
  return (
    <>
      <Button variant="contained" onClick={handleOpen}>
        Dodaj nową półkę
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Dodawanie nowej półki'}
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit(onSubmit)}>
            <Box sx={{ display: 'flex', pt: 2 }}>
              <TextField
                required
                fullWidth
                id="outlined-basic"
                label="Nazwa nowej półki"
                variant="outlined"
                {...register('name')}
                sx={{ flexGrow: 1 }}
                error={!!errors.name && touchedFields.name}
                helperText={errors.name?.message}
              />
            </Box>
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
                  Dodaj
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
export default AddShelfButton

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
