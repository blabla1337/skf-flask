## Description:

## Control Objective

V2: Data Storage and Privacy Requirements

The protection of sensitive data, such as user credentials and private information, is a key focus in mobile security. Firstly, sensitive data can be unintentionally exposed to other apps running on the same device if operating system mechanisms like IPC are used improperly. Data may also unintentionally leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, so an adversary gaining physical access is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.

Note that, as the MASVS is app-centric, it does not cover device-level policies such as those enforced by MDM solutions. We encourage the use of such policies in an Enterprise context to further enhance data security.


### Definition of Sensitive Data

Sensitive data in the context of the MASVS pertains to both user credentials and any other data considered sensitive in the particular context, such as:
	- Personally identifiable information (PII) that can be abused for identity theft:  Social security numbers, credit card numbers, bank account numbers, health information;
	- Highly sensitive data that would lead to reputational harm and/or financial costs if compromised: Contractual information, information covered by non-disclosure agreements, management information;
	- Any data that must be protected by law or for compliance reasons.


## Mitigation:

empty control