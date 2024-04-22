import * as React from 'react'
import BooksCarousel from 'src/components/carousel'

const BooksMock = [
  {
    title: 'title1',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100856/1123909-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title2',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5101000/5101903/1129249-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title3',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100977/1129575-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title4',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5077000/5077539/1114281-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title5',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100856/1123909-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title6',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5101000/5101903/1129249-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title7',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5107000/5107048/1134280-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title8',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5098000/5098037/1118881-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title1',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100856/1123909-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title2',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5101000/5101903/1129249-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title3',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100977/1129575-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title4',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5077000/5077539/1114281-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title5',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5100000/5100856/1123909-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title6',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5101000/5101903/1129249-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title7',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5107000/5107048/1134280-352x500.jpg',
    author: 'string',
  },
  {
    title: 'title8',
    img_src:
      'https://s.lubimyczytac.pl/upload/books/5098000/5098037/1118881-352x500.jpg',
    author: 'string',
  },
]

const AppPage: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-center w-100 space-y-5">
      <BooksCarousel title={'Ostatnio dodane'} items={BooksMock} />
      <BooksCarousel title={'Najlepiej oceniane'} items={BooksMock} />
    </div>
  )
}

export default AppPage
