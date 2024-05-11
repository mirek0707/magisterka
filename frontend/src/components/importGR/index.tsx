import AttachFileIcon from '@mui/icons-material/AttachFile'
import {
  Typography,
  Modal,
  Box,
  Grid,
  Button,
  InputAdornment,
} from '@mui/material'
import { MuiFileInput } from 'mui-file-input'
import * as React from 'react'
import { useForm, Controller, FieldValues } from 'react-hook-form'
import { putImportGR } from 'src/shelves/api'

import { Loading } from '../loading'

const ImportLCButton: React.FC = () => {
  const [open, setOpen] = React.useState(false)
  const [loading, setLoading] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => setOpen(false)
  const { control, handleSubmit } = useForm()
  const onSubmit = async (data: FieldValues) => {
    try {
      setLoading(true)
      const formData = new FormData()
      formData.append('file', data.file)
      await putImportGR(formData)
      setLoading(false)
      handleClose()
      alert('Dane zaimportowane pomyślnie')
    } catch (e) {
      setLoading(false)
      alert('Operacja nie powiodła się')
    }
  }
  return (
    <>
      <Button variant="contained" onClick={handleOpen}>
        Importuj dane z goodreads.com
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
            {'Importuj dane z goodreads.com'}
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Importuj swoją biblioteczkę z goodreads.com. Aby to zrobić, wejdź w
            zakładkę 'My Books', kliknij 'Import and export' oraz 'Export
            Library'. Pobrany plik umieść poniżej.
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit(onSubmit)}>
            <Box sx={{ display: 'flex', pt: 2 }}>
              <Controller
                name="file"
                control={control}
                render={({ field, fieldState }) => (
                  <MuiFileInput
                    {...field}
                    helperText={
                      fieldState.invalid
                        ? 'Nieprawidłowy plik'
                        : 'Dodaj plik z goodreads.com'
                    }
                    error={fieldState.invalid}
                    sx={{ flexGrow: 1 }}
                    inputProps={{ accept: '.csv' }}
                    getInputText={(value) => (value ? value.name : '')}
                    label="Plik"
                    InputProps={{
                      startAdornment: (
                        <InputAdornment position="start">
                          <AttachFileIcon />
                        </InputAdornment>
                      ),
                    }}
                  />
                )}
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
