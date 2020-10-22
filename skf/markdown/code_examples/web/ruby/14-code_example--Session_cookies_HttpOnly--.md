# Session cookies HTTPOnly
-------

## Example:


    // Add "httponly: true" option to APP_DIR/config/initializers/session_store.rb
    Rails.application.config.session_store :cookie_store, key: 'SESSIONID', httponly: true