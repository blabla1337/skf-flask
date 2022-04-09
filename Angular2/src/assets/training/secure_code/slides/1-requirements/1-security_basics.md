# 1. Security Basics

This chapter provides a high-level overview about security, including definitions of security and privacy, requirements, and risk management.

Learning Objectives:

1. Explain what security means and understand common types of security requirements.

2. Discuss what privacy is, its importance, and privacy requirements.

3. Discuss risk management.

4. Discuss defense-in-breadth and how to apply security concepts in different software development processes.

5. Understand the importance of *Protection, Detection, and Response*.

6. Explain the basics of handling vulnerabilities.

## What Do We Need?

### What Does “Security” Mean?

To get secure software, we first need to understand what *security* means. Different software has different specific security requirements, but many people divide security requirements into three broad objectives - Confidentiality, Integrity, and Availability:

* **Confidentiality**
“No unauthorized read” - users are only allowed to read the information they are authorized to read.

* **Integrity**
“No unauthorized modification (write or delete)”  - users are only allowed to modify the information they are authorized to modify; modification includes additions, changes, and deletions.

* **Availability**
“Keeps working in presence of attack.” - the software keeps working while under attack. A Denial of Service (DoS) attack is an attack that tries to make the software no longer available.

This set of Confidentiality, Integrity, and Availability (CIA) is sometimes called the CIA triad.

![CIA Triad](../../cia.png)

The CIA Triad

Many add one more security objective: **non-repudiation** or **accountability**. The point of non-repudiation or accountability is that if someone takes certain actions, the system should be able to later prove it, even if the person involved later denies it. Examples of such actions are transferring a large sum of money, deleting something important, sending an important message, or receiving an important message. Some systems do not have such requirements, and even when they do, some people consider this a special case of integrity. Some people add other objectives, too. No matter how you categorize things, though, it is important to know clearly what the system is supposed to do. Having some simple categories can help you do that.

These security objectives need some supporting mechanisms. For example, confidentiality and integrity require that there be a way to determine if an action is authorized (unless all requests are authorized). Here are some common supporting mechanisms:

* **Identity & Authentication (I&A)**
Require users to identify themselves and prove (authenticate) their identity before doing anything that requires authorization. For example, they might use a username or email address as their identity, and use a password or hardware token to authenticate that they really are that user. This is typically done by a login process.

* **Authorization**
Determine what that user is allowed (authorized) to do before deciding to do it. You can think of authorization as a list of what each user is allowed to do. If it is easy for an attacker to add authorizations, then secure I&A means little. This is critical for implementing confidentiality and/or integrity. Watch out: the words *authentication* and *authorization* sound similar, but they are not the same thing. You may know exactly who someone is (authentication), but still not allow that person to do something (authorization).

* **Auditing** (aka logging)
Record important events to help detect and recover from attacks. Typically these events include log in, log out, and modifying important information. Auditing is often critical for implementing non-repudiation / accountability requirements.

What you specifically do depends on the software you are developing. If you are developing a lower-level library, you might not be directly supporting any of these supporting mechanisms, but you still have to make sure that what you are doing will fit into a larger program.

