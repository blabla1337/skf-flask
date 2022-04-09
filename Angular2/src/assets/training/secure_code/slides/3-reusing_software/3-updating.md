### Updating Reused Software 

#### Updating Reused Software Components

In practice, you will have many reused software components, and they will need to be updated occasionally. Sometimes a vulnerability will be found in one, in which case you need to be notified quickly and be prepared to rapidly update. As a result, you need to manage reused components:

1. Use package managers, version control systems (such as git), build tools, and automated tests so that you can easily determine exactly what versions you have of every reused component and can rapidly update any of them.

2. Only depend on *documented* interfaces and behavior, and avoid obsolete interfaces, to maximize the likelihood of being able to update reused software when necessary.

3. *Expect* that you will be updating the software you use, including your underlying platform. It is foolish to assume that software will never need to be rapidly updated.

4. Do not modify OSS and create your own “local fork”. If a vulnerability is fixed in a later version of that OSS, it will become increasingly difficult to incorporate that fix. Instead, if you need to modify some OSS to fit your needs, work with the original upstream OSS project to get your improvements incorporated into the official version. Then newer versions of that OSS, including ones that fix vulnerabilities, will also include the capabilities you need.

5. Keep your reused software relatively up-to-date. If your reused components go very far out-of-date, then it may be very difficult to replace a vulnerable version with a fixed version.

6. Monitor to determine if any of the software versions you use has had a publicly-known vulnerability discovered. We will discuss this later in the section on software composition analysis (SCA).

STORY TIME: Equifax

The widely-used program Apache Struts had a critical vulnerability that was fixed on 2017-03-06 and widely reported by the computer press. The data broker Equifax was notified by Apache, US CERT, and the US Department of Homeland Security about the vulnerability, and was provided instructions on how to make the fix. However, Equifax failed to implement a timely update. *“Two months later, Equifax had still failed to patch its systems. It eventually got around to it on July 29. The attackers used the vulnerability to access the company’s databases and steal consumer information on May 13, over two months after Equifax should have patched the vulnerability.” Equifax reported that “145.5 million US customers, about 44% of the [US] population, were impacted by the breach... The attackers got access to … exactly the sort of information criminals can use to impersonate victims to banks, credit card companies, insurance companies, cell phone companies and other businesses vulnerable to fraud. As a result, all 143 million US victims are at greater risk of identity theft, and will remain at risk for years to come. And those who suffer identity theft will have problems for months, if not years, as they work to clean up their name and credit rating.”* (Bruce Schneier, [*Me on the Equifax Breach: Testimony and Statement for the Record of Bruce Schneier*](https://www.schneier.com/blog/archives/2017/11/me_on_the_equif.html),  2017)

#### Updating How You Use Reused Software (Avoid/Replace Obsolete Interfaces)

You not only need  to update components you use, but also how you use them.

When components are updated, they sometimes replace their interface with a new/improved interface over an obsolete/deprecated interface. Where practical, you should avoid or replace any uses of the obsolete/deprecated interfaces of other components. Sometimes the interface is obsolete because of a security vulnerability. In addition, these obsolete interfaces are typically dropped over time, so if you use the obsolete interface, it may be impossible to quickly update if a vulnerability is later found.

If you are obsoleting an interface used by others, do your best to provide a long transition period where both the old and new interfaces are available. Some projects will not be able to easily switch, and it can sometimes take time. Trying to force a rapid update often backfires and causes users to *reject* your updates or delay using them, potentially leading to long-term security problems.

#### Reusing Software: Wrap-up

These are merely tips, and are by no means exhaustive. It is great that we have so much great software to reuse; modern software development would be impossible without them. However, there are a few potential security pitfalls with reused software. The practices we have discussed in this chapter will help you avoid many security problems due to reused software.
