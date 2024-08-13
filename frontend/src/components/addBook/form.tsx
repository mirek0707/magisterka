import {
  Box,
  Checkbox,
  FormGroup,
  FormControlLabel,
  Button,
  Grid,
} from '@mui/material'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { patchAddBookToShelf, patchDelBookToShelf } from 'src/shelves/api'
import { Shelf } from 'src/shelves/types'

interface Props {
  isbn: string
  shelves: Shelf[]
  closeModal: () => void
}

interface CheckboxesValues {
  [key: string]: boolean
}

const AddBookForm: React.FC<Props> = ({ isbn, shelves, closeModal }) => {
  const { register, handleSubmit } = useForm()
  const onSubmit = async (data: CheckboxesValues) => {
    const keys = Object.keys(data)
    for (const shelf_id of keys) {
      const add = data[shelf_id]
      const shelf = shelves.find((shelf) => shelf._id === shelf_id)
      try {
        if (add && shelf && !shelf.books.includes(isbn)) {
          await patchAddBookToShelf(shelf_id, isbn)
        } else if (!add && shelf && shelf.books.includes(isbn)) {
          await patchDelBookToShelf(shelf_id, isbn)
        }
      } catch (e) {
        alert('Operacja nie powiodła się dla półki ' + shelf_id)
      }
    }
    closeModal()
    // alert('Operacja powiodła się')
  }
  return (
    <Box component="form" noValidate onSubmit={handleSubmit(onSubmit)}>
      <FormGroup sx={{ p: 1 }}>
        {shelves.map((item, index) => (
          <FormControlLabel
            key={index}
            label={item.name}
            control={
              <Checkbox
                defaultChecked={item.books.includes(isbn)}
                {...register(item._id)}
              />
            }
          />
        ))}
      </FormGroup>
      <Grid
        container
        direction="row"
        justifyContent="flex-end"
        alignItems="center"
        columnSpacing={1}
      >
        <Grid item>
          <Button type="submit" variant="contained">
            Zatwierdź
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={closeModal}>
            Anuluj
          </Button>
        </Grid>
      </Grid>
    </Box>
  )
}
export default AddBookForm
