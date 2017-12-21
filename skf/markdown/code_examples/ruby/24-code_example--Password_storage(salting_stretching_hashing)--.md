# Password storage (salting sretching hashing)
-------

## Example:

    
    // It is highly recommended to use Devise gem that handles authentication on your RoR app.
    // more info: https://github.com/plataformatec/devise

    // Configure the gem in APP_DIR/config/initializers/devise.rb
    config.stretches = Rails.env.test? ? 3 : 11

    // By default password hashing algorithm is set to BCRYPT which is good - it means that u can
    // leave it with default settings

    // Now update your model
    // For example:
    class User < ApplicationRecord
      has_many :posts

      // add :database_authenticatable to turn on password safe storing
      devise :database_authenticatable, :registerable,
            :recoverable, :rememberable, :trackable, :secure_validatable
    end

