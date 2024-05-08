import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import { Divider, Typography, Box, Grid } from '@mui/material'
import {
  ThemeProvider,
  createTheme,
  responsiveFontSizes,
} from '@mui/material/styles'
import * as React from 'react'
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import { Carousel } from 'react-responsive-carousel'
import { NavLink } from 'react-router-dom'
import { Routes } from 'src/routes'

import BooksCarouselItem from './item'
import { CarouselItemProps, BooksCarouselProps } from './types'

let theme = createTheme()
theme = responsiveFontSizes(theme)

const BooksCarousel: React.FC<BooksCarouselProps> = ({
  title,
  items,
  shelf_id,
}) => {
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
        {shelf_id ? (
          <NavLink
            to={Routes.ShelfUrl(shelf_id)}
            color="inherit"
            className={'hover:underline'}
          >
            <Grid
              container
              direction="row"
              justifyContent="flex-start"
              alignItems="center"
            >
              <Typography variant="h5">{title}</Typography>
              <ExpandMoreIcon fontSize="large" />
            </Grid>
          </NavLink>
        ) : (
          <Typography variant="h5">{title}</Typography>
        )}

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
