##Description:

The product implements a protection mechanism that relies on a list of inputs (or properties of inputs) that are not allowed by policy or otherwise require other action to neutralize before additional processing takes place, but the list is incomplete, leading to resultant weaknesses.

Developers often try to protect their products against malicious input by performing tests against inputs that are known to be bad, such as special characters that can invoke new commands. However, such lists often only account for the most well-known bad inputs. Attackers may be able to find other malicious inputs that were not expected by the developer, allowing them to bypass the intended protection mechanism.

##Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
Do not rely exclusively on detecting disallowed inputs. There are too many variants to encode a character, especially when different environments are used, so there is a high likelihood of missing some variants. Only use detection of disallowed inputs as a mechanism for detecting suspicious activity. Ensure that you are using other protection mechanisms that only identify good input - such as lists of allowed inputs - and ensure that you are properly encoding your outputs.

