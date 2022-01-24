import { AuthConfig } from 'angular-oauth2-oidc';
import { environment } from '../environments/environment';

export const authConfig: AuthConfig = {
  // Url of the Identity Provider
  issuer: environment.OPENID_ISSUER,

  // URL of the SPA to redirect the user to after login
  redirectUri: environment.OPENID_REDIRECT_URI,

  // The SPA's id. The SPA is registered with this id at the auth-server
  clientId: environment.OPENID_CLIENT_ID,
  responseType: environment.OPENID_RESPONSE_TYPE,
  useSilentRefresh: environment.OPENID_USE_SILENT_REFRESH,
  // set the scope for the permissions the client should request
  // The first three are defined by OIDC. The 4th is a usecase-specific one
  scope: environment.OPENID_SCOPE,
}

