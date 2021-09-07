## Description:

Best Practices for Passwords

MSTG-AUTH-5: A password policy exists and is enforced at the remote endpoint.

Password strength is a key concern when passwords are used for authentication. The password policy defines requirements to which end users should adhere. A password policy typically specifies password length, password complexity, and password topologies. A "strong" password policy makes manual or automated password cracking difficult or impossible.


## Mitigation:

The following characteristics define a strong password:
	- Password Length
	    - **Minimum** length of the passwords should be **enforced** by the application. Passwords **shorter than 8 characters** are considered to be weak ([NIST SP800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html)).
	    - **Maximum** password length should not be set **too low**, as it will prevent users from creating passphrases. A common maximum length is 64 characters due to limitations in certain hashing algorithms, as discussed in the [Password Storage Cheat Sheet](Password_Storage_Cheat_Sheet.md#maximum-password-lengths). It is important to set a maximum password length to prevent [long password Denial of Service attacks](https://www.acunetix.com/vulnerabilities/web/long-password-denial-of-service/).
	- Do not silently truncate passwords. The [Password Storage Cheat Sheet](Password_Storage_Cheat_Sheet.md#maximum-password-lengths) provides further guidance on how to handle passwords that are longer than the maximum length.
	- Allow usage of **all** characters including unicode and whitespace. There should be no password composition rules limiting the type of characters permitted.
	- Ensure credential rotation when a password leak, or at the time of compromise identification.
	- Include password strength meter to help users create a more complex password and block common and previously breached passwords
	    - [zxcvbn library](https://github.com/dropbox/zxcvbn) can be used for this purpose. (Note that this library is no longer maintained)
	    - [Pwned Passwords](https://haveibeenpwned.com/Passwords) is a service where passwords can be checked against previously breached passwords. You can host it yourself or use [API](https://haveibeenpwned.com/API/v3#PwnedPasswords).