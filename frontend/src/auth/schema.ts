import {
    ErrorMessages,
    GenericUsernameConstraint,
    GenericEmailConstraint,
    GenericPasswordConstraint,
} from 'src/utils/zod/utils';
import { z } from 'zod';



export const LoginFormSchema = z.object({
    email: GenericEmailConstraint,
    password: z.string({ required_error: ErrorMessages.required }),
});

export type LoginFormData = z.infer<typeof LoginFormSchema>;


export const RegisterFormSchema = z
    .object({
        username: GenericUsernameConstraint,
        email: GenericEmailConstraint,
        password: GenericPasswordConstraint,
        confirmPassword: GenericPasswordConstraint,
    })
    .refine((v) => v.confirmPassword === v.password, {
        message: ErrorMessages.passwordsNotMatching,
        path: ['confirmPassword'],
    });

export type RegisterFormData = z.infer<typeof RegisterFormSchema>;