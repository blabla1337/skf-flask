# Encoder

# Example

# This is the encoder method for whenever you have to allow certain
# possibly dangerous characters into your code for i.e names such as O'reily

class Encoder
  # include SanitizeHelper for the implementation of #sanitize method
  include ActionView::Helpers::SanitizeHelper
  # and this one to provide #sign_out
  include Devise::Controllers::SignInOut

  PATTERN = '^[a-zA-Z0-9%s]+$'.freeze

  attr_reader :store

  # If your application is running on multiple processes or machines make sure you use a key-value backend for Rails cache
  # like Redis or Memcached. If you're using Unicorn/Passenger/Puma in clustered mode you're already running multiple processes!
  # Alternatively you can provide your own implementation backed by either a key-value store or just your database.
  def initialize(store = Rails.cache)
    @store = store
  end

  def encode(user, input, allowed_characters)
    pattern = PATTERN % allowed_characters

    regex = Regexp.compile(pattern)

    unless input =~ regex
      cache_key = cache_key(user)
      store.increment(cache_key)

      # Every bad input validation has to be logged.
      Rails.logger.warn "#{user.id} -> Bad user input"

      if store.fetch(cache_key) >= 3
        sign_out(user)
        store.delete(cache_key)
      end

      return false
    end

    sanitize(input)
  end

  private

  def cache_key(user)
    "#{user.cache_key}/input_counter"
  end
end
