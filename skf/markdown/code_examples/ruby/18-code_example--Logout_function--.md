# Logout function

# Example

# It is highly recommended to use Devise gem that handles authentication on your RoR app.
# more info: https://github.com/plataformatec/devise

# When all authentication is done by Devise gem the implement logout function is as simple as
# adding the link into your base template. For my application this is 
# APP_DIR/views/layouts/application.html.haml

%ul.nav.navbar-nav.navbar-right
- if user_signed_in?
  %li= link_to "New Post", new_post_path
  %li= link_to "Sign out", destroy_user_session_path, method: :delete # Logout function
- else
  %li= link_to "Sign in", new_user_session_path
  %li= link_to "Sign up", new_user_registration_path

# Also, remember about authenticate in controllers before performing any action in specific controllers
before_action :authenticate_user!, only: [Methods_here] 