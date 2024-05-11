import { GenericURLConstraint } from 'src/utils/zod/utils'
import { z } from 'zod'

export const ImportLCFormSchema = z.object({
  url: GenericURLConstraint,
})

export type ImportLCFormData = z.infer<typeof ImportLCFormSchema>
