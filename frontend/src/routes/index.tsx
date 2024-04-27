export const Routes = {
  HomeUrl: () => `/`,
  AppUrl: () => `/app`,
  LoginUrl: () => `/login`,
  RegisterUrl: () => `/register`,

  LibraryUrl: () => `/app/library`,
  BooksUrl: () => `/app/books`,
  ProfileUrl: () => `/app/profile`,

  BookUrl: (isbn: string) => `/app/books/${isbn}`,
}
