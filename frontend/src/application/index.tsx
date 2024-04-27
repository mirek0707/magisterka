import * as React from 'react'
import { useBooksPerPage } from 'src/books/rquery'
import { Book } from 'src/books/types'
import { CarouselItemProps } from 'src/components/carousel/types'

const LazyBooksCarousel = React.lazy(() => import('src/components/carousel'))

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
  const convertBookToCarouselItem = (book: Book): CarouselItemProps => {
    return {
      title: book.title[0],
      img_src:
        book.img_src && book.img_src[0]
          ? book.img_src[0]
          : 'https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg',
      author: book.author[0],
      isbn: book.isbn,
    }
  }

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

function Loading() {
  return <h2>🌀 Ładowanie...</h2>
}

export default AppPage
