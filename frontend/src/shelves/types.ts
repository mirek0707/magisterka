export type Shelf = {
  _id: string
  books: string[]
  is_default: boolean
  name: string
}

export type ImportLCReq = {
  url: string
}

export type AddShelfReq = {
  name: string
}
