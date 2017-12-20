# X-XSS-Protection header

# Example:

# Ruby on Rails sets encoding header with "utf-8" option by default.
# If in your case it doesn't or you want to set different encoding, you can do it manually.

# Add the following code to APP_DIR/config/environments/production.rb

config.encoding = 'utf-8'
