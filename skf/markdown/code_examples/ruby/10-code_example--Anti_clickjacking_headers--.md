# Anti clickjacking headers

# Example:

# Ruby on Rails sets X-Frame-Options header with "SAMEORIGIN" option by default.
# If in your case it doesn't or you want to enforce "DENY" options, you can add that headers manually.

# Add the following code to APP_DIR/config/environments/production.rb

config.action_dispatch.default_headers = {
  'X-Frame-Options' => 'DENY' # this will completely prevent your page from being displayed in an iframe.
}

# OR

config.action_dispatch.default_headers = {
  'X-Frame-Options' => 'SAMEORIGIN' # this will completely prevent your page from being displayed in an iframe on other sites.
}
