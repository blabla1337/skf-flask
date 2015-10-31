Differential analysis attack
-------

**Description:**

Whenever an attacker sends a request to the server, in example by means of an 
authentication functionality then they can measure the average response time between a request
containing a valid username and a request containing a invalid username. The
attacker can now use this differential in response time to enumerate user accounts.


**Solution:**

Verify that all authentication challenges, whether successful or failed, should respond 
in the same average response time.





   
