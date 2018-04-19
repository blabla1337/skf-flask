# Timeout a session
-------

## Example:


    // Add "expire_after: 1.hour option to APP_DIR/config/initializers/session_store.rb
    Rails.application.config.session_store :cookie_store, key: 'SESSIONID', secure: true, expire_after: 1.hour