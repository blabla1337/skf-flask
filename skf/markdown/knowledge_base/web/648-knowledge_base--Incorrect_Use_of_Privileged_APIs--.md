##Description:

The application does not conform to the API requirements for a function call that requires extra privileges. This could allow attackers to gain privileges by causing the function to be called incorrectly.

When an application contains certain functions that perform operations requiring an elevated level of privilege, the caller of a privileged API must be careful to: ensure that assumptions made by the APIs are valid, such as validity of arguments account for known weaknesses in the design/implementation of the API call the API from a safe context If the caller of the API does not follow these requirements, then it may allow a malicious user or process to elevate their privilege, hijack the process, or steal sensitive data. For instance, it is important to know if privileged APIs do not shed their privileges before returning to the caller or if the privileged function might make certain assumptions about the data, context or state information passed to it by the caller. It is important to always know when and how privileged APIs can be called in order to ensure that their elevated level of privilege cannot be exploited.

##Mitigation:


PHASE:Implementation:
Before calling privileged APIs, always ensure that the assumptions made by the privileged code hold true prior to making the call.

PHASE:Architecture and Design:
Know architecture and implementation weaknesses of the privileged APIs and make sure to account for these weaknesses before calling the privileged APIs to ensure that they can be called safely.

PHASE:Implementation:
If privileged APIs make certain assumptions about data, context or state validity that are passed by the caller, the calling code must ensure that these assumptions have been validated prior to making the call.

PHASE:Implementation:
If privileged APIs do not shed their privilege prior to returning to the calling code, then calling code needs to shed these privileges immediately and safely right after the call to the privileged APIs. In particular, the calling code needs to ensure that a privileged thread of execution will never be returned to the user or made available to user-controlled processes.

PHASE:Implementation:
Only call privileged APIs from safe, consistent and expected state.

PHASE:Implementation:
Ensure that a failure or an error will not leave a system in a state where privileges are not properly shed and privilege escalation is possible (i.e. fail securely with regards to handling of privileges).

