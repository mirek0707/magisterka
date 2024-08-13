export type AuthData = {
  token: string
}

export type LoginResponse = {
  access_token: AuthData['token']
}

export type RegisterRequest = {
  username: string
  email: string
  password: string
  role: string
}
