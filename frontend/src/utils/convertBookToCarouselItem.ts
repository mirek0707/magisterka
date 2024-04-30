import { Book } from 'src/books/types'
import { CarouselItemProps } from 'src/components/carousel/types'

export const convertBookToCarouselItem = (book: Book): CarouselItemProps => {
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
