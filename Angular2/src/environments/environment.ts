// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: true,
  
  /* 
      This config is about the endpoint where your api is running that is talking to the Angular UI
      DO NOT CHANGE HTTP TO HTTPS MANUALLY SHOULD BE HANDLED BY DEPLOY SCRIPTS
  */
  API_ENDPOINT: 'https://krakend.secureby.design:8443',
  
  /* 
      This config is about wether you want to use OPENID or skipping logging etirely 
      
      AUTH_METHOD: 'openidprovider',
      AUTH_METHOD: 'skiploginprovider',  
  */
  AUTH_METHOD: 'openidprovider',
  
  /* 
     This config is about wether to show the SKF lab deployment options,  
     True || False -> This affects the way the lab page is shown with deployment buttons
  */
  KUBERNETES_ENABLED: 'True',
  
  /* 
    OPENID needs to know where krakend is because in the config we can tell to send the bearer token on each request:
    From : app.module.ts
    OAuthModule.forRoot({
      resourceServer: {
        allowedUrls: ['http://127.0.0.1:8080'],
        sendAccessToken: true
      }
    }),
  */
  KRAKEND_ENDPOINT: 'https://krakend.secureby.design:8443',

  /*
    Here is the rest of the auth config for openID connect
  */

  // Url of the Identity Provider
  OPENID_ISSUER: 'https://keycloak.secureby.design:8443/realms/krakend',
  // URL of the SPA to redirect the user to after login
  OPENID_REDIRECT_URI: window.location.origin + '/auth/openid',
  // The SPA's id. The SPA is registered with this id at the auth-server
  OPENID_CLIENT_ID: 'krakend',
  OPENID_RESPONSE_TYPE: 'code',
  OPENID_USE_SILENT_REFRESH: true,
  // set the scope for the permissions the client should request
  // The first three are defined by OIDC. The 4th is a usecase-specific one
  OPENID_SCOPE: 'openid profile email',

};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.