
Input rejection
-------

**Description:**

Whenever the application detects malicious or unexpected user-input you want to make sure 
the application actual rejects the submitted user-input rather than directly process it. 


**Solution:**

Verify that the application actually rejects the user requests whenever malicious input
is detected by your application. The base of this process will be checking the application
for expected user-input, for example: Whenever the user is filling in a form which 
contains a checkbox, there are fixed values which your application can expect from
the user to return. Whenever this value differs from what the application served the user
as possible answers, you can assume the request was corrupted and you reject the request.

You must also keep track of the users movements by adding an audit trail as well as an
counter for tracking the number of his violations(submitting bad input) in your input 
validation class. You should enforce a lockout whenever a unreasonable number of 
violations are detected by your application in order to protect it from attackers.

Recommended knowledge base items:

- Input validation
- Client side input validation
- Single input validation controls
- Character encoding
