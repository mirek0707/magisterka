export type AuthData = {
  token: string
}

export type LoginResponse = {
  access_token: AuthData['token']
}
