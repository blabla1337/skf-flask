##Description:

The code uses a cache that contains sensitive information, but the cache can be read by an actor outside of the intended control sphere.

Applications may use caches to improve efficiency when communicating with remote entities or performing intensive calculations. A cache maintains a pool of objects, threads, connections, pages, ficial data, passwords, or other resources to minimize the time it takes to initialize and access these resources. If the cache is accessible to unauthorized actors, attackers can read the cache and obtain this sensitive information.

##Mitigation:


PHASE:Architecture and Design:
Protect information stored in cache.

PHASE:Architecture and Design:
Do not store unnecessarily sensitive information in the cache.

PHASE:Architecture and Design:
Consider using encryption in the cache.

