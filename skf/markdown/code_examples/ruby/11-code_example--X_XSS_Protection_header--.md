# X-XSS-Protection header
-------

## Example:


    // Ruby on Rails sets X-XSS-Protection header with "1; mode=block" option by default.
    // If in your case it doesn't, you can add the header manually.

    // Add the following code to APP_DIR/config/environments/production.rb

    config.action_dispatch.default_headers = {
      'X-XSS-Protection' => '1; mode=block'
    }
