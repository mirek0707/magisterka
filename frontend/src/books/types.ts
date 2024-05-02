export type Book = {
  _id: string
  title: string[]
  author: string[]
  pages: number[] | null
  isbn: string
  publisher: string[] | null
  original_title: string[] | null
  release_date: Date[] | null
  release_year: number[] | null
  polish_release_date: Date[] | null
  rating_lc: number | null
  ratings_lc_number: number | null
  rating_tk: number | null
  ratings_tk_number: number | null
  rating_gr: number | null
  ratings_gr_number: number | null
  rating: number | null
  ratings_number: number | null
  img_src: string[] | null
  description: string
  genre: string
}

export type BooksPerPageReq = {
  page?: number
  limit?: number
  sort_by?: string
  order?: number
  release_year_from?: number | null
  release_year_to?: number | null
  author?: string | null
  publisher?: string | null
  genre?: string | null
}

export type BooksCount = {
  count: number
}

export type BooksAuthors = {
  authors: string[]
}

export type BooksGenres = {
  genres: string[]
}

export type BooksCountFiltersReq = {
  release_year_from?: number | null
  release_year_to?: number | null
  author?: string | null
  publisher?: string | null
  genre?: string | null
}

export type BooksPublishers = {
  publishers: string[]
}

export type BooksMinMaxYears = {
  max_year: number
  min_year: number
}
