import { zodResolver } from '@hookform/resolvers/zod'
import {
  Box,
  Button,
  CssBaseline,
  Divider,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Typography,
} from '@mui/material'
import dayjs from 'dayjs'
import duration from 'dayjs/plugin/duration'
import { useForm, useFieldArray, Controller } from 'react-hook-form'
import { addBook } from 'src/books/api'
import { useBooksGenres } from 'src/books/rquery'
import { AddBookRequest } from 'src/books/types'
import Form from 'src/components/Form'
import DateInput from 'src/components/Form/dateInput'
import NumberInput from 'src/components/Form/numberInput'
import TextInput from 'src/components/Form/textInput'
import { Loading } from 'src/components/loading'
import { styled } from 'styled-components'

import ErrorPage from '../error'

import { AddBookFormSchema } from './schema'

dayjs.extend(duration)
const AddBookPage = () => {
  const methods = useForm({
    mode: 'onBlur',
    reValidateMode: 'onBlur',
    resolver: zodResolver(AddBookFormSchema),
    defaultValues: {
      title: '',
      author: [{ value: '' }],
      pages: 0,
      isbn: '',
      publisher: '', //null
      original_title: '', //null
      release_date: null,
      polish_release_date: null,
      release_year: 0,
      img_src: '',
      description: '', //null
      genre: 'albumy', //null
    },
  })
  const {
    register,
    handleSubmit,
    control,
    reset,
    // formState: { errors, touchedFields },
  } = methods

  const { fields, append, remove } = useFieldArray({
    control,
    name: 'author',
  })

  const genres = useBooksGenres()
  if (genres.isError || genres.isIdle) {
    return <ErrorPage />
  }
  if (genres.isLoading) {
    return <Loading />
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onSubmit = async (data: any) => {
    // console.log(data)
    const book: AddBookRequest = {
      title: data.title,
      author: data.author.map((author: { value: string }) => author.value),
      pages: data.pages === 0 ? null : data.pages,
      isbn: data.isbn,
      publisher: data.publisher,
      original_title: data.original_title,
      release_date:
        data.release_date === null ? null : data.release_date.hour(12).toDate(),
      release_year: data.release_year === 0 ? null : data.release_year,
      polish_release_date:
        data.polish_release_date === null
          ? null
          : data.polish_release_date.hour(12).toDate(),
      img_src: data.img_src === '' ? null : [data.img_src],
      genre: data.genre,
      description: data.description,
    }
    // console.log(book)
    try {
      await addBook(book)
      reset()
      alert('Dodano książkę')
    } catch (e) {
      alert('Nie udało się dodać książki')
    }
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
            <Typography variant="h4">Dodaj nową książkę</Typography>
          </Grid>
          <Grid item className="p-3">
            <Divider sx={{ color: 'success.dark' }} />
          </Grid>
          <Grid item>
            <StyledForm methods={methods} onSubmit={handleSubmit(onSubmit)}>
              <TextInput name="isbn" label="ISBN" required />
              <TextInput name="title" label="Tytuł" required />
              <NumberInput
                name="pages"
                label="Liczba stron"
                required={false}
                title="Jeżli nie masz tej informacji pozostaw 0"
              />
              <TextInput name="publisher" label="Wydawca" required={false} />
              <TextInput
                name="original_title"
                label="Oryginalny tytuł"
                required={false}
              />
              <DateInput
                name="release_date"
                label="Data wydania"
                minDate={dayjs(1970)}
                maxDate={dayjs().add(dayjs.duration({ years: 5 }))}
              />
              <NumberInput
                name="release_year"
                label="Rok wydania"
                required={false}
                title="Jeżli nie masz tej informacji pozostaw 0"
              />
              <DateInput
                name="polish_release_date"
                label="Polska data wydania"
                minDate={dayjs(1970)}
                maxDate={dayjs().add(dayjs.duration({ years: 5 }))}
              />
              <TextInput
                name="img_src"
                label="Link do zdjęcia okładki"
                required={false}
              />
              <TextInput
                name="description"
                label="Opis"
                multiline
                minRows={4}
                maxRows={10}
                required={false}
              />
              <InputLabel id="select-genre-label">Gatunek</InputLabel>
              <Select
                labelId="select-genre-label"
                // name="genre"
                defaultValue={'albumy'}
                sx={{ width: 1 }}
                {...register('genre')}
              >
                {genres.data.genres.map((item: string, index: number) => {
                  if (item !== '')
                    return (
                      <MenuItem key={index} value={item}>
                        {item}
                      </MenuItem>
                    )
                })}
              </Select>
              <>
                <ul>
                  {fields.map((item, index) => {
                    return (
                      <li key={item.id}>
                        <Controller
                          name={`author.${index}.value`}
                          control={control}
                          render={({ field, fieldState: { error } }) => (
                            <TextField
                              {...field}
                              label={'Autor'}
                              error={!!error}
                              helperText={error?.message}
                            />
                          )}
                        />
                        <button type="button" onClick={() => remove(index)}>
                          Delete
                        </button>
                      </li>
                    )
                  })}
                </ul>
                <section>
                  <button
                    type="button"
                    onClick={() => {
                      append({ value: '' })
                    }}
                  >
                    append
                  </button>
                </section>
              </>
              <Button type="submit">Dodaj</Button>
            </StyledForm>
          </Grid>
        </Grid>
      </Box>
    </Box>
  )
}

export default AddBookPage

const StyledForm = styled(Form)`
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 1.5rem;
` as typeof Form
