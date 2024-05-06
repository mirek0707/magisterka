import { useLocation } from 'react-router-dom'

const SearchPage = () => {
  const location = useLocation()

  const query = new URLSearchParams(location.search)
  const searchInput = query.get('q')
  return <>{searchInput}</>
}

export default SearchPage
