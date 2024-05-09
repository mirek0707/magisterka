import * as React from 'react'
import { useBooksSearchFt } from 'src/books/rquery'

import SearchResultBooks from './books'

type Props = {
  query: URLSearchParams
  searchInput: string
  page: number
}

const SearchDef: React.FC<Props> = ({ query, page, searchInput }) => {
  const books = useBooksSearchFt({
    query: searchInput,
    num_of_books: 300,
  })
  return <SearchResultBooks query={query} page={page} books={books} />
}

export default SearchDef
