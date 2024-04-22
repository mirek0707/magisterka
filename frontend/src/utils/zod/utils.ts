import { z } from 'zod'

export const ErrorMessages = {
  required: 'To pole jest wymagane',
  email: 'Nieprawidłowy adres email',
  passwordLength: 'Hasło musi zawierać co najmniej 6 znaków',
  passwordsNotMatching: 'Podane hasła są różne od siebie',
  passwordValidationFail:
    'Hasło musi zawierać małą, wielką literę, cyfrę i znak specjalny',
  usernameLength: 'Nazwa użytkownika musi zawierać od 3 do 12 znaków',
}

const passwordValidation = new RegExp(
  /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$/
)

export const GenericUsernameConstraint = z
  .string({ required_error: ErrorMessages.required })
  .min(3, { message: ErrorMessages.usernameLength })
  .max(12, { message: ErrorMessages.usernameLength })

export const GenericPasswordConstraint = z
  .string({ required_error: ErrorMessages.required })
  .min(6, { message: ErrorMessages.passwordLength })
  .regex(passwordValidation, {
    message: ErrorMessages.passwordValidationFail,
  })

export const GenericEmailConstraint = z
  .string({ required_error: ErrorMessages.required })
  .email({ message: ErrorMessages.email })
