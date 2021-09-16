## Description:

Local Storage for Sensitive Data 

MSTG-STORAGE-1: System credential storage facilities need to be used to store sensitive data, such as PII, user credentials or cryptographic keys.

MSTG-STORAGE-2: No sensitive data should be stored outside of the app container or system credential storage facilities.

Conventional wisdom suggests that as little sensitive data as possible should be stored on permanent local storage. In most practical scenarios, however, some type of user data must be stored. For example, asking the user to enter a very complex password every time the app starts isn't a great idea in terms of usability. Most apps must locally cache some kind of authentication token to avoid this. Personally identifiable information (PII) and other types of sensitive data may also be saved if a given scenario calls for it.

Sensitive data is vulnerable when it is not properly protected by the app that is persistently storing it. The app may be able to store the data in several places, for example, on the device or on an external SD card. When you're trying to exploit these kinds of issues, consider that a lot of information may be processed and stored in different locations. Identifying at the outset the kind of information processed by the mobile application and input by the user is important. Identifying information that may be valuable to attackers (e.g., passwords, credit card information, PII) is also important.

Disclosing sensitive information has several consequences, including decrypted information. In general, an attacker may identify this information and use it for additional attacks, such as social engineering (if PII has been disclosed), account hijacking (if session information or an authentication token has been disclosed), and gathering information from apps that have a payment option (to attack and abuse them).


## Mitigation:

The following checks should be performed:

	- Analyze data storage in the source code.
	- Be sure to trigger all possible functionality in the application (e.g. by clicking everywhere possible) in order to ensure data generation.
	- Check all application generated and modified files and ensure that the storage method is sufficiently secure.
	- This includes SharedPreferences, SQL databases, Realm Databases, Internal Storage, External Storage, etc.

In general sensitive data stored locally on the device should always be at least encrypted, and any keys used for encryption methods should be securely stored within KeyChain (iOS) or KeyStore (Android). These files should also be stored within the application sandbox. If achievable for the application, sensitive data should be stored off device or, even better, not stored at all.
