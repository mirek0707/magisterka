import { Grid } from '@mui/material'
import * as React from 'react'

import BookCard from './card'
import { CarouselItemProps, BooksCarouselProps } from './types'

const BooksCarouselItem: React.FC<BooksCarouselProps> = ({ items }) => {
  return (
    <Grid container direction="row" spacing={{ lg: 1, xl: 2 }}>
      {items.map((item: CarouselItemProps, index: number) => (
        <Grid item xs={12 / 8} key={index} className="p-1">
          <BookCard {...item} bookAdd={true} />
        </Grid>
      ))}
    </Grid>
  )
}

export default BooksCarouselItem
