##Description:

The product's physical debug and test interface protection does not block untrusted agents, resulting in unauthorized access to and potentially control of sensitive assets.

If the product implements access-control protection on the debug and test interface, a debugger is typically required to enter either a valid response to a challenge provided by the authorization logic or, alternatively, enter the right password in order to exercise the debug and test interface. However, if this protection mechanism does not exclude all untrusted, debug agents, an attacker could access/control security-sensitive registers.

##Mitigation:


PHASE:Architecture and Design Implementation:
For security-sensitive assets accessible over debug/test interfaces, only allow trusted agents.

