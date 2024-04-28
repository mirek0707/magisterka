import {
  Card,
  Grid,
  CardActionArea,
  CardMedia,
  CardContent,
  Typography,
} from '@mui/material'
import * as React from 'react'
import { Routes } from 'src/routes'

import { CarouselItemProps } from './types'

const BookCard: React.FC<CarouselItemProps> = (item) => {
  return (
    <Card
      className="h-full text-left relative"
      sx={{ ':hover': { boxShadow: 10 } }}
    >
      <CardActionArea className="h-full" href={Routes.BookUrl(item.isbn)}>
        <CardMedia
          component="img"
          className="h-3/4"
          sx={{ objectFit: 'cover' }}
          image={item.img_src}
          alt="book cover"
        />
        <CardContent sx={{ p: 0 }} className="h-1/4">
          <Grid
            className="h-full p-2"
            container
            direction="column"
            justifyContent="center"
          >
            <Grid item>
              <Typography
                sx={{
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  display: '-webkit-box',
                  WebkitLineClamp: '1',
                  WebkitBoxOrient: 'vertical',
                }}
                variant="subtitle1"
              >
                {item.title}
              </Typography>
              <Typography
                sx={{
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  display: '-webkit-box',
                  WebkitLineClamp: '1',
                  WebkitBoxOrient: 'vertical',
                  fontStyle: 'italic',
                }}
                variant="subtitle2"
              >
                {item.author}
              </Typography>
            </Grid>
          </Grid>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}

export default BookCard
