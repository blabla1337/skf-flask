# Aggregate user controls
-------

## Example:


    // First of all, you have to know that Devise gem is AUTHENTICATION gem, not AUTHORIZATION.
    // Using "before_action" in specific controllers will provide only authentication.

    // It is recommended to use authorization gem like Pundit over creating your own code
    // more info: https://github.com/elabs/pundit

    // However, for simple privilege based authentication we can use simpler gem like Petergate
    // more info: https://github.com/elorest/petergate

    // Quick introduction to Petergate gem:
    // 1. Use this generators
    $> rails g petergate:install
    $> rake db:migrate
    // 2. Configure roles in user.rb
    petergate(roles: [:admin, :editor], multiple: false)
    // 3. Setup permissions in the specific controller
    def YourController < ApplicationController
      access all: [:show, :index], user: {except: [:destroy]}, company_admin: :all
    end
