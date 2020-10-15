##Description:

There are two popular methods for handling input validation. The first is blacklisting and the second one is the whitelisting method, also known as a positive validation model.
The big disadvantage of the blacklisting model would be that an attacker has a great diversity into forging his attack strings and payloads which can make it hard for your application to detect all of them. It would be very time consuming importing them all into your system.
Whenever you are using a positive validation model you are simply checking for the input you were expecting as defined in your application’s operation, for example:

Let's say you have a form and were expecting it to return the value of a checkbox. This would be a fixed value, yes or no? Whenever the value diverges from the expected input in the applications operation you can assume there was an intercepting proxy tampering these values and act accordingly to it. 
Same goes for whenever you were expecting just a string, integer, alphanumeric character or even special strings such as names as O’Reily.
This method also makes your code clear, transparent and highly maintainable.

##Mitigation:

First there must be a client side input validation method as you would apply to the server
side. This means you should also apply input rejection as well as typecasting and such.
This is to prevent users from being attacked by XSS attacks which are undetectable by
the server.

