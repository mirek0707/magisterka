import { get } from 'src/api'
import { useReactQuery } from 'src/rquery'

import { getUserShelves, getUserShelf } from './api'
import { Shelf } from './types'

export const useUserShelves = (user_id: string) =>
  useReactQuery<Shelf[]>(get, getUserShelves(user_id))

export const useShelf = (user_id: string, shelf_id: string) =>
  useReactQuery<Shelf>(get, getUserShelf(user_id, shelf_id))
