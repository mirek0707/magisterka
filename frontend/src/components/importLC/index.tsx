import { zodResolver } from '@hookform/resolvers/zod'
import { Typography, Modal, Box, Grid, Button, TextField } from '@mui/material'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { putImportLC } from 'src/shelves/api'

import { Loading } from '../loading'

import { ImportLCFormData, ImportLCFormSchema } from './schema'

const ImportLCButton: React.FC = () => {
  const [open, setOpen] = React.useState(false)
  const [loading, setLoading] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => setOpen(false)
  const {
    register,
    handleSubmit,
    formState: { errors, touchedFields },
  } = useForm<ImportLCFormData>({
    mode: 'onBlur',
    reValidateMode: 'onBlur',
    resolver: zodResolver(ImportLCFormSchema),
    defaultValues: {
      url: '',
    },
  })
  const onSubmit = async (data: ImportLCFormData) => {
    try {
      setLoading(true)
      await putImportLC(data)
      setLoading(false)
      alert('Dane zaimportowane pomyślnie')
      handleClose()
    } catch (e) {
      setLoading(false)
      alert('Operacja nie powiodła się')
    }
  }
  return (
    <>
      <Button variant="contained" onClick={handleOpen}>
        Importuj dane z lubimyczytac.pl
      </Button>
      <Modal
        open={loading}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Loading />
        </Box>
      </Modal>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Importuj dane z lubimyczytac.pl'}
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Importuj swoją biblioteczkę z lubimyczytac.pl. Aby to zrobić,
            wygeneruj link do swojej biblioteczki i wklej go poniżej. Pamiętaj,
            aby ustawić widoczność swojego profilu na publiczną.
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit(onSubmit)}>
            <Box sx={{ display: 'flex', pt: 2 }}>
              <TextField
                required
                fullWidth
                id="outlined-basic"
                label="Adres URL twojego profilu"
                variant="outlined"
                {...register('url')}
                sx={{ flexGrow: 1 }}
                error={!!errors.url && touchedFields.url}
                helperText={errors.url?.message}
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
                  Importuj
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
export default ImportLCButton

const style = {
  position: 'absolute' as const,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 600,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
}
