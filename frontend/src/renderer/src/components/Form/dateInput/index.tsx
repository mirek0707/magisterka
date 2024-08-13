import { LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { DatePicker } from '@mui/x-date-pickers/DatePicker'
import { plPL } from '@mui/x-date-pickers/locales'
import dayjs from 'dayjs'
import * as React from 'react'
import { Controller } from 'react-hook-form'
import 'dayjs/locale/pl'

type Props = {
  name: string
  label: string
  minDate: dayjs.Dayjs
  maxDate: dayjs.Dayjs
}
const DateInput: React.FC<Props> = ({
  name,
  label,
  minDate,
  maxDate,
  ...datePickerProps
}) => {
  return (
    <Controller
      name={name}
      render={({ field: { value, onChange }, fieldState: { error } }) => (
        <LocalizationProvider
          localeText={
            plPL.components.MuiLocalizationProvider.defaultProps.localeText
          }
          dateAdapter={AdapterDayjs}
        >
          <DatePicker
            label={label}
            format="YYYY-MM-DD"
            value={value}
            onChange={onChange}
            minDate={minDate}
            maxDate={maxDate}
            slotProps={{
              textField: {
                error: !!error,
                helperText: error?.message,
              },
            }}
            {...datePickerProps}
          />
        </LocalizationProvider>
      )}
    />
  )
}

export default DateInput
