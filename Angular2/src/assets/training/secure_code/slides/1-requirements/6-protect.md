### Protect, Detect, Respond

Software is developed to be used, so let’s briefly look at security from the viewpoint of operations.

Organizations should not assume that they can always protect their systems from attack. Attackers sometimes break through. For example, the [US NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) identifies five concurrent and continuous functions organizations should apply in their operations to manage cybersecurity risk:

1. **Identify**
*“Develop an organizational understanding to manage cybersecurity risk to systems, people, assets, data, and capabilities”.*

2. **Protect**
*“Develop and implement appropriate safeguards to **ensure** delivery of critical services”.*

3. **Detect**
*“Develop and implement appropriate activities to identify the occurrence of a cybersecurity event”.*

4. **Respond**
“Develop and implement appropriate activities to take action regarding a detected cybersecurity incident”.

5. **Recover**
*“Develop and implement appropriate activities to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cybersecurity incident”.*

This list of five functions is sometimes simplified to three basic functions: **protect**, **detect**, and **respond**. When using this simplified list of three basic functions, identify is considered part of protect, and recover is considered part of respond. We will use that shortened list of basic functions here.

None of these three basic functions (protect, detect, and respond) is effective by itself. If you only protect, but don’t detect or recover, then an attacker who breaks through your defenses can do whatever they want. If you only detect or recover, without protecting your system, you will never get any work done; you will instead spend all your time on detection or recovery, and soon no one will trust your system. In addition, recovery is useless without detection, because you often won’t know *when* to recover.

We will talk a lot about protection measures. It is typically cheaper to prevent problems than deal with them later (old proverbs apply here, e.g., *“an ounce of prevention is worth a pound of cure”*). But we will also discuss measures to detect and respond, because they are also necessary. At the very least, larger applications should include mechanisms like logging (to support detection) and backup (to support recovery), because they are necessary in applications we deploy.