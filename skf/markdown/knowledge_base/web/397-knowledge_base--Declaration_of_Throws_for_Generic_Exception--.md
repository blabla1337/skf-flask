## Description:

Throwing overly broad exceptions promotes complex error handling code that is more likely to contain security vulnerabilities.

Declaring a method to throw Exception or Throwable makes it difficult for callers to perform proper error handling and error recovery. Java's exception mechanism, for example, is set up to make it easy for callers to anticipate what can go wrong and write code to handle each specific exceptional circumstance. Declaring that a method throws a generic form of exception defeats this system.

## Mitigation:
