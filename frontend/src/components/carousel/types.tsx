export type CarouselItemProps = {
  title: string
  img_src: string
  author: string
  isbn: string
  bookAdd?: boolean
  refetchShelf?: () => void
}

export type BooksCarouselProps = {
  title?: string
  items: CarouselItemProps[]
  shelf_id?: string
}
