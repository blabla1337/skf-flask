Identify all external dependencies
-------

**Description:**

Sometimes your application has certain external dependencies which may strongly
influence your application's operation. These external dependencies
might become an attackers target since compromising that service might lead to
a DoS of your system or influence the system in such a way it leaves room for other 
attacks.

**Solution:**

First you must identify which external dependencies your application relays on 
for its operation. Second, there should be a fail safe implemented should this dependency ever
fail to deliver its services towards your application. 



   
