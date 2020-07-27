##Description:

The software does not follow, or incorrectly follows, the chain of trust for a certificate back to a trusted root certificate, resulting in incorrect trust of any resource that is associated with that certificate.

If a system does not follow the chain of trust of a certificate to a root server, the certificate loses all usefulness as a metric of trust. Essentially, the trust gained from a certificate is derived from a chain of trust -- with a reputable trusted entity at the end of that list. The end user must trust that reputable source, and this reputable source must vouch for the resource in question through the medium of the certificate. In some cases, this trust traverses several entities who vouch for one another. The entity trusted by the end user is at one end of this trust chain, while the certificate-wielding resource is at the other end of the chain. If the user receives a certificate at the end of one of these trust chains and then proceeds to check only that the first link in the chain, no real trust has been derived, since the entire chain must be traversed back to a trusted source to verify the certificate. There are several ways in which the chain of trust might be broken, including but not limited to: Any certificate in the chain is self-signed, unless it the root. Not every intermediate certificate is checked, starting from the original certificate all the way up to the root certificate. An intermediate, CA-signed certificate does not have the expected Basic Constraints or other important extensions. The root certificate has been compromised or authorized to the wrong party.

##Mitigation:


PHASE:Architecture and Design:
Ensure that proper certificate checking is included in the system design.

PHASE:Implementation:
Understand, and properly implement all checks necessary to ensure the integrity of certificate trust integrity.

PHASE:Implementation:
If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the full chain of trust.

