# Input validation

# This class is where you store all your input validation controls.
# It makes it easy to maintain whenever you want to apply changes for
# certain input validation roles and reduces the chance of mistakes in your regexes.

class Validation

	# Application has to protect itself. Every bad input the counter will increment. If the counter
	# hits 3 user's session must be terminated. 
	attr_reader :counter

	def initialize
		@counter = 0
	end

	def validation_failed
			@counter += 1

			# Every bad input validation has to be logged.
			Rails.logger.warn "#{session.id} -> Bad user input"

			if @counter >= 3
				# DO LOGOUT HERE
			end
	end

	def numeric?(input)
		unless input =~ /^[0-9]+$/
			self.validation_failed
			return false
		end

		return true 
	end

	def alphanumeric?(input)
		unless input =~ /^[a-zA-Z]+$/
			self.validation_failed
			return false
		end

		return true 
	end
end