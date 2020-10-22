# Enforce secure passwords
-------

## Example:


    // It is highly recommended to use Devise gem that handles authentication on your RoR app.
    // more info: https://github.com/plataformatec/devise
    // Then install Devise Security Extension gem (https://github.com/phatworx/devise_security_extension)
    // Follow the installing instructions mentioned on Github

    // After successful installation you should have created user's views and controllers

    // Firstly, configure the mail settings

    // APP_DIR/config/environments/production.rb
    config.action_mailer.delivery_method = :smtp
    config.action_mailer.smtp_settings = {
    :address              => "smtp.yoursite.com",
    :port                 => 587,
    :user_name            => ENV['email_username'], // it is not recommended to hardcode sensitive data
    :password             => ENV['email_password'],
    :ssl                  => true,
    :enable_starttls_auto => true
    }

    // Now it's time to configure the gem in APP_DIR/config/initializers/devise.rb
    // Uncomment and customize following lines of code
    config.password_archiving_count = 5
    config.deny_old_passwords = true


    // Now update your model
    // For example:
    class User < ApplicationRecord
      has_many :posts

      // add :recoverable that allows user reset the password
      devise :database_authenticatable, :registerable,
            :recoverable, :rememberable, :trackable, :secure_validatable
    end

