### What Is Privacy and Why It Is Important

Security and privacy are interrelated, but not the same thing. In this unit we will cover what privacy is, its relationship to security, and why privacy is important.

#### What Does Privacy Mean?

The non-profit [International Association of Privacy Professionals (IAPP) defines privacy](https://iapp.org/about/what-is-privacy/) as *“the right to be let alone, or freedom from interference or intrusion”*. More specifically, it says *“Information privacy is the right to have some control over how your personal information is collected and used... various cultures have widely differing views on what a person’s rights are when it comes to privacy and how it should be regulated.”* They also contrast privacy and security: *“Data privacy is focused on the use and governance of personal data—things like putting policies in place to ensure that consumers’ personal information is being collected, shared and used in appropriate ways.”*

Put another way, privacy is about protecting personal data about individuals from abuse.

#### Why Is Privacy Important?

While some have argued that privacy is no longer possible or relevant, many others disagree, and many laws have been put in place around the world to protect privacy. One accessible summary for the widespread position that privacy is important is Glenn Greenwald’s TED Talk [*“Why privacy matters”*](https://www.ted.com/talks/glenn_greenwald_why_privacy_matters) (2014). Here are some of his points (see the talk for details):

* People who say, *“If you’re doing something that you don’t want other people to know, maybe you shouldn’t be doing it in the first place”* are engaged in extreme self-deprecation; *“What they’re really saying is,"I have agreed to make myself such a harmless and unthreatening and uninteresting person that I actually don’t fear having the government know what it is that I’m doing.’”*

* Many of these same people [who make these claims] do not actually act in this way, e.g., they will take many steps to gain privacy for themselves.

* *“There’s a reason privacy is so craved universally and instinctively… when we’re in a state where we can be monitored, where we can be watched, our behavior changes dramatically… There are dozens of psychological studies that prove that when somebody knows that they might be watched, the behavior they engage in is vastly more conformist and compliant.”*

* *“Mass surveillance creates a prison in the mind that is a much more subtle though much more effective means of fostering compliance with social norms or with social orthodoxy, much more effective than brute force could ever be.”*

* *“A society in which people can be monitored at all times is a society that breeds conformity and obedience and submission, which is why every tyrant, the most overt to the most subtle, craves that system.”*

* *“When we allow a society to exist in which we’re subject to constant monitoring, we allow the essence of human freedom to be severely crippled.”*

* *“a system of mass surveillance suppresses our own freedom in all sorts of ways. It renders off-limits all kinds of behavioral choices without our even knowing that it’s happened.”*

### Privacy Requirements

#### Simplest Approach: Don’t Collect Personal Information

The first step for addressing privacy is acknowledging that privacy is important, and then considering how to ensure your software provides adequate privacy if it collects information about individuals.

The simplest approach to privacy, and often the best starting point, is to *not* collect information about individuals unless you specifically need it. If you do not collect the information, you cannot divulge it later and you do not have to determine how to prevent its misuse. Eliminating it entirely is best from a privacy point of view.

Failing that, minimize personal information to what you absolutely require. If you must collect information about individuals, you must then provide a variety of protections for them, at the very least those required by law and regulation. This can be complicated, because many laws and regulations may apply.

#### Privacy Laws and Regulations

Laws and regulations about privacy are widespread. Different terms are used for them, including information privacy, data privacy, and data protection. Whether or not these laws and regulations affect your software depends on what kind of data your software collects. In many cases, software does not need to do anything special for privacy. However, in other cases these laws and regulations can matter greatly.

[Article 17 of the International Covenant on Civil and Political Rights of the United Nations](https://www.ohchr.org/en/professionalinterest/pages/ccpr.aspx) in 1966 is widely ratified and protects privacy. It says, *“No one shall be subjected to arbitrary or unlawful interference with his privacy, family, home or correspondence, nor to unlawful attacks on his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks.”*

Different countries, and provinces/states within countries, have different laws regarding privacy. Here we will briefly discuss the US and European approaches.

#### United States

The United States (US) does not have a comprehensive information privacy law as a whole. Instead, the US federal government has a number of laws that cover specific circumstances. This includes the Family Educational Rights and Privacy Act of 1974 (FERPA) for student education records, the Health Insurance Portability and Accountability Act of 1996 (HIPAA) for health-related data, the Children’s Online Privacy Protection Act of 1998 (COPPA) for data related to children, and the Fair and Accurate Credit Transactions Act of 2003 (FACTA) for some financial data.

The [US Privacy Act of 1974 (5 U.S.C. 552a)](https://www.govinfo.gov/content/pkg/USCODE-2018-title5/pdf/USCODE-2018-title5-partI-chap5-subchapII-sec552a.pdf) mandates how US federal agencies must maintain records about individuals who are US citizens and lawful permanent resident aliens. For example, they must:

* collect only relevant and necessary information that is relevant and necessary to carry out an agency function;

* explain at the time the information is being collected, why it is needed and how it will be used;

* ensure that the records are used only for the reasons given, or seek the person’s permission when another purpose for the records’ use is considered necessary or desirable;

* provide adequate safeguards to protect the records from unauthorized access and disclosure; and

* allow people to see the records kept on them and provide them with the opportunity to correct inaccuracies in their records.

Some US states have additional laws. For example, the [California Online Privacy Protection Act (OPPA) of 2003](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22575) requires operators of commercial web sites or online services *“that collects personally identifiable information through the Internet about individual consumers residing in California who use or visit its [site or service must] conspicuously post its privacy policy…”* and comply with it. More recently, the [California Consumer Privacy Act of 2018 (CCPA)](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5), which became effective in 2020, gives California residents additional rights to know what personal information has been collected by businesses, and to opt out of the sale of that information.

Europe *does* have a comprehensive law, and even those outside Europe often must comply with it. So let’s focus on it; it applies to many situations, and understanding it will help you understand other privacy requirements.

#### European General Data Protection Regulation (GDPR)

The European General Data Protection Regulation (GDPR) protects the personal data of subjects who are in the European Union (EU). It applies whether or not the data processing occurs within the EU, and it applies whether or not the subjects are European citizens. As a result, the GDPR applies in many circumstances. [The Linux Foundation has a summary of the GDPR](https://www.linuxfoundation.org/wp-content/uploads/2018/05/lf_gdpr_052418.pdf) that highlights issues important to software developers. Below we point out some GDPR basics from the Linux Foundation’s GDPR summary.

But first: complying with the GDPR is important. Serious infringements can result in a fine of up to €20 million, or 4% of a firm’s worldwide annual revenue from the preceding financial year, whichever amount is *higher*.

The GDPR defines personal data (requiring protection as such) as *“any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person”*. Note that it is not just data that identifies an individual - it is data that is connected to data that identifies an individual. For example, a person’s mailing address is personal data; details about a person’s skills or preferences are also personal data if they are linked, or reasonably capable of being linked, to other information identifying that individual.

Under the GDPR some personal data are considered more sensitive, and there are greater restrictions on collecting and processing them. These include:

* racial or ethnic origin

* political opinions, religious or philosophical beliefs, or trade union membership

* genetic data

* biometric data for the purpose of uniquely identifying a natural person

* data concerning health

* data concerning a natural person’s sex life or sexual orientation

Personal data is *processed* any time an operation is performed on it. This includes collecting, storing, viewing, transmitting, and deleting it, whether or not by automated means. In the GDPR, a “controller” is the person or organization who determines the purpose and means of processing. A “processor” is a third party that processes the data on a controller’s behalf.

The GDPR defines seven primary principles for processing personal data. These principles inform the purposes of all of the specific provisions of the GDPR. Understanding them goes a long way towards having a good initial “gut reaction” for whether a particular use of personal data is likely to be acceptable. These are:

1. **Lawfulness, Fairness and Transparency**
Process personal data in a way that is legal, fair and transparent to the data subject.

2. **Purpose Limitation**
Only process personal data in ways that are compatible with the legitimate purposes for which it was collected.

3. **Data Minimization**
Limit the personal data you collect to what’s adequate for those purposes.

4. **Accuracy**
Keep personal data accurate and up to date, and take every reasonable step to erase or rectify inaccurate data.

5. **Storage Limitation**
Store personal data in a form which permits identification for no longer than needed for the purposes for which it was collected.

6. **Integrity and Confidentiality**
Process personal data in a way that ensures appropriate security.

7. **Accountability**
A controller of personal data is responsible for the above principles, and for demonstrating its compliance with them.

Six articles in the GDPR lay out specific rights given to individuals regarding their personal data. This gives EU residents the right to contact a data controller and request that it take certain actions (*GDPR requests*). Since EU residents have these rights, software systems and organizational processes must be designed to enable these rights. The types of requests described in the GDPR include the following:

* **Right of Access** (Art. 15)
Data subjects can ask whether their personal data is being processed. If it is, they can receive “access” to the data (e.g., a copy or screenshot of it) and information regarding the processing.

* **Right to Rectification** (Art. 16)
Data subjects can have inaccurate data updated and corrected.

* **Right to Erasure** (a.k.a “Right to be Forgotten”) (Art. 17)
In certain circumstances, data subjects can have their personal data erased.

* **Right to Restriction of Processing** (Art. 18)
In certain circumstances, data subjects can restrict processing of their personal data. It can still be stored, unless a “Right to Erasure” request was also made.

* **Right to Data Portability** (Art. 20)
In certain circumstances, data subjects can have their personal data exported (e.g., provided to the data subject or a third party in a structured, commonly used and machine-readable format).

* **Right to Object** (Art. 21)
In certain circumstances, particularly for direct marketing and profiling purposes, data subjects can object to having their personal data processed.

To process personal data, it must be lawful, meaning it must fall into at least one of several categories, including the following among others:

* **Compliance with Law**. Personal data can be processed if it is necessary for compliance with a legal obligation.

* **Performing a Contract with the Data Subject**. Personal data can be processed if it is necessary to perform a contract that is with that data subject. *Note that this likely does not apply to a contract with somebody other than the data subject, such as their employer.*

* **Legitimate Business Interests**. Personal data can be processed if doing so is consistent with “legitimate interests,” unless overridden by the data subject’s interests to the contrary. This can be a more ambiguous concept.

* **Consent**. Personal data can be processed if the data subject gives their consent.

Note that personal data can be processed if the data subject gives their consent. However, for consent to be valid under the GDPR:

* it must be *“specific”* and *“informed”* (e.g., it should include a specific description of what data is being collected, and how it will be used);

* it requires a *“clear affirmative action”* by the data subject (e.g., requiring the participant to check a checkbox, and not having it pre-checked); and

* it must be freely revocable (e.g., the data subject must be able to withdraw consent at any time).

Even if consent is granted, you may want to also find another lawful basis for processing the data, especially if you want to retain it. Under the GDPR, you are generally not allowed to retain personal data without a lawful basis.

Under the GDPR, *profiling* is any form of automated processing that involves using personal data to evaluate aspects of that person. Profiling will usually require getting explicit consent

from the individual, which means also that the individual will be able to withdraw that consent at any time. Therefore, profiling activities will typically require a greater degree of review and protections for the applicable personal data.

Here are some resources for learning more about the GDPR:

* The [official EU site for the GDPR text](http://data.europa.eu/eli/reg/2016/679/oj) 

* [*“The Guide to the General Data Protection Regulation (GDPR)”*](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/) 

* [*“Solutions for a responsible use of the blockchain in the context of personal data”*](https://www.cnil.fr/sites/default/files/atoms/files/blockchain_en.pdf) 

* [*“Security of Personal Data”*](https://www.cnil.fr/sites/default/files/atoms/files/cnil_guide_securite_personnelle_gb_web.pdf) 

* The Linux Foundation, [*“Summary of GDPR Concepts For Free and Open Source Software Projects”*](https://www.linuxfoundation.org/wp-content/uploads/2018/05/lf_gdpr_052418.pdf)

* [California Online Privacy Protection Act, Chapter 22. Internet Privacy Requirements [22575-22579]](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22575)

#### Telemetry

Software sometimes includes functionality to collect telemetry data, that is, data about how the software is used or performing. Telemetry data is often collected through a “phone home” mechanism built into the software itself, where the software sends this data elsewhere.

Telemetry data is especially fraught with privacy and confidentiality issues. End users are typically presented with an option to opt-in to share statistical data with the developers of the software, but that agreement may not be adequate. End users ideally should be given a full awareness of what data may be sent to the vendor or other third party when they use the software, and abilities to control that transfer of data.

The Linux Foundation’s [*“Telemetry Data Collection and Usage Policy”*](https://www.linuxfoundation.org/telemetry-data-policy/) presents a brief discussion of some of the issues that should be considered before implementing telemetry data collection, as well as discussing the Foundation’s approach to managing use of telemetry by its open source project communities. This may be useful to you in other contexts.