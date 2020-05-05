## Description:

The software does not properly control the allocation and maintenance of a limited resource thereby enabling an actor to influence the amount of resources consumed, eventually leading to the exhaustion of available resources.

Limited resources include memory, file system storage, database connection pool entries, and CPU. If an attacker can trigger the allocation of these limited resources, but the number or size of the resources is not controlled, then the attacker could cause a denial of service that consumes all available resources. This would prevent valid users from accessing the software, and it could potentially have an impact on the surrounding environment. For example, a memory exhaustion attack against an application could slow down the application as well as its host operating system. There are at least three distinct scenarios which can commonly lead to resource exhaustion: Lack of throttling for the number of allocated resources Losing all references to a resource before reaching the shutdown stage Not closing/returning resource after processing Resource exhaustion problems are often result due to an incorrect implementation of the following situations: Error conditions and other exceptional circumstances. Confusion over which part of the program is responsible for releasing the resource.

## Mitigation:


PHASE:Architecture and Design:
Design throttling mechanisms into the system architecture. The best protection is to limit the amount of resources that an unauthorized user can cause to be expended. A strong authentication and access control model will help prevent such attacks from occurring in the first place. The login application should be protected against DoS attacks as much as possible. Limiting the database access, perhaps by caching result sets, can help minimize the resources expended. To further limit the potential for a DoS attack, consider tracking the rate of requests received from users and blocking requests that exceed a defined rate threshold.

PHASE:Architecture and Design:
Mitigation of resource exhaustion attacks requires that the target system either: recognizes the attack and denies that user further access for a given amount of time, or uniformly throttles all requests in order to make it more difficult to consume resources more quickly than they can again be freed. The first of these solutions is an issue in itself though, since it may allow attackers to prevent the use of the system by a particular valid user. If the attacker impersonates the valid user, they may be able to prevent the user from accessing the server in question. The second solution is simply difficult to effectively institute -- and even when properly done, it does not provide a full solution. It simply makes the attack require more resources on the part of the attacker.

PHASE:Architecture and Design:
Ensure that protocols have specific limits of scale placed on them.

PHASE:Implementation:
Ensure that all failures in resource allocation place the system into a safe posture.

