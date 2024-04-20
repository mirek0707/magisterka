import { z } from 'zod';

export const ErrorMessages = {
  required: 'To pole jest wymagane',
  email: 'Nieprawidłowy adres email',
  passwordLength: 'Zbyt krótkie hasło, powinno mieć co najmniej 6 znaków',
  passwordsNotMatching: 'Podane hasła są różne od siebie',
};


export const GenericUsernameConstraint = z
  .string({ required_error: ErrorMessages.required });

export const GenericPasswordConstraint = z
  .string({ required_error: ErrorMessages.required })
  .min(6, { message: ErrorMessages.passwordLength });

export const GenericEmailConstraint = z
  .string({ required_error: ErrorMessages.required })
  .email({ message: ErrorMessages.email });