import { getPersistentAuthData } from '/src/auth/localStorage'

export const getAxiosAuthorizationHeader = (): string | undefined => {
  const data = getPersistentAuthData()

  return data?.token
}
