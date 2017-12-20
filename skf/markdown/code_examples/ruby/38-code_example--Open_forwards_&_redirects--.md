# Open forwards & redirects

# Example

# When using forwards & redirects you should make sure the URL is being explicitly
# declared in the code and cannot be manipulated by an attacker like:

redirect_to params[:redirect]

# Generally you should avoid getting input into the redirect which could contain
# userinput by any means. if for any reason this may not be feasible than you
# should make a whitelist input validation for the redirect

def redirecting
	if params[:redirect] =~ %r{^https\:\/\/trusted-site.com\/.+$}
		redirect_to params[:redirect]
	end
end