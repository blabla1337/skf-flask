
All authentication controls must fail securely
-------

**Description:**

Whenever there are multiple authentication controls in place in a web application all of 
these controls must be verified to fail securely in order to prevent an attacker gaining 
unauthorised access due to one of these controls not failing securely.


**Solution:**

Make sure all the access control systems are thoroughly tested for failing securely before 
using it in your application. It is common that Unit-test are created especially 
for this purpose.
