## Miscellaneous

### Assurance Cases

Sadly, you cannot just do one thing and make a system secure. Instead, you need to do a variety of things. Tracking the various techniques you need to do, to ensure that you are really addressing everything you think you should, can become overwhelming… especially if your software gets large or there are expectations of strong security. In addition, sometimes potential stakeholders (such as users) want to understand what you are doing in order to determine if you are doing enough for their purposes. An unstructured list of “*things that were done*” does not really help when a system gets larger; you might do many things, but fail to address something important.

A practical alternative is creating an *assurance case*. An assurance case *“includes a top-level  claim for a property of a system or product (or set of claims), systematic argumentation regarding this claim, and the evidence and explicit assumptions that underlie this argumentation”* ([ISO/IEC 15026-2:2011](https://www.iso.org/standard/52926.html)). Let’s look at that definition; put another way, an assurance case includes:

* Claim(s): Top-level claim(s) for a property of a system or product. That is, something that you want to be true.

* Arguments: A systematic argumentation justifying this claim.

* Evidence/assumptions: Evidence and explicit assumptions underlying the argument.

The point of an assurance case is that it is *systematic*. In other words, you should start with whatever claim(s) you want to make that are important, and repeatedly break that down to show that the claim is true. Imagine that you are a lawyer trying to make a case to a skeptical jury; your job is to justify that the claim(s) are true. Creating an assurance case helps you determine and justify to people that the software is secure, both to others and yourself.

An assurance case does not have to be in any particular form. However, they are often documents with figures showing the high-level structure, and text providing the details. That is simply because it is easy to glance at the figures to see how things work together, but the text provides the details to really understand things.

Let’s talk about one way to create an assurance case, based on material from [*A Sample Security Assurance Case Pattern*](https://www.ida.org/-/media/feature/publications/a/as/a-sample-security-assurance-case-pattern/p-9278.ashx) by David A. Wheeler (2018). Let’s say that we have an overall claim: we want to claim that our “system is adequately secure against moderate threats”. Let’s argue that we can provide adequate proof of this if our security requirements are identified and met by its functionality, and that security is implemented by system life cycle processes. We can break down the security requirements further into our security requirement triad (confidentiality, integrity, and availability), properly handling access control, and identifying and addressing the assets and threat actors. Here is a figure that shows the top level of an assurance case:

![image alt text](../../top_assurance_case.png)

**Sample top level of an assurance case**, by David A. Wheeler (2018)

We could then repeatedly break each item down further. For example, we might divide the lifecycle processes into areas like design, implementation, and verification. We could then explain how we address security in each:

* For design, we might show that we followed all the Saltzer & Schroeder (S&S) design principles we have already discussed.

* For implementation, we might show that we countered all the “top” vulnerabilities identified by some widely-accepted and relevant list of top vulnerabilities.

* For verification, we might show that we use a variety of tools to detect vulnerabilities before the software is released. 

For a detailed discussion and template for creating an assurance case, see [*A Sample Security Assurance Case Pattern*](https://www.ida.org/-/media/feature/publications/a/as/a-sample-security-assurance-case-pattern/p-9278.ashx) by David A. Wheeler (2018). If you would like to see an actual example, you can see the [OpenSSF Best Practices BadgeApp assurance case](https://github.com/coreinfrastructure/best-practices-badge/blob/master/doc/security.md).

When do you end? The usual answer is when the stakeholders agree that it is enough. If they don’t think it is enough, then ask them what would be enough and if they are willing to pay for those changes. If they are not paying you enough, then you don’t need to do it.

What is great about an assurance case is that if someone later wants to know “is this software adequately secure”, they can simply review the assurance case. Simply *having* an assurance case provides a lot of confidence, because it shows that someone thought through what the system is supposed to do and has a reasonable argument (with evidence) that the claims are correct.