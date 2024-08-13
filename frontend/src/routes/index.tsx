export const Routes = {
  HomeUrl: () => `/`,
  AppUrl: () => `/app`,
  LoginUrl: () => `/login`,
  RegisterUrl: () => `/register`,

  LibraryUrl: () => `/app/library`,
  ShelfUrl: (shelf_id: string) => `/app/shelf/${shelf_id}`,
  BooksUrl: () => `/app/books`,
  SearchUrl: () => `/app/search`,
  ProfileUrl: () => `/app/profile`,
  AddBookUrl: () => `/app/addbook`,

  BookUrl: (isbn: string) => `/app/books/${isbn}`,
}
