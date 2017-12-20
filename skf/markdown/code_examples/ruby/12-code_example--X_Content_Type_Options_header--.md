# X-Content-Type-Options header

# Example:

# Ruby on Rails sets X-Content-Type-Options header with "nosniff" option by default.
# If in your case it doesn't, you can add the header manually.

# Add the following code to APP_DIR/config/environments/production.rb

config.action_dispatch.default_headers = {
  'X-Content-Type-Options' => 'nosniff'
}
