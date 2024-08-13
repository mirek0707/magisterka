import * as React from 'react'
import { Shelf } from '/src/shelves/types'

import EmptyShelfComp from './emptyShelfComp'
import ShelfComp from './shelfComp'

interface Props {
  shelves: Shelf[]
  refetch: () => void
}

const Library: React.FC<Props> = ({ shelves, refetch }) => {
  return shelves.map((item: Shelf, index: number) => (
    <React.Fragment key={index}>
      {item.books.length !== 0 ? (
        <ShelfComp shelf={item} refetch={refetch} />
      ) : (
        <EmptyShelfComp
          shelfName={item.name}
          default_shelf={item.is_default}
          shelf_id={item._id}
          refetch={refetch}
        />
      )}
    </React.Fragment>
  ))
}
export default Library
