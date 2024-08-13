import { TextField, TextFieldProps } from '@mui/material'
import * as React from 'react'
import {
  useFieldArray,
  Controller,
  Control,
  FieldValues,
} from 'react-hook-form'
import { AddBookFormData } from '/src/pages/addBook/schema'

type Props = TextFieldProps & {
  name: string
  label: string
  control: Control<FieldValues, AddBookFormData>
}
const ArrayInput: React.FC<Props> = ({
  name,
  label,
  control,
  ...textFieldProps
}) => {
  const { fields, append, remove } = useFieldArray({
    control,
    name: name,
  })

  return (
    <>
      <ul>
        {fields.map((item, index) => {
          return (
            <li key={item.id}>
              <Controller
                name={name}
                render={({
                  field: { onChange, onBlur, value },
                  fieldState: { error },
                }) => (
                  <TextField
                    onChange={onChange}
                    onBlur={onBlur}
                    value={value}
                    label={label}
                    error={!!error}
                    helperText={error?.message}
                    {...textFieldProps}
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
            append({ firstName: 'appendBill', lastName: 'appendLuo' })
          }}
        >
          append
        </button>
      </section>
    </>
  )
}

export default ArrayInput
