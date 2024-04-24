import * as React from 'react'
import AuthProvider from 'src/auth/context'
import RQueryClientProvider from 'src/rquery/provider'
import { QueryParamProvider } from 'use-query-params'
import { ReactRouter6Adapter } from 'use-query-params/adapters/react-router-6'

import UserProvider from './user/context'

type Props = {
  children: React.ReactNode
}

const Providers: React.FC<Props> = ({ children }) => {
  return (
    <QueryParamProvider adapter={ReactRouter6Adapter}>
      <RQueryClientProvider>
        <AuthProvider>
          <UserProvider>{children}</UserProvider>
        </AuthProvider>
      </RQueryClientProvider>
    </QueryParamProvider>
  )
}

export default Providers
