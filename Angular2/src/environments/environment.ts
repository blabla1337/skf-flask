// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: true,  
  /* 
      This config is about the endpoint where your api is running that is talking to the Angular UI
      DO NOT CHANGE HTTP TO HTTPS MANUALLY SHOULD BE HANDLED BY DEPLOY SCRIPTS
  */
  API_ENDPOINT: 'http://localhost:8888',
  AUTH_METHOD: 'skiploginprovider',
  
  /* 
     This config is about wether to show the SKF lab deployment options,  
     True || False -> This affects the way the lab page is shown with deployment buttons
  */
  KUBERNETES_ENABLED: 'True',

    /* 
     config need to be there but is not used -  feeling wacky might refactor later
    */
  KRAKEND_ENDPOINT: '',
  OPENID_ISSUER: '',
  OPENID_REDIRECT_URI: '',
  OPENID_CLIENT_ID: '',
  OPENID_RESPONSE_TYPE: '',
  OPENID_USE_SILENT_REFRESH: true,
  OPENID_SCOPE: '',
};