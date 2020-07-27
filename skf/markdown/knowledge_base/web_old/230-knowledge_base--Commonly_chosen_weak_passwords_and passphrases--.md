##Description:

Whenever an attacker has enumerated usernames from an application the attacker could start
a brute-force attack on the authentication functionality. Whenever users have common known weak
passwords or passphrases there is a high probability that the attacker can compromise 
some of the accounts on the application.

## Solution:

The internet is full of top X worst password lists which can be used to verify the users 
freshly entered password against. Whenever a user enters a password that matches up to a password
provided in one of those lists. The password should be rejected and the user should be advised to take
another password.
