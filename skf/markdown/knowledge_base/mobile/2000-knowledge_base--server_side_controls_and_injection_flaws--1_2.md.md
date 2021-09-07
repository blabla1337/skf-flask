## Description:

Server side controls and Injection Flaws

MSTG-ARCH-2: Security controls are never enforced only on the client side, but on the respective remote endpoints.

An *injection flaw* describes a class of security vulnerability occurring when user input is inserted into backend queries or commands. By injecting meta-characters, an attacker can execute malicious code that is inadvertently interpreted as part of the command or query. For example, by manipulating a SQL query, an attacker could retrieve arbitrary database records or manipulate the content of the backend database.

Vulnerabilities of this class are most prevalent in server-side web services. Exploitable instances also exist within mobile apps, but occurrences are less common, plus the attack surface is smaller.

For example, while an app might query a local SQLite database, such databases usually do not store sensitive data (assuming the developer followed basic security practices). This makes SQL injection a non-viable attack vector. Nevertheless, exploitable injection vulnerabilities sometimes occur, meaning proper input validation is a necessary best practice for programmers.


## Mitigation:

The following two layers of defense should be used in order to prevent injection attacks:
	1. Parameterization - If available, use structured mechanisms that automatically enforce the separation between data and command. These mechanisms can help to provide the relevant quoting, encoding.
	2. Input validation - the values for commands and the relevant arguments should be both validated. There are different degrees of validation for the actual command and its arguments:
		- When it comes to the commands used, these must be validated against a list of allowed commands.
		- In regards to the arguments used for these commands, they should be validated using the following options:
			* Positive or "allow list" input validation - where are the arguments allowed explicitly defined
			* Allow-list Regular Expression - where is explicitly defined a list of good characters allowed and the maximum length of the string. Ensure that metacharacters like & | ; $ > < \ \ !` and white-spaces are not part of the Regular Expression. For example, the following regular expression only allows lowercase letters and numbers, and does not contain metacharacters. The length is also being limited to 3-10 characters: ^[a-z0-9]{3,10}$
