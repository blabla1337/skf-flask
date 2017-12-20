# Secure session cookies

# Example:

# Add "secure: true" option to APP_DIR/config/initializers/session_store.rb
Rails.application.config.session_store :cookie_store, key: 'SESSIONID', expire_after: 1.hour, secure: true