import { Box, Divider, Typography } from '@mui/material'
import * as React from 'react'
interface Props {
  shelfName: string
}
const EmptyShelfComp: React.FC<Props> = ({ shelfName }) => {
  return (
    <Box
      sx={{
        width: '100%',
        minWidth: '900px',
        maxWidth: '1600px',
      }}
    >
      <Typography variant="h5">{shelfName}</Typography>
      <Divider sx={{ color: 'success.dark', m: 1 }} />
      <Typography variant="h6">
        {'Półka pusta, dodaj do niej książki'}
      </Typography>
    </Box>
  )
}
export default EmptyShelfComp
