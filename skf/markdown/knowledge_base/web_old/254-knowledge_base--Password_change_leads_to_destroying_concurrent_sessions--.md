##Description:

Whenever a user changes his password, the user should be granted the option
to kill all other concurrent sessions. This countermessure helps to exclude
potential attackers living on a hijacked session.

Note: Whenever users are granted the possibility to change their passwords,
      do not forget to make them re-authenticate or to use a form of step up
      or adaptive authentication mechanism.

## Solution:

Verify the user is prompted with the option to terminate all other active sessions 
after a successful change password process.
