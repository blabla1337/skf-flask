## Description:

The software receives a request, message, or directive from an upstream component, but the software does not sufficiently preserve the original source of the request before forwarding the request to an external actor that is outside of the software's control sphere. This causes the software to appear to be the source of the request, leading it to act as a proxy or other intermediary between the upstream component and the external actor.

If an attacker cannot directly contact a target, but the software has access to the target, then the attacker can send a request to the software and have it be forwarded from the target. The request would appear to be coming from the software's system, not the attacker's system. As a result, the attacker can bypass access controls (such as firewalls) or hide the source of malicious requests, since the requests would not be coming directly from the attacker. Since proxy functionality and message-forwarding often serve a legitimate purpose, this issue only becomes a vulnerability when: The software runs with different privileges or on a different system, or otherwise has different levels of access than the upstream component; The attacker is prevented from making the request directly to the target; and The attacker can create a request that the proxy does not explicitly intend to be forwarded on the behalf of the requester. Such a request might point to an unexpected hostname, port number, or service. Or, the request might be sent to an allowed service, but the request could contain disallowed directives, commands, or resources.

## Mitigation:


PHASE:Architecture and Design:
Enforce the use of strong mutual authentication mechanism between the two parties.

