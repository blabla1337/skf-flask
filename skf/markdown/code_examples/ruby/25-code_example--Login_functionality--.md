# Login functionality

# Like in other authenthication cases - Ruby on Rails use a gem called "Devise" to handle login functionality. 
# Use generators below to create required staff
$> rails generate devise:install
$> rails g devise:views
$> rails generate devise User
$> rake db:migrate

# Update your User model in APP_DIR/app/models/user.rb
devise :database_authenticatable, :registerable,
     :recoverable, :rememberable, :trackable, :validatable

# Set routes in APP_DIR/config/routes.rb
devise_for :users

# And finally create login view
<h2>Log in</h2>

<%= simple_form_for(resource, as: resource_name, url: session_path(resource_name)) do |f| %>
  <div class="form-inputs">
    <%= f.input :email, required: false, autofocus: true %>
    <%= f.input :password, required: false, autocomplete: off %> # Remember turning off autocomplete on password field
    <%= f.input :remember_me, as: :boolean if devise_mapping.rememberable? %>
  </div>

  <div class="form-actions">
    <%= f.button :submit, "Log in" %>
  </div>
<% end %>

<%= render "devise/shared/links" %>

# Also, remember turning on HTTPS on login site and setting cookies properly. More info: Secure session cookies.