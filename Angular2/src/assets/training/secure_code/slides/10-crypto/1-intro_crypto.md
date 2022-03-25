# 3. Cryptography

This chapter describes the basics of how to use cryptography to help develop secure software, including the basics of symmetric/shared key encryption algorithms, cryptographic hashes, public-key (asymmetric) encryption, how to securely store passwords, cryptographically secure pseudo-random number generators (CSPRNG), and Transport Layer Security (TLS).

Learning objectives:

1. Understand what cryptography is.

2. Discuss the basics of symmetric/shared key encryption algorithms.

3. Discuss the basics of cryptographic hashes.

4. Discuss the basics of public-key (asymmetric) encryption.

5. Explain how to *securely* store passwords.

6. Discuss the basics of cryptographic pseudo-random number generators (PRNG).

7. Understand the basics of using Transport Layer Security (TLS).

8. Understand the basics of other key cryptographic topics.

## Cryptography

### Introduction to Cryptography

The word *cryptography* comes from the Greek phrase for “secret writing”. Cryptography is the science or art of transforming intelligible form, and its reverse. However, many people attack cryptographic systems; cryptanalysis is the science or art of undoing a cryptographic transformation without the exact knowledge of how it was done.

Cryptography provides a set of tools that can sometimes help develop secure software. Cryptography *cannot* solve all security problems. In fact, most computer security vulnerabilities have nothing to do with cryptography.

![image alt text](../../security_xkcd.png)

**Security**, retrieved from [xkcd](https://xkcd.com/538/), provided indeed [CC-BY-NC-2.5](https://creativecommons.org/licenses/by-nc/2.5/) 

That said, in *some* systems cryptography is a vitally important part of making a system secure. Cryptography is often used to protect sensitive data’s confidentiality, and it can do that in two ways: *at rest* (storing the information in an encrypted form) and *in transit* (transmitting the information in an encrypted form). Cryptography can also, with certain limits, verify that information is from someone with a corresponding key, and/or verify that certain data has not been changed.

For example, we typically want our web browsers and web servers to have an encrypted connection between each other so that the information is confidential from others, cannot be modified without detection, and so that at least the web browser can have high confidence that it is communicating with the correct web server. Many systems manage sensitive data such as financial data, healthcare data, and personally-identifiable information (PII). Cryptography is often a part of protecting this data so it cannot be easily read by others.

However, there are many people who know how to attack cryptographic systems. Using cryptography incorrectly can sometimes lead to having false confidence in an insecure system. What’s worse, incorrectly-used cryptography can sometimes be hard to spot if you are not an expert, so these mistakes may be exploited for long periods of time.

🔔 Sensitive data exposure is such a common mistake in web applications that it is 2017 OWASP Top 10 #3. Sensitive data exposure is not always caused by poor use of cryptography, but it is a common underlying cause. Inadequate encryption strength is such a common cause of security vulnerabilities by itself that it is 2019 CWE Top 25 #3 (it is [CWE-326](https://cwe.mitre.org/data/definitions/326.html)).

For normal software development there are three key rules for cryptography:

1. **_Never_ develop your own cryptographic algorithm or protocol**.
Creating these is highly specialized. To do a good job you need a PhD in cryptography, which in turn requires advanced college mathematics. Instead, find out what has been publicly vetted by reputable cryptographers and use that.

2. **_Never_ implement your cryptographic algorithms or protocols (if you have an alternative)**.
There are a large number of specialized rules for implementing cryptographic algorithms that don’t apply to normal software and are thus not known to most software developers. Tiny implementation errors of cryptographic algorithms often become massive vulnerabilities. Instead, reuse good implementations where practical.

3. **Cryptographic systems (such as algorithms and protocols) are occasionally broken.**
Make sure the ones you choose are still strong enough, and make sure you are  prepared to replace them.

When choosing a cryptographic library, prefer ones that have had significant public review and have a simple-to-use-correctly API. Otherwise, you risk having a vulnerability either in the reused component or having one caused due to incorrect use of an API.

Cryptanalysts are always looking for ways to break cryptographic algorithms, and cryptographers are always working to counter those attacks. Historically, cryptographic algorithms are developed, last for a while, and then finally are broken due to some attack. So before choosing anything in cryptography, do some searches to make sure that what you are choosing is not weak or broken. Perhaps nothing has been broken recently… but it would be unwise to assume that.

The following sections will identify some key algorithms and protocols, and some pointers about them.

### Symmetric/Shared Key Encryption Algorithms

A *symmetric key* or *shared key* encryption algorithm takes data (called “cleartext”) and a key as input, and produces encrypted data (called “ciphertext”). It can also go the other way: using the ciphertext and the same key, it can produce the corresponding cleartext.

What is important about symmetric key encryption algorithms is that the *same* key is used to both encrypt and decrypt the data. So if you want people to be able to decrypt some ciphertext encrypted this way, you have to arrange for them to get the key. Most modern symmetric key algorithms are extremely fast (they are often hardware-accelerated), and they form the basis of many cryptographic systems.

#### Choosing a Symmetric Key Algorithm

At the time of this writing (2020), the most common symmetric key algorithm is the Advanced Encryption Standard (AES). AES supports 3 key sizes: 128, 192, or 256 bits; the longer key sizes are stronger against attack, but take longer to execute. At the time of this writing, even 128 bits is considered adequately secure for most purposes, but check to see if something has changed. AES is extremely fast; it was designed to be fast on modern processors, and many processors have mechanisms that speed it up even further.

There are other historical symmetric key algorithms that are considered *insecure* for typical use cases today:

* DES: Its 56-bit key length is far too short to be secure today.

* RC4: Many vulnerabilities have been found in RC4, and it is generally considered insecure.

* 3DES: Internally, this has a block size of only 64 bits. Algorithms with such small block sizes are vulnerable to an attack called a *birthday attack* if they are used to encrypt significant amounts of data with the same key.

* Blowfish: This also has a block size of only 64 bits, and thus has the same problems as 3DES.

There are alternative symmetric key algorithms that are also generally considered secure. For example, TwoFish was a finalist in the contest that led to AES, and at the time of this writing has no known practical vulnerabilities.

#### Choosing a Mode

Many symmetric key algorithms, including AES, are what is called *block algorithms*. With block algorithms you must also choose a *mode* to use. Here is the most important rule about modes:

**Never use Electronic Code Book (ECB) mode!**

The ECB mode is basically a debug or test mode for testing cryptographic algorithms. In ECB mode, the same block of data will produce the same encryption result. This is disastrous for an encryption algorithm, because it reveals far too much about the data that is supposed to be encrypted. A great illustration of this is the so-called “ECB Penguin” image; this image is encrypted using an ECB mode. Encrypted images should appear as random noise, but because ECB mode is used, in the ECB Penguin the image of Tux the Penguin is clearly visible.

![The ECB Penguin: A dark encrypted image that clearly shows the Linux mascot, Tux the Penguin](../../ecb_penguin.png)

The ECB Penguin, by Filippo Valsorda, retrieved from [filippo.io](https://blog.filippo.io/the-ecb-penguin/). Licensed under [CC BY-SA 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode). This image was inspired by the original lower-resolution ECB Penguin image by Wikipedia User: Lunkwill. Source “The ECB Penguin” (2013-11-10). Based on the Tux the penguin official Linux mascot created by Larry Ewing in 1996

Historically the *Cipher block chaining* (CBC) mode was used, but this must be calculated sequentially, so it is slow on multi-core systems. Another problem is that many systems that use CBC are vulnerable to attacks unless they are integrity-checked first. So in general, it is best to avoid CBC mode today ([Microsoft CBC Documentation](https://docs.microsoft.com/en-us/dotnet/standard/security/vulnerabilities-cbc-mode), 2020).

A common mode used today is the Galois/Counter Mode (GCM). It is fast, parallelizable, and adds an authentication code so it can easily detect if the wrong key is used. It is a good mode to use. There are other good modes as well; the important thing is to choose a mode wisely, and in particular, to *never* use ECB mode in production systems.