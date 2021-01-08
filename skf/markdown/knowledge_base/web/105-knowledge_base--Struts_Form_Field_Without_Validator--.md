##Description:

The application has a form field that is not validated by a corresponding validation form, which can introduce other weaknesses related to insufficient input validation.

Omitting validation for even a single input field may give attackers the leeway they need to compromise the application. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

##Mitigation:


PHASE:Implementation:
Ensure that you validate all form fields. If a field is unused, it is still important to constrain it so that it is empty or undefined.

