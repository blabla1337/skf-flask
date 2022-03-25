### Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)

Many algorithms depend on secret values that cannot be practically guessed by an attacker. This includes values used by cryptography algorithms (such as nonces), session ids, and many other values. If an attacker can guess a value, including past or future values, many systems become insecure.

One challenge is historical: today, the name *random* in programming language libraries usually implies that the function is *not* cryptographically secure. One of the first uses for digital computers was to implement simulations (especially *Monte Carlo simulations*) where random numbers were repeatedly acquired for a simulation. It was often important to be able to *reconstruct* these random numbers so experiments could be repeated. Internally, such random functions would be implemented using algorithms such as a linear congruential generator (LCG), and would often be “seeded” (initialized) by values such as a date/time that can be trivially guessed by an attacker. Because this was one of the first uses of computers, there is a convention across almost all programming languages that the word “random” refers to a way to create a sequence of numbers that could be easily reconstructed later if needed. In other words, the word “random” in programming languages typically implies “*predictably random*”, and that is not what you want in cryptography. Such random numbers *must not* be used for security mechanisms where it is important that an attacker *not* be able to determine the number.

Instead, for cryptography and security-related tasks you need to use a [cryptographically secure pseudo-random number generator (CSPRNG)](https://en.wikipedia.org/wiki/Cryptographically-secure_pseudorandom_number_generator) for crypto and security-related tasks. Put another way, there are many pseudo-random number generator (PRNG) algorithms and implementations, but for security, you should *only* use PRNGs that are cryptographically secure PRNGs (CSPRNGs). A good CSPRNG prevents practically predicting the next output given past outputs (at greater than random chance) and it also prevents revealing past outputs if its internal state is compromised. CSPRNGs are also called cryptographic PRNGs (CPRNGs). Typically a CSPRNG implementation's name will have “secure” and/or “crypto” in it. In their documentation, you may see references to well-accepted CSPRNG algorithms such as Yarrow, Fortuna, ANSI X9.17 (which can use any block cipher), NIST SP 800-90A’s Hash_DRBG, HMAC_DRBG, and CTR_DRBG. 

** Never use the algorithm Dual_EC_DRBG, as it is widely accepted that this is a subverted and insecure algorithm.**

Here are some examples of how to call the predictable PRNG versus a cryptographically secure PRNG in different programming languages (in practice there are often multiple ways; the point is to show that they are different):

<table>
  <tr>
    <td>Language</td>
    <td>Predictable random value
(do not use for security)</td>
    <td>Cryptographically secure random value</td>
  </tr>
  <tr>
    <td>Java</td>
    <td>Random()</td>
    <td>SecureRandom()</td>
  </tr>
  <tr>
    <td>C#</td>
    <td>System.Random</td>
    <td>System.Security.Cryptography. RandomNumberGenerator</td>
  </tr>
  <tr>
    <td>JavaScript</td>
    <td>Math.random</td>
    <td>window.crypto.getRandomValues
or crypto.randomBytes</td>
  </tr>
  <tr>
    <td>Python</td>
    <td>random</td>
    <td>os.random</td>
  </tr>
</table>


Another challenge is that software is fundamentally deterministic; given exactly the same inputs, a sequential algorithm should produce exactly the same output. You should not normally be directly seeding (initializing) any cryptographically secure algorithms, as many of these libraries implement secure seeding themselves. If you must seed it (and that is a bad sign), ensure that attackers cannot guess the seed value. Some people seed cryptographically secure PRNGs algorithms with date/time data, which is a vulnerability; in many cases, attackers can easily guess the likely date/times.

There is a simple solution: use a CSPRNG and use hardware to correctly provide data to it. Most operating system kernels today provide cryptographically secure random numbers by gathering environmental noise from hardware devices. If you are directly running on Linux, reading from **/dev/urandom** will provide cryptographically random data (in special circumstances, you might want to use **/dev/random** instead, but that can block). These cryptographically secure random numbers can be used directly, or can be used as a secure seed for a cryptographically secure PRNG.

A particularly nasty security problem in computer systems is *insecure random number generators*. An insecure random number generator produces values that look fine, but destroys the security of the entire system. Many failures of cryptographic systems have been traced back to bad random number generation, in part because it can be hard to detect the problem.

In many cases using insecure random number generators is an unintentional mistake, but in some cases organizations *intentionally* subvert random number generators. For example, in 2020 it was revealed that the US CIA, in cooperation with West Germany intelligence, owned the company Crypto AG and had widely sold cryptographic products that had been intentionally subverted, in at least some cases by tampering with how it generated “random” values. See [The intelligence coup of the century](https://www.washingtonpost.com/graphics/2020/world/national-security/cia-crypto-encryption-machines-espionage/) by Greg Miller for more information.

Insecure random number generation is an especially serious problem in Internet of Things (IoT) device software. One 2021 report found that about 35 billion IoT devices had disastrous security vulnerabilities due to insecure cryptographic random number generation. This is in part because many IoT software developers directly call hardware random number generators (they shouldn’t do that), but even worse, they ignored error return codes from those generators (and they definitely shouldn’t do that). Hardware random number generators typically have easily-exceeded generation rates, so they can generate random numbers at limited speeds only. If users read too fast, the generator will likely report errors. Just paying attention to the error code from the hardware isn’t really enough, though.  Hardware sometimes fails, and if the software just hangs in that case, the IoT device may be too unreliable to compete. Sample code for accessing the random number generator hardware is often insecure (it shows how to get data, but not how to use it correctly). Correctly using the hardware directly can be quite difficult, for example, the LPC 54628’s user manual page number 1,106 (of 1,152) notes, in a convoluted way, that after reading a random number from its hardware you must read and throw away the next 32 values. The same research also shows that hardware random number generators from popular processors used in IoT products do not generate fully random data. One can use a randomness test to verify if the generated numbers are actually random.

Software developers for IoT devices should not access the hardware registers directly, but should instead call well-crafted CSPRNG generators that correctly use hardware sources (preferably multiple sources) as inputs into their internal entropy pool. In most cases IoT developers should use an IoT operating system that includes a CSPRG implementation that is correctly seeded from multiple hardware sources, and simply check to see if it appears to be carefully written for security. Where that’s not practical, use a well-crafted and analyzed CSPRNG library that includes correct software to extract random values from your hardware; do not implement your own crypto unless you’re an expert in cryptography. IoT software developers should also run statistical tests on their random number generation mechanism to ensure that they’re random, because this is an especially common problem in IoT devices. For more details, see [You're Doing IoT RNG](https://labs.bishopfox.com/tech-blog/youre-doing-iot-rng) ([presentation](https://www.youtube.com/watch?v=Zuqw0-jZh9Y)) by Dan Petro and Allan Cecil, a 2021 DEF CON presentation.

In short: Make sure you use a strong, properly-implemented cryptographically secure pseudo-random random number (CSPRNG) generator, seeded with multiple hardware values, every time you need a value that an adversary cannot predict.
