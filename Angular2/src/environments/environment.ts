// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: true,
  //DO NOT CHANGE HTTP TO HTTPS MANUALLY SHOULD BE HANDLED BY DEPLOY SCRIPTS
  //API_ENDPOINT: 'http://127.0.0.1:8888',
  API_ENDPOINT: 'https://beta.securityknowledgeframework.org',
  //API_ENDPOINT: 'https://owasp-skf.cloud.tyk.io/api/api',
  //AUTH_METHOD: 'openidprovider'
  //AUTH_METHOD: 'skiploginprovider'
  AUTH_METHOD: 'skfprovider'
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
