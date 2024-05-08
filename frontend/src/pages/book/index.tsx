import {
  Box,
  Grid,
  List,
  ListItem,
  ListItemText,
  Rating,
  Typography,
} from '@mui/material'
import moment from 'moment'
import 'moment/dist/locale/pl'
import * as React from 'react'
import { Carousel } from 'react-responsive-carousel'
import { useParams } from 'react-router-dom'
import { useBook } from 'src/books/rquery'
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import AddBookButton from 'src/components/addBook'
import { Loading } from 'src/components/loading'

import ErrorPage from '../error'
const BookPage: React.FC = () => {
  moment.locale('pl')
  const { isbn = '' } = useParams()
  const book = useBook(isbn)
  if (book.isError || book.isIdle) {
    return <ErrorPage />
  }
  if (book.isLoading) {
    return <Loading />
  }
  return (
    <Grid container spacing={2}>
      <Grid
        item
        container
        alignItems="center"
        direction="column"
        xs={3}
        minWidth={'199px'}
      >
        <Box
          sx={{
            maxWidth: 280,
          }}
        >
          <Carousel
            autoPlay={true}
            infiniteLoop={true}
            showIndicators={false}
            showStatus={false}
            showThumbs={false}
          >
            {(book.data.img_src && book.data.img_src.length
              ? book.data.img_src
              : [
                  'https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg',
                ]
            ).map((src: string, index: number) => (
              <Box key={index} sx={{ maxWidth: 280 }}>
                <img className="w-full" src={src} alt="book cover" />
              </Box>
            ))}
          </Carousel>
        </Box>
        <Typography component="legend" sx={{ p: 2 }}>
          Ocena ogólna:
        </Typography>
        <Grid
          container
          spacing={2}
          direction="row"
          justifyContent="center"
          alignItems="flex-start"
        >
          <Rating
            name="rating"
            value={book.data.rating}
            precision={0.1}
            readOnly
            size="large"
          />
          <Box sx={{ ml: 1, fontSize: '1.29rem' }}>
            {book.data.rating?.toFixed(2)}
          </Box>
        </Grid>
        <Typography sx={{ p: 1 }}>Ilość: {book.data.ratings_number}</Typography>
      </Grid>
      <Grid item container xs={9}>
        <Grid item>
          <Typography variant="h4">{book.data.title[0]}</Typography>
          <Typography variant="subtitle1">
            {book.data.author.join(', ')}
          </Typography>
        </Grid>
        <AddBookButton
          title={book.data.title[0]}
          isbn={book.data.isbn}
          onBookPage={true}
        />
        <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
          <ListItem>
            <ListItemText primary="ISBN" secondary={book.data.isbn} />
          </ListItem>
          {book.data.title[1] && (
            <ListItem>
              <ListItemText
                primary="Inne tytuły"
                secondary={book.data.title.slice(1).join(', ')}
              />
            </ListItem>
          )}
          {book.data.genre !== '' && (
            <ListItem>
              <ListItemText primary="Gatunek" secondary={book.data.genre} />
            </ListItem>
          )}
          {book.data.pages && book.data.pages[0] && (
            <ListItem>
              <ListItemText
                primary="Ilość stron"
                secondary={book.data.pages.join(', ')}
              />
            </ListItem>
          )}
          {book.data.publisher && book.data.publisher[0] && (
            <ListItem>
              <ListItemText
                primary="Wydawnictwo"
                secondary={book.data.publisher.join(', ')}
              />
            </ListItem>
          )}
          {book.data.original_title && book.data.original_title[0] && (
            <ListItem>
              <ListItemText
                primary="Oryginalny tytuł"
                secondary={book.data.original_title.join(', ')}
              />
            </ListItem>
          )}
          {(book.data.release_date && book.data.release_date[0] && (
            <ListItem>
              <ListItemText
                primary="Data wydania"
                secondary={book.data.release_date
                  .map((date) => moment(date).format('L'))
                  .join(' lub ')}
              />
            </ListItem>
          )) ||
            (book.data.release_year && book.data.release_year[0] && (
              <ListItem>
                <ListItemText
                  primary="Rok wydania"
                  secondary={book.data.release_year.join(' lub ')}
                />
              </ListItem>
            ))}
          {book.data.polish_release_date &&
            book.data.polish_release_date[0] && (
              <ListItem>
                <ListItemText
                  primary="Polska data wydania"
                  secondary={book.data.polish_release_date
                    .map((date) => moment(date).locale('pl').format('L'))
                    .join(' lub ')}
                />
              </ListItem>
            )}
          {book.data.description !== '' && (
            <ListItem>
              <ListItemText primary="Opis" secondary={book.data.description} />
            </ListItem>
          )}
          {(book.data.rating_lc || book.data.rating_lc === 0) && (
            <ListItem
              sx={{
                flexDirection: 'column',
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
              }}
            >
              <ListItemText primary="Ocena na lubimyczytac.pl" />
              <Grid
                container
                spacing={2}
                direction="row"
                alignItems="flex-start"
                sx={{ p: 2 }}
              >
                <Rating
                  name="rating"
                  value={book.data.rating_lc}
                  precision={0.1}
                  readOnly
                  max={10}
                />
                <Box
                  className="css-83ijpv-MuiTypography-root"
                  sx={{ ml: 1, fontSize: '1.05rem' }}
                >
                  {`${book.data.rating_lc?.toFixed(2)}, ilość: ${
                    book.data.ratings_lc_number
                  }`}
                </Box>
              </Grid>
            </ListItem>
          )}
          {(book.data.rating_gr || book.data.rating_gr === 0) && (
            <ListItem
              sx={{
                flexDirection: 'column',
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
              }}
            >
              <ListItemText primary="Ocena na goodreads.com" />
              <Grid
                container
                spacing={2}
                direction="row"
                alignItems="flex-start"
                sx={{ p: 2 }}
              >
                <Rating
                  name="rating"
                  value={book.data.rating_gr}
                  precision={0.1}
                  readOnly
                />
                <Box
                  className="css-83ijpv-MuiTypography-root"
                  sx={{ ml: 1, fontSize: '1.05rem' }}
                >
                  {`${book.data.rating_gr?.toFixed(2)}, ilość: ${
                    book.data.ratings_gr_number
                  }`}
                </Box>
              </Grid>
            </ListItem>
          )}
          {(book.data.rating_tk || book.data.rating_tk === 0) && (
            <ListItem
              sx={{
                flexDirection: 'column',
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
              }}
            >
              <ListItemText primary="Ocena na taniaksiazka.pl" />
              <Grid
                container
                spacing={2}
                direction="row"
                alignItems="flex-start"
                sx={{ p: 2 }}
              >
                <Rating
                  name="rating"
                  value={book.data.rating_tk}
                  precision={0.1}
                  readOnly
                />
                <Box
                  className="css-83ijpv-MuiTypography-root"
                  sx={{ ml: 1, fontSize: '1.05rem' }}
                >
                  {`${book.data.rating_tk?.toFixed(2)}, ilość: ${
                    book.data.ratings_tk_number
                  }`}
                </Box>
              </Grid>
            </ListItem>
          )}
        </List>
      </Grid>
    </Grid>
  )
}

export default BookPage
