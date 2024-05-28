import dayjs, { type Dayjs } from 'dayjs'
import { parse } from 'isbn3'
import { ErrorMessages } from 'src/utils/zod/utils'
import { z } from 'zod'
const authorSchema = z.object({
  value: z.string().min(2, { message: ErrorMessages.required }),
})

export const AddBookFormSchema = z.object({
  title: z
    .string({ required_error: ErrorMessages.required })
    .min(1, { message: ErrorMessages.required }),
  pages: z
    .number({
      invalid_type_error: ErrorMessages.pagesNotValid,
    })
    .int({ message: ErrorMessages.pagesNotValid })
    .min(0, { message: ErrorMessages.pagesNotValid }),
  author: z.array(authorSchema).min(1, { message: 'ErrorMessages.required' }),
  isbn: z
    .string({ required_error: ErrorMessages.required })
    .refine((val) => parse(val), ErrorMessages.isbnNotValid),
  publisher: z.string(),
  original_title: z.string(),
  release_date: z.instanceof(dayjs as unknown as typeof Dayjs).nullable(),
  release_year: z.number().int(),
  polish_release_date: z
    .instanceof(dayjs as unknown as typeof Dayjs)
    .nullable(),
  img_src: z
    .string()
    .url(ErrorMessages.linkNotValid)
    .refine(
      (url) => {
        return /\.(jpg|jpeg|png|gif|bmp|webp)$/i.test(url)
      },
      { message: ErrorMessages.linkNotValid }
    )
    .optional()
    .or(z.literal('')),
  description: z.string(),
  genre: z.string(),
})

export type AddBookFormData = z.infer<typeof AddBookFormSchema>
