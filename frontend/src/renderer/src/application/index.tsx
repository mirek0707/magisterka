import * as React from 'react'
import { useBooksPerPage } from '/src/books/rquery'
import { Loading } from '/src/components/loading'
import { convertBookToCarouselItem } from '/src/utils/convertBookToCarouselItem'

const LazyBooksCarousel = React.lazy(() => import('/src/components/carousel'))

const AppPage: React.FC = () => {
  const latestBooks = useBooksPerPage({
    page: 1,
    limit: 32,
    sort_by: 'release_date',
    order: -1,
  })
  const bestBooks = useBooksPerPage({
    page: 1,
    limit: 32,
    sort_by: 'ratings_number',
    order: -1,
  })

  return (
    <div className="flex flex-col items-center justify-center w-100 space-y-5">
      <React.Suspense fallback={<Loading />}>
        {latestBooks.data ? (
          <LazyBooksCarousel
            title={'Najnowsze książki'}
            items={latestBooks.data.map(convertBookToCarouselItem)}
          />
        ) : (
          <Loading />
        )}
      </React.Suspense>
      <React.Suspense fallback={<Loading />}>
        {bestBooks.data ? (
          <LazyBooksCarousel
            title={'Najpopularniejsze książki'}
            items={bestBooks.data.map(convertBookToCarouselItem)}
          />
        ) : (
          <Loading />
        )}
      </React.Suspense>
    </div>
  )
}

export default AppPage
