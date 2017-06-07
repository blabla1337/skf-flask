# Brute-force password guessing
-------

## Description:

Login functions should not be abused in an automated way that an attacker could create a
script that contains a list of usernames and passwords, which he could use against your
login function in order to gain unauthorized access to user accounts.

## Solution:

Implement a method that limits the amount of tries with automated tools.
Some examples are using a CAPTCHA or a TARPIT(rate-limiting) method.
