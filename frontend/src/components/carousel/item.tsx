import {
  Card,
  Grid,
  CardActionArea,
  CardMedia,
  CardContent,
  Typography,
} from '@mui/material'
import * as React from 'react'

import { CarouselItemProps, BooksCarouselProps } from './types'

const BooksCarouselItem: React.FC<BooksCarouselProps> = ({ items }) => {
  return (
    <Grid container direction="row" spacing={1}>
      {items.map((item: CarouselItemProps, index: number) => (
        <Grid item xs={12 / 8} key={index} className="p-1">
          <Card className="text-left">
            <CardActionArea>
              <CardMedia
                component="img"
                height="100"
                image={item.img_src}
                alt="book cover"
              />
              <CardContent>
                <Typography variant="h5">{item.title}</Typography>
                <Typography variant="subtitle1" sx={{ fontStyle: 'italic' }}>
                  {item.author}
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>
      ))}
    </Grid>
  )
}

export default BooksCarouselItem
