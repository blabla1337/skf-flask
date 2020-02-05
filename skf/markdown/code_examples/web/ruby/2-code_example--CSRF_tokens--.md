# CSRF Tokens
-------

## Example:

          
    // Handling Cross-Site Request Forgery is as simple as adding following line of code into 
    // your APP_DIR/controllers/application_controller.rb

    class ApplicationController < ActionController::Base
      protect_from_forgery with: :exception
    end

    // It's important to know that RoR is REST based framework and CSRF protection does not work on HTTP GET requests.