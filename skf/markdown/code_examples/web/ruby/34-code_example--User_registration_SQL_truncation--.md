# User registration SQL truncation
-------

## Example:


    // Ruby on Rails uses special gem called Devise to handle whole registration (and authentication). This gem makes you invulnerable to SQL truncation.
    // Always remember to enforce better security in the User model (more info: "Password storage"). It is highly recommended to enforce
    // SSL connection during user's signing up and signing in (more info: "Secure session cookies").

    // Examples of models, views and controllers containing registration

    // User model
    class User < ApplicationRecord
      has_many :posts
      // Include default devise modules. Others available are:
      // :confirmable, :lockable, :timeoutable and :omniauthable
      devise :database_authenticatable, :registerable,
            :recoverable, :rememberable, :trackable
    end


    // Registration//new view
    <h2>Sign up</h2>

    <%= simple_form_for(resource, as: resource_name, url: registration_path(resource_name)) do |f| %>
      <%= f.error_notification %>

      <div class="form-inputs">
        <%= f.input :email, required: true, autofocus: true %>
        <%= f.input :password, required: true, hint: ("//{@minimum_password_length} characters minimum" if @minimum_password_length) %>
        <%= f.input :password_confirmation, required: true %>
      </div>

      <div class="form-actions">
        <%= f.button :submit, "Sign up" %>
      </div>
    <% end %>

    <%= render "devise/shared/links" %>

    // Devise has it own registration controller that can be seen here: https://github.com/plataformatec/devise/blob/master/app/controllers/devise/registrations_controller.rb