# 3. Calling Other Programs

This chapter describes how to call other programs securely, including how to counter injection attacks (including SQL injection and OS command injection) and how to properly handle filenames/pathnames.

Learning objectives:

1. Discuss the basics of securely calling other programs.

2. Understand how to counter injection attacks (including SQL injection and OS command injection).

3. Discuss proper handling of filenames/pathnames.

## Introduction to Securely Calling Programs

### Introduction to Securely Calling Programs

Very few programs are entirely self-contained; nearly all programs call out to other programs. This includes local programs, such as programs provided by the operating system, built-in software libraries for that language, and software from package repositories (like npm, PyPI, and maven). Modern systems often call out through a network to other services, making requests through various APIs (such as REST and GraphQL APIs) and receiving data in formats such as JSON and XML. Almost all of these programs then call other programs. Often, these indirect calls are not obvious (e.g., calling a library written by someone else) or involve a great deal of “hidden” infrastructure.

You need to be careful about what programs you choose to use (trust) and manage them (e.g., how you record and update them). Once you choose them, you must be careful about how you use these other programs. In this section, we are going to talk about securely *using* other programs.

First, the obvious: if a program is known to be insecure, and security matters, then don’t use it! But usually, you are not using a known-insecure program, so let’s move beyond that.

If there is a relatively easy way to limit privileges of the routine you are calling, do so. If you can *limit* the privileges given, then, if an attacker breaks through, the damage is more limited and it may make it harder for the attacker to cause more damage. This is another example of the security principle of least privilege. For example, if you are calling a database, try to limit database privileges of the program making the request. If you are using SQL, consider using the **GRANT** command so the requesting program has fewer privileges.

A useful principle is to only call a routine with valid values. If a routine requires that a number be 0 through 9, then it should not be possible for an attacker to cause 50 to be sent. This is easier in theory than in practice, especially since those limits are not always well-documented. But where you know of a limitation, consider doing some checks to make sure they are honored, or write your program so that the limitations are necessarily honored.

A very important principle is that if a routine is hard to use securely, and there is another way to do the task that is easier to do securely, *use the routine that is easier to use securely*. Here are some warning signs that you are using a routine that is hard to use securely:

* It executes whatever program is sent to it, and some data you send might come from an attacker. Any routine with a name like **eval()**, **exec()**, **execute()**, or **system()** has a high chance of being in this category. For example, don’t use **eval()** in JavaScript to process JSON data (in general!); use something safer like JavaScript’s function **JSON.parse()**.

* It requires you to concatenate constant strings with data that might come from an attacker. Generally, that other data from an attack has to be escaped, and it is easy to make a mistake when escaping data.

* Its input format is described using a language specification (such as Backus-Naur Form).

* It was intended for direct human interaction, not for a program to invoke it.

You *can* use such routines securely, and sometimes you need to. But if you can avoid it, your program will probably be more secure - and it will probably be easier to maintain, too. If you cannot avoid them, you may want to wrap their use in special wrappers to make them easier to use safely.

Why are certain kinds of routines hard to use securely? One common problem is that many routines accept languages with *metacharacters* - that is, characters that change how other characters are interpreted instead of being data themselves. For example, the double quote character (**“**) is often a metacharacter (including in SQL and shell). If there is a language specification, that almost certainly means there are metacharacters. Supporting metacharacters is very flexible, and if all of the input is trusted, it is not a problem. But when parts of the data might be from an attacker, you need to be very careful and take extra precautions. If an attacker can insert metacharacters into the input, and they are not escaped exactly correctly, then dangerous and easily-exploited vulnerabilities often follow if they are read by some kind of interpreter. These kinds of attacks are sometimes called injection attacks.

Vulnerabilities to injection attacks are such common mistakes in web applications that “Injection” is 2017 OWASP Top 10 #1 and 2019 CWE Top 25 #18. It is identified as [CWE-94](https://cwe.mitre.org/data/definitions/94.html),  *Improper Control of Generation of Code (‘Code Injection’)*.

So you need to ensure that when you send data to some program (or output), you send it in a secure way. That may involve:

* **Sanitizing**
Removing any illegal or potentially-malicious character (usually metacharacters) from the data.

* **Escaping**
Modifying characters (some metacharacters) so that they are not interpreted incorrectly.

* **Normalizing**
Changing the form of data to be a common form (and, as a side-effect, preventing it from causing a security problem).

Where possible, use libraries and APIs that do this for you; they are easier to use securely.

Let’s now examine some common injection attack cases and how to handle them securely. Again, an injection vulnerability is when a program accepts data from an attacker and improperly hands that data to some command interpreter. Some of the most common problems occur when that data is sent to a database system (SQL injection attacks) or an operating system command interpreter (OS command injection attacks), so we will focus on those. Once you understand how to deal with these two common cases, it will be much clearer how to properly handle other interpreters we will not cover here (e.g., the Lightweight Directory Access Protocol (LDAP)). We will begin by discussing sending data to database systems, which are often vulnerable to SQL injection attacks.