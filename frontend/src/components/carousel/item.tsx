import { Paper, Grid } from '@mui/material'
import * as React from 'react'

import { CarouselItemProps, BooksCarouselProps } from './types'

const BooksCarouselItem: React.FC<BooksCarouselProps> = ({ items }) => {
  return (
    <Grid container direction="row" xs={12} spacing={2}>
      {items.map((item: CarouselItemProps, index: number) => (
        <Grid item xs={3}>
          <Paper
            key={index}
            className="flex justify-center items-center py-2 max-h-64 flex-col"
          >
            <img
              src={item.img_src}
              className="object-scale-down rounded-md h-52"
            />
            <h2 className="text-lg uppercase">{item.title}</h2>
          </Paper>
        </Grid>
      ))}
    </Grid>
  )
}

export default BooksCarouselItem
