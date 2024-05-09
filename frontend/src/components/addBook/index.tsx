import AddCircleIcon from '@mui/icons-material/AddCircle'
import { Typography, Modal, Box, IconButton } from '@mui/material'
import * as React from 'react'
import ErrorPage from 'src/pages/error'
import { useUserShelves } from 'src/shelves/rquery'
import { useUserSession } from 'src/user/rquery'

import { Loading } from '../loading'

import AddBookForm from './form'
interface Props {
  title: string
  isbn: string
  onBookPage?: boolean
  refetchShelf?: () => void
}
const AddBookButton: React.FC<Props> = ({
  title,
  isbn,
  onBookPage,
  refetchShelf,
}) => {
  const [open, setOpen] = React.useState(false)

  const handleOpen = () => setOpen(true)
  const handleClose = () => {
    setOpen(false)
    shelves.refetch()
    if (refetchShelf !== undefined) {
      refetchShelf()
    }
  }

  const user = useUserSession()
  const shelves = useUserShelves(user.data?.id as string)

  if (user.isError || user.isIdle || shelves.isError || shelves.isIdle) {
    return <ErrorPage />
  }
  if (user.isLoading || shelves.isLoading) {
    return <Loading />
  }
  return (
    <>
      <IconButton
        onClick={handleOpen}
        sx={
          onBookPage
            ? {
                p: 0,
                m: 1,
                ml: 2,
                backgroundColor: 'black',
                '&:hover': {
                  backgroundColor: 'black',
                  transform: 'scale(1.2)',
                },
              }
            : {
                p: 0,
                backgroundColor: 'black',
                '&:hover': {
                  backgroundColor: 'white',
                  transform: 'scale(1.15)',
                },
              }
        }
        size="large"
        color="inherit"
        style={onBookPage ? {} : { position: 'absolute', top: 5, right: 5 }}
        className="max-h-6"
      >
        <AddCircleIcon color="primary" />
      </IconButton>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {'Dodaj książkę "' + title + '" na półki:'}
          </Typography>
          <AddBookForm
            shelves={shelves.data}
            isbn={isbn}
            closeModal={handleClose}
          />
        </Box>
      </Modal>
    </>
  )
}
export default AddBookButton

const style = {
  position: 'absolute' as const,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 600,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
}
