# X-Content-Type header
-------

## Example:


    // Ruby on Rails sets X-Content-Type-Options header with "nosniff" option by default.
    // If in your case it doesn't, you can add the header manually.

    // Add the following code to APP_DIR/app/controllers/YOUR_CONTROLLER.rb

    class YourController < ApplicationController
      def rendering_inline
        render inline: 'Content of the file', content_type: 'application/foo'
      end

      def rendering_from_file
        render file: filename, content_type: 'application/foo'
      end
    end

