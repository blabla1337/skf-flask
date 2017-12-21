# Session cookies (domain)
-------

## Example:


    // Whenever a session is started, and you want to share it over different domains,
    // the domain value should be set to the specific domain:

    // Add "domain: DOMAIN_NAME" option to APP_DIR/config/initializers/session_store.rb
    Rails.application.config.session_store :cookie_store, key: 'SESSIONID', domain: "DOMAIN_NAME"