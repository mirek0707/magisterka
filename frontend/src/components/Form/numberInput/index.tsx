import { TextField, TextFieldProps } from '@mui/material'
import * as React from 'react'
import { Controller } from 'react-hook-form'

type Props = Omit<TextFieldProps, 'type'> & {
  name: string
  label: string
}

const NumberInput: React.FC<Props> = ({ name, label, ...textFieldProps }) => {
  return (
    <Controller
      name={name}
      render={({
        field: { onChange, onBlur, value },
        fieldState: { error },
      }) => (
        <TextField
          onChange={(event) => {
            onChange(
              event.target.value === '' ? '' : parseInt(event.target.value)
            )
          }}
          onBlur={onBlur}
          value={value}
          label={label}
          type="number"
          error={!!error}
          helperText={error?.message}
          {...textFieldProps}
        />
      )}
    />
  )
}

export default NumberInput
