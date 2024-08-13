import { Book } from '/src/books/types'
import { CarouselItemProps } from '/src/components/carousel/types'

export const convertBookToCarouselItem = (book: Book): CarouselItemProps => {
  return {
    title: book.title[0],
    img_src:
      book.img_src && book.img_src[0]
        ? book.img_src[0]
        : 'https://media.istockphoto.com/id/1055079680/vector/black-linear-photo-camera-like-no-image-available.jpg?s=612x612&w=0&k=20&c=P1DebpeMIAtXj_ZbVsKVvg-duuL0v9DlrOZUvPG6UJk=',
    author: book.author[0],
    isbn: book.isbn,
  }
}
