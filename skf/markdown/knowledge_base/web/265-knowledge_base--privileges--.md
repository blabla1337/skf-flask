##Description:

Weaknesses in this category occur with improper handling, assignment, or management of privileges. A privilege is a property of an agent, such as a user. It lets the agent do things that are not ordinarily allowed. For example, there are privileges which allow an agent to perform maintenance functions such as restart a computer.


##Mitigation:


This can strongly overlap authorization errors.

Many of the following concepts require deeper study. Most privilege problems are not classified at such a low level of detail, and terminology is very sparse. Certain classes of software, such as web browsers and software bug trackers, provide a rich set of examples for further research. Operating systems have matured to the point that these kinds of weaknesses are rare, but finer-grained models for privileges, capabilities, or roles might introduce subtler issues.

A sandbox could be regarded as an explicitly defined sphere of control, in that the sandbox only defines a limited set of behaviors, which can only access a limited set of resources.
