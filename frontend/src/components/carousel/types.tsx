export type CarouselItemProps = {
  title: string
  img_src: string
  author: string
  isbn: string
}

export type BooksCarouselProps = {
  title?: string
  items: CarouselItemProps[]
}
