import { ErrorMessages } from 'src/utils/zod/utils'
import { z } from 'zod'

export const ImportAddBookFormSchema = z.object({
  name: z.string({ required_error: ErrorMessages.required }),
})

export type ImportAddBookFormData = z.infer<typeof ImportAddBookFormSchema>
