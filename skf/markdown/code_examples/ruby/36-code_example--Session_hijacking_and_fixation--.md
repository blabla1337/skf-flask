# Session hijacking and fixation

# In order to secure your session, you have to turn on SECURE and HTTPONLY cookies' flags
# More info in: "Session cookies HTTPOnly" and "Secure session cookies"

# Turn on `force_ssl` in config/environments/production.rb
Rails.application.configure do
  # redirects all HTTP to HTTPS and also adds secure flag to your cookies
  config.force_ssl = true

  config.ssl_options = {
    # HTTP Strict Transport Security configuration
    hsts: {
      # default
      expires: 180.days,

      # default - if all present and future subdomains will be HTTPS
      subdomains: true,

      # Recommended: If the site owner would like their domain to be included in the HSTS preload list
      # defaults to false
      preload: true
    }
  }

  # more information can be found here: http://api.rubyonrails.org/classes/ActionDispatch/SSL.html
end

# After that add :trackable symbol to the devise configuration in users' model

# For example:
class User < ApplicationRecord
  has_many :posts

  # Be sure that :trackable is added
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :secure_validatable
end

# Now update controllers that need authenticated users to perform actions.
class ContollerWithAuthenticatedUsers < ApplicationController
  before_action :authenticate_user!
  before_action :check_ip

  private
  # After this modification current users' IP address will be compared to
  # the last IP that was used to log in on the account. If they dont match - 
  # user will be warned. This check will be performed every single user action.
  def check_ip
  	if current_user.last_sign_in_ip != request.remote_ip
  		flash[:warning] = "There are other active sessions on other IP addresses. " +
  		"Your session could be hijacked. Press logout in order to authenticate again " +
  		"for security reasons!"
  	end
  end  
end

