import { Box, Divider, Grid, Typography } from '@mui/material'
import * as React from 'react'

import DeleteShelfButton from '../deleteShelf'
interface Props {
  shelfName: string
  shelf_id: string
  default_shelf: boolean
  refetch: () => void
}
const EmptyShelfComp: React.FC<Props> = ({
  shelfName,
  shelf_id,
  default_shelf,
  refetch,
}) => {
  return (
    <Box
      sx={{
        width: '100%',
        minWidth: '900px',
        maxWidth: '1600px',
      }}
    >
      <Grid
        container
        direction="row"
        justifyContent="flex-start"
        alignItems="center"
      >
        <Grid item sx={{ p: 1, pl: 0 }}>
          <Grid
            container
            direction="row"
            justifyContent="flex-start"
            alignItems="center"
          >
            <Typography variant="h5">{shelfName}</Typography>
          </Grid>
        </Grid>
        <Grid item sx={{ p: 1, pl: 0 }}>
          <DeleteShelfButton
            shelf_id={shelf_id}
            default_shelf={default_shelf as boolean}
            refetch={refetch}
          />
        </Grid>
      </Grid>
      <Divider sx={{ color: 'success.dark', m: 1 }} />
      <Typography variant="h6">
        {'Półka pusta, dodaj do niej książki'}
      </Typography>
    </Box>
  )
}
export default EmptyShelfComp
