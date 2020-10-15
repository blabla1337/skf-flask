##Description:

Whenever an attacker sends a request to the server, an example by means of
authentication functionality. He can measure the average response time between a request
containing a valid username and a request containing a invalid username. The
attacker can now use this differential in response time to enumerate user accounts.

##Mitigation:

Verify that all authentication challenges, whether successful or failed, should respond
in the same average response time. This same methodology applies for other sensitive information that could
potentially be recovered with differential attacks.
