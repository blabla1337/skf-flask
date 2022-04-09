### Countering Denial-of-Service (DoS) Attacks

Secure systems should be available to authorized users even while under attack. This is especially difficult if your system can be accessed via the public internet. Attackers may be able to launch a distributed DoS (DDoS) attack from many systems they control, creating millions or billions of requests. If an attacker has many resources, you may not be able to counter the attack *except* by using significant resources (including money) to handle the workload.

One approach is to design your system to be able to handle larger amounts of traffic. That way, attacker requests will simply be handled. Design your system to be scalable (e.g., through containerization) and deploy on a cloud system where you can automatically (or at least rapidly) scale up to much larger sizes if there is demand. Use caches, Content Delivery Networks (CDNs), and minimize execution time per request so that more requests can be handled each second. Consider using a static site where this kind of website is a viable option. There are many ways to minimize execution time (aka increase performance); for many systems, maximal use of database indexes and eliminating so-called “N+1” queries is a good first step.

However, at some point an attacker who controls enough resources will be able to overwhelm most services unless you are willing to spend a large amount of money to handle them. So another approach is to rapidly recover from excessive attacker-caused demand. Make sure your restart can be automated and that your system can restart relatively quickly. Where it is sensible, have a “backoff” mode (e.g., a read-only mode or separate service) so that *some* services are available during an aggressive attack.

Another way to make DoS attacks more difficult is to reduce the amount of resources your application requires. If resources are temporarily required (e.g., file handles, etc.), make sure their allocation and consumption is controlled and that they are returned when no longer needed. In addition, avoid “losing” resources. Memory is a resource automatically managed by many languages, but many other resources are not or are easily lost. If you have to manually return a resource in a language with exception handling, ensure that the resources are returned *even* when an exception is thrown.

There are several kinds of (related) resource handling vulnerabilities, and any of them can eventually lead to a denial of service. What is more, they are common problems:

* *Uncontrolled Resource Consumption* ([CWE-400](https://cwe.mitre.org/data/definitions/400.html)) is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #20. 

* This is highly related to having a missing release of resources, 2019 CWE Top 25 #21, [CWE-772](https://cwe.mitre.org/data/definitions/772.html), *Missing Release of Resource after Effective Lifetime*.

* *Allocation of Resources Without Limits or Throttling* ([CWE-770](https://cwe.mitre.org/data/definitions/770.html)) is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #39.  

An obvious but surprisingly common problem is loops where an attacker can cause the exit condition to never occur, causing the program to get stuck in an infinite loop without getting work done.

Loops with unreachable exit conditions are 2019 CWE Top 25 #26, [CWE-835](https://cwe.mitre.org/data/definitions/835.html).

Make sure that you have backups of important datasets and a workable recovery process. That way, if an attacker manages to shut down the whole system, the data loss will be minimized. If necessary, you could even restart the service somewhere else or in some other form using the backups. You should have multiple backups, and at least some older ones should be in *cold storage* (that is, the backups cannot be modified by a later computer attack). That way, if newer backups are corrupted by an attacker (such as by using a ransomware attack), there are backups that can still be used.