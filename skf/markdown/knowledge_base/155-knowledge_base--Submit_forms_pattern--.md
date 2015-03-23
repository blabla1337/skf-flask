
Submit forms - pattern
-------

**Description:**

Whenever a user can submit a form in your system you should consider implementing
the following defence mechanism in order to ensure high level security.

1.  Single user input validation controls and Audit logs
2.  CSRF tokens
3.  Principle of least privilege
4.  GET/POST requests




**Solution:**

Here are the steps described briefly.
For more detailed information you should look into these items in the knowledge base.
 
First, you should create a single user input validation control class which should 
validate the expected input values in order to verify if the user is not tampering data 
or is injecting malicious code into your application. All infringements should be logged
and repercussions should be taken whenever these infringements are frequent. 

Second, whenever an authenticated user is submitting the form always ensure the forms
contain CSRF tokens in order to prevent cross site request forgery.

Third, Whenever there are authenticated users with different roles/privileges you should
enforce restrictions on the server side upon your form submits/processing in order 
to prevent privilege escalation. You should apply the principle of least privilege in 
order to ensure higher level of security.

Fourth, Whenever the application is sending sensitive data through the form submit
this data must always be send through an POST variable instead of an GET since
a GET will leak this data through the url by example the referer header.