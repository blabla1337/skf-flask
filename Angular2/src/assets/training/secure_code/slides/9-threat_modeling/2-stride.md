### STRIDE

An easy design-centric approach is one developed by Microsoft called STRIDE. We will cover STRIDE here, because it is better to know one simple approach that helps than a complex system that may be too hard to use. In the literature this version is called *STRIDE-by-element*. See Robert Reichel’s [*How we threat model*](https://github.blog/2020-09-02-how-we-threat-model/) (2020) for a discussion of how GitHub uses STRIDE.

Microsoft recommends doing the following steps for any threat modeling (attack modeling) approach ([Microsoft Threat Modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)):

1.  Define security requirements. 

2.  Create an application diagram. 

3.  Identify threats. 

4.  Mitigate threats. 

5.  Validate that threats have been mitigated.

When applying STRIDE in step 2, you need to create a simple representation of your design. Typically, this is done by creating a simple data flow diagram (DFD) (for more details, see [*Threat Modeling: 12 Available Methods*](https://insights.sei.cmu.edu/sei_blog/2018/12/threat-modeling-12-available-methods.html), by Nataliya Shevchenko, 2018):

1. Data processes are represented with circles

2. Data stores are represented with lines above and below their names (you may also see them as cylinders)

3. Data flows are represented with directed lines; these include data flows over a network

4. Interactors (items that are outside your system and interact with it) typically have simple icons, such as a stick figure for a human

5. Trust boundaries are represented with a dashed line; these represent the border between trusted and untrusted portions.

Elements are everything except the trust boundaries. That is, processes, data stores, data flows, and interactors are all elements.

The idea is to have a simple model of the design that shows the essential features. Here are some quick rules of thumb for a good representation:

* Every data store should have at least one input and at least one output (“no data coming out of thin air”).

* Only processes read or write data in data stores (“no psychokinesis”)

* Similar elements in a single trust boundary can be collapsed into one element (“make the model simple”).

Then, when applying STRIDE in step 3, you examine each of the elements (processes, data stores, data flows, and interactors) to determine what threats it is susceptible to. For each element, you look for the threats as shown in this table:

![image alt text](../../stride_threat_categories.png)

**STRIDE Threat Categories**, retrieved from [SEI](https://insights.sei.cmu.edu/sei_blog/2018/12/threat-modeling-12-available-methods.html), originally from Microsoft

Notice that “STRIDE” is simply an acronym for the threats being considered: Spoofing, Tampering, Repudiation, Information disclosure, Denial of Service, and Elevation of privilege.

STRIDE is one of the oldest, most well-known, and simplest forms of threat modeling ([*Threat Modeling: Uncover Security Design Flaws Using the STRIDE Approach*](https://web.archive.org/web/20070303103639/http://msdn.microsoft.com/msdnmag/issues/06/11/ThreatModeling/default.aspx), by Shawn Hernan, Scott Lambert, Tomasz Ostwald, and Adam Shostack, 2006). There are tools you can use that are designed to support STRIDE; you can also use STRIDE with basic tools such as a drawing tool, word processor, and/or spreadsheet.

As we noted earlier, there are other approaches. Feel free to learn or use them instead if they help you. The Software Engineering Institute (SEI) has even written some analyses of the various approaches, including their pros and cons ([Shevchenko, 2018](https://insights.sei.cmu.edu/sei_blog/2018/12/threat-modeling-12-available-methods.html)). Microsoft has also written some material on [threat modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling).

Threat modeling is overkill if you do not have significant security threats, and threat modeling does not guarantee you will find all the problems. That said, if you have significant security threats, threat modeling using approaches like STRIDE can provide a relatively simple way to think through key questions before you invest a lot of time.