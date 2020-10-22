# Enforce sequential step order 
-------

## Example:


	// Whenever an functionality consists out of following several steps to achieve some goal i.e,
	// "User adds items to chart", "User enters shipping information", "User pays for goods",
	// "Items will be shipped." You want to make sure the user can not skip the payment step in
	// order to receive his goods.

	class Product < ApplicationRecord
	end

	class Order < ApplicationRecord
		has_many :products, through: :products_orders

		belongs_to :customer
		belongs_to :payment
	end

	// As you can see above we have a very simplified database structure for your average
	// web shop. now we can walk through the different steps needed to enforce the user to take
	// all steps before payment.
	//
	// We wont cover the entire shopping cart functions since that would become a rather big
	// example so let's cover the basics of enforcing the sequential steps.
	//
	// Step1: would be, the user adding items to his cart.
	//
	// Step2: would be, the user adding products to checkout. Whenever he is done shopping
	// we'll change the state of the Order
	//
	// For managing the state we could use a Ruby gem that implements an interface
	// for a state machine, like Statesman (https://github.com/gocardless/statesman)
	// It even provides adapters for ActiveRecord models and can save the entire
	// state transition history for later audit.

	// First, we should create a state machine:
	class OrderStateMachine
		include Statesman::Machine

		state :pending, initial: true
		state :checking_out
		state :purchased
		state :cancelled

		transition from: :pending,      to: [:checking_out, :cancelled]
	transition from: :checking_out, to: [:purchased, :cancelled]
	end

	// Then, we can link it to our ActiveRecord model:
	class Order < ApplicationRecord
		include Statesman::Adapters::ActiveRecordQueries

		has_many :order_transitions, autosave: false
		has_many :products, through: :products_orders

		belongs_to :customer
		belongs_to :payment

		// Optionally delegate some methods
		delegate :can_transition_to?, :transition_to!, :transition_to, :current_state,
			to: :state_machine

		def state_machine
			@state_machine ||= OrderStateMachine.new(self, transition_class: OrderTransition)
		end

		def self.transition_class
			OrderTransition
		end

		def self.initial_state
			:pending
		end
		private_class_method :initial_state
	end

	// Next, lets create an AR model to represent state transitions:
	class OrderTransition < ActiveRecord::Base
	include Statesman::Adapters::ActiveRecordTransition

	belongs_to :order, inverse_of: :order_transitions
	end

	// And lets put the following code into confing/initializers/statesman.rb
	// So that Statesman knows it should persist the state to DB
	Statesman.configure do
	storage_adapter(Statesman::Adapters::ActiveRecord)
	end

	// Now in your controllers you can use the following methods:
	// - Machine//can_transition_to?(state): true|false
	// - Machine//transition_to(state): true|false
	// - Machine//transition_to!(state): true|Statesman::TransitionFailedError|Statesman::GuardFailedError
	order = Order.create!

	order.current_state
	// => pending

	order.can_transition_to?(:purchased)
	// => false

	order.transition_to(:purchased)
	// => false

	// order still in the pending state:
	order.current_state
	// => pending

	// You definitely should check out the gem's Github page (https://github.com/gocardless/statesman)
	// as it has a great README with a more broad example
    