##Description:

After completing a password recovery functionality, the user should not be sent a plaintext
password to his email adress. The application should also under no circumstances disclose the old or current password
to the users.

## Solution:

The application should under no circumstances disclose the users current, old and new password plain text.
This behavior makes the application susceptible to side channel attacks and make the passwords
lose their integrity since they could be compromised by someone looking over another users shoulder to
see the password. 
