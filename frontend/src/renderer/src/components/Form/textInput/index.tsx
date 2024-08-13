import { TextField, TextFieldProps } from '@mui/material'
import * as React from 'react'
import { Controller } from 'react-hook-form'

type Props = TextFieldProps & {
  name: string
  label: string
}

const TextInput: React.FC<Props> = ({ name, label, ...textFieldProps }) => {
  return (
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
  )
}

export default TextInput
