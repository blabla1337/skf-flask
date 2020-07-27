##Description:

The product contains an assert() or similar statement that can be triggered by an attacker, which leads to an application exit or other behavior that is more severe than necessary.

While assertion is good for catching logic errors and reducing the chances of reaching more serious vulnerability conditions, it can still lead to a denial of service. For example, if a server handles multiple simultaneous connections, and an assert() occurs in one single connection that causes all other connections to be dropped, this is a reachable assertion that leads to a denial of service.

##Mitigation:


PHASE:Implementation:
Make sensitive open/close operation non reachable by directly user-controlled data (e.g. open/close resources)

PHASE:Implementation:STRATEGY:Input Validation:
Perform input validation on user data.

