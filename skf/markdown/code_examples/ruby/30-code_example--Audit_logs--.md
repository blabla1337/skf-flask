# Audit Logs
-------

## Example:


    // Logging is turned on in Ruby on Rails by default. Every request is logged that is nice but it may 
    // cause security issues like information disclosure. If attacker gets access to web server, it's possible
    // to read all requests containing confidential data like logins, passwords, card numbers etc. That's why it
    // is recommended to define which values shouldn't be stored in logs.

    // Add following line of code to APP_DIR/config/initializers/filter_parameter_logging.rb in order to filter
    // confidential data being saved in logs.

    Rails.application.config.filter_parameters += [:confidential_parameter]