export const API_ROOT_PATH = '/shelf'

export const getUserShelves = (user_id: string) => `${API_ROOT_PATH}/${user_id}`
export const getUserShelf = (user_id: string, shelf_id: string) =>
  `${API_ROOT_PATH}/${user_id}/${shelf_id}`
