# Re authentication
-------

## Example:


	// Whenever a user wants to change his credentials or do other important data exchanges such as
	// transferring money he should always be challenged to reauthenticate himself before
	// allowing them to perform these actions.

	// Enforcing re-authentication before changing the password is provided by default in Devise gem. All you have
	// To do is add such link in your view
	<%= link_to "Change your password", edit_user_registration_path %


	// Other action may require adding your before_action method in specific controller
	class SpecificController < ApplicationController
		before_action :re_entered_password?, only: [:edit] 

		private
		def re_entered_password? 
			if session[:reauthenticated_at] == nil or session[:reauthenticated_at] > 2.minute
				// Redirect to view that requires entering your password
				redirect_to action: => "re_authenticate" 
			end
		end
	end

	// After successful authentication set 
	session[:reauthenticated_at] = Time.now
    