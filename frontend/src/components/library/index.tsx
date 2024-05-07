import * as React from 'react'
import { Shelf } from 'src/shelves/types'

import EmptyShelfComp from './emptyShelfComp'
import ShelfComp from './shelfComp'

interface Props {
  shelves: Shelf[]
}

const Library: React.FC<Props> = ({ shelves }) => {
  return shelves.map((item: Shelf, index: number) => (
    <>
      {item.books.length !== 0 ? (
        <ShelfComp key={index} shelf={item} />
      ) : (
        <EmptyShelfComp shelfName={item.name} />
      )}
    </>
  ))
}
export default Library
