## Consider Availability on All Inputs

### Consider Availability on All Inputs

As we discussed before, it is often difficult to guarantee availability in all possible circumstances. For example, if a system is publicly accessible over the Internet, an attacker could initiate a large-scale distributed denial-of-service (DDoS) attack, overwhelming your service’s resources.

But once you start considering availability as a risk management problem, things are not so dire. You want to reduce the risk from DoS attacks, that is, reduce their likelihood or impact. You can reduce the likelihood by making the attack more difficult, risky, or resource-intensive for the attacker.

#### Try to Eliminate Easily Amplified Inputs

A useful concept is the idea of leverage. *“In the context of a DoS attack, if a vulnerability has high leverage it means attackers can consume a ton of your server resources with minimal resources… the higher the leverage, the higher the risk, and the more likely I am to address the issue directly. The lower the leverage, the more likely I’ll accept the risk and/or lean on [other] mitigations.”* ([*Not all attacks are equal: understanding and preventing DoS in web applications*](https://r2c.dev/blog/2020/understanding-and-preventing-dos-in-web-apps/), by Jacob Kaplan-Moss, 2020)

Consider each kind of input your software receives. Is there any way an attacker can send a very small amount of input and consume a large amount of resources (e.g., computation and/or output)? These are often higher risk to availability, because these inputs are easily amplified.

Here are some examples of resources an input might disproportionately consume:

* Network bandwidth — e.g., an input can produce a disproportionately large output.

* CPU utilization — e.g., an input can cause large amounts of computation; we have seen an example of that earlier in ReDoS.

* Storage space — e.g., a compressed file might expand to fill storage.

* Concurrency limits — e.g., an input can cause a thread/process to run slowly, causing the software to reach concurrency maximums (e.g., the number of threads, processes, or database connections). 

The risks of these can be reduced via authentication, since then attackers have to expose some information about themselves. In general, try to eliminate at least the unauthenticated ones, and consider requiring some kind of authentication for the rest ([*Not all attacks are equal: understanding and preventing DoS in web applications*](https://r2c.dev/blog/2020/understanding-and-preventing-dos-in-web-apps/), by Jacob Kaplan-Moss, 2020).

One partial solution to reduce network bandwidth is *paging*. That is, instead of returning a very large result, return smaller results each time. This requires the attacker to repeatedly make requests.

If you cannot eliminate highly amplified inputs, try to distribute the load. For example, if you are distributing large files, consider using a Content Delivery Network (CDN), torrent, or other such system. Many websites use CDNs so that simple requests with potentially-large replies do not overwhelm their servers.

#### Rate Limiting

A simple widely-used approach on networked systems to improve availability is rate limiting. Rate limiting limits the rate of input requests (e.g., for a given user, API key, or IP address). As long as the rate limits are relatively high, rate limits don’t significantly impact normal use, and they can make single-system DoS attacks much less effective. In some cases, rate limits can even provide a partial countermeasure against DDoS attacks (since they may reduce the effectiveness of each attacking system). Rate limiting also counters some accidental problems.

Note that if you force attackers to make many requests (e.g., via paging), the attacker may start to hit rate limits.

Rate limiting is not a complete solution, but it is an easy and inexpensive approach that increases the costs and efforts for attackers.