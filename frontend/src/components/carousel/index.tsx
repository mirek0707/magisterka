import { Divider, Typography, Box } from '@mui/material'
import {
  ThemeProvider,
  createTheme,
  responsiveFontSizes,
} from '@mui/material/styles'
import * as React from 'react'
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import { Carousel } from 'react-responsive-carousel'

import BooksCarouselItem from './item'
import { CarouselItemProps, BooksCarouselProps } from './types'

let theme = createTheme()
theme = responsiveFontSizes(theme)

const BooksCarousel: React.FC<BooksCarouselProps> = ({ title, items }) => {
  const newArray = []
  const newData = [...items]
  while (newData.length > 0) newArray.push(newData.splice(0, 8))
  return (
    <Box
      sx={{
        width: '100%',
        minWidth: '900px',
        maxWidth: '1600px',
      }}
    >
      <ThemeProvider theme={theme}>
        <Typography variant="h5">{title}</Typography>
        <Divider sx={{ color: 'success.dark', m: 1 }} />
        <Carousel
          autoPlay={true}
          infiniteLoop={true}
          showIndicators={false}
          showStatus={false}
          showThumbs={false}
        >
          {newArray.map((item: CarouselItemProps[], index: number) => (
            <BooksCarouselItem key={index} items={item} />
          ))}
        </Carousel>
      </ThemeProvider>
    </Box>
  )
}

export default BooksCarousel
