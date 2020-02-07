# Enforce secure passwords
-------

## Example:


    // It is highly recommended to use Devise gem that handles authentication on your RoR app.
    // more info: https://github.com/plataformatec/devise
    // Then install Devise Security Extension gem (https://github.com/phatworx/devise_security_extension)
    // Follow the installing instructions mentioned on Github

    // Now it's time to configure the gem in APP_DIR/config/initializers/devise.rb
    // Uncomment and customize following lines of code

    // Configuration of the gem core
    config.password_length = 10..128

    // Configuration of the gem extenstion
    config.password_regex = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])/ // at least one number, big letter and small letter
    config.password_archiving_count = 5
    config.deny_old_passwords = true

    // Now update your model
    // For example:
    class User < ApplicationRecord
      has_many :posts

      // add :secure_validatable. Remember not to use :secure_validatable with :validatable
      devise :database_authenticatable, :registerable,
            :recoverable, :rememberable, :trackable, :secure_validatable
    end

