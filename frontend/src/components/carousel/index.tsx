import * as React from 'react'
import Carousel from 'react-material-ui-carousel'

import BooksCarouselItem from './item'
import { CarouselItemProps, BooksCarouselProps } from './types'

const BooksCarousel: React.FC<BooksCarouselProps> = ({ items }) => {
  const newArray = []
  const newData = [...items]
  while (newData.length > 0) newArray.push(newData.splice(0, 4))
  return (
    <Carousel>
      {newArray.map((item: CarouselItemProps[], index: number) => (
        <BooksCarouselItem key={index} items={item} />
      ))}
    </Carousel>
  )
}

export default BooksCarousel
