# Protecting device memory
-------

## Description:

When critical functionality is loaded into the device memory and always in the same place and location 
then an attacker is able to create a very stable exploit for the application. This can lead to abuse 
of the application business logic or stealing of sensitive information.

## Solution:

A very good and known and proven technology that can be used is ASLR (Address Space Layout Randomisation).
It does this by randomly offsetting the location of modules and certain in-memory structures that will
make the developing of exploits much harder.
