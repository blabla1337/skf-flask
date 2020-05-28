// The file contents for the current environment will overwrite these during build.

export const environment = {
  production: false,
  //DO NOT CHANGE HTTP TO HTTPS MANUALLY SHOULD BE HANDLED BY DEPLOY SCRIPTS
  API_ENDPOINT: 'http://127.0.0.1:8888/api',
  //AUTH_METHOD: 'openidprovider'
  //AUTH_METHOD: 'skiploginprovider'
  AUTH_METHOD: 'skfprovider'
};
