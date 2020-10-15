##Description:

An important aspect of secure application development is to prevent information leakage. 
Error messages give an attacker great insight into the inner workings of an application.

The purpose of reviewing the Error Handling code is to assure the application fails safely under all 
possible error conditions, expected and unexpected. No sensitive information is presented to the user 
when an error occurs.

When an exception or error is thrown we also need to log this occurrence. Sometimes this is due to bad
development, but it can be the result of an attack or some other service your application relies on failing.

All code paths that can cause an exception to be thrown should check for success in order for the exception 
not to be thrown.

##Mitigation:

We should use a localized description string in every exception, a friendly error reason such as “System Error – Please try again later”. When the user sees an error message, it will be derived from this description string of the exception that was thrown, and never from the exception class which may contain a stack trace, line number where the error occurred, 
class name or method name.

Do not expose sensitive information in exception messages. Information such as paths on the local file system is considered privileged information; any system internal information should be hidden from the user. As mentioned before an attacker could use this information to gather private user information from the application or components that make up the app.

Don’t put people’s names or any internal contact information in error messages. Don’t put any “human” information, which would lead to a level of familiarity and a social engineering exploit.

Another good example would be for password forget functions to throw a generic error message when a email adress
is or is not known on the system. This should prevent enumeration of email adresses.

