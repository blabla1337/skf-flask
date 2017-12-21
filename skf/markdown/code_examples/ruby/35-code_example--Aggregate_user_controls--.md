# Aggregate user controls
-------

## Example:


		// First of all, you have to know that Devise gem is AUTHENTICATION gem, not AUTHORIZATION.
		// Using "before_action" in specific controllers will provide only authentication.

		// It is recommended to use authorization gem like Pundit over creating your own code
		// more info: https://github.com/elabs/pundit

		// Quick introduction:

		// 1. Install gem and run generator - `rails g pundit:install`
		// 2. Create policies and update controllers
		// Policy example
			class PostPolicy
				attr_reader :user, :post

				def initialize(user, post)
					@user = user
					@post = post
				end

				def update?
					user.admin? || !post.published?
				end
			end

			// Controller authorization example
			def admin_list
				authorize Post // we don't have a particular post to authorize
				// Rest of controller action
			end

		// 3. Make scopes for policies
		// 4. Ensure if policies and scopes are used
