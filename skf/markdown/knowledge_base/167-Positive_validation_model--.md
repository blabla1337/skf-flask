Positive validation model
-------

**Description:**

There are two populair methods in handeling input validation. The first is blacklisting
and the second one is the whitelisting method, also known as a positive validation model.

The big disadvantage of the blacklisting model would be that an attacker has a great
diversity into forging his attack strings and payloads which can make it hard for your
application to detect al of them. It would also be very time consuming importing al of 
them into your system.

Whenever you are using a positive validation model you are simply checking for the input 
you were expecting as defined in your applications operation, for example:

Let's say you have a form and was expecting the form to return the value of a checkbox.
This would be a fixed value, yes or no. Whenever the value diverges of the expected
input as was intended in the applications operation you can now assume there was an
intercepting proxy tampering these values and act accordingly to it.

Same goes for whenever you were expecting just a string, integer, alphanumeric character
or even special strings such as names as an o'reily.

This methods also makes your code clear, transparant and highly maintainable.

**Solution:**

First there must be a client side input validation method as you would apply to the server
side. This means you should also apply input rejection as wel as typecasting and such.
This is to prevent users from being attacked by XSS attacks which are undetectable by
the server.

Recommended knowledge base items:
- Single input validation controls
- Input rejection
- Input validation




   
