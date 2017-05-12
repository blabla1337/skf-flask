# Intrusion detecting and reporting
-------

## Description:

All possible attacks on your application should be detected an reported in order to
prevent further escalation.

## Solution:

Intrusion detecting could be done by means of a:

"Positive security model:"
In this model you create certain regular expressions in order to only make the application
pass the so called "known good".
Whenever an application detects strange behavior and anomalies,
these issues should be reported. Keep in mind whenever the application changes this
whitelist method has to evolve alongside with it. A big con is it could generate a lot
of reports and alerts.

"Negative security model:"
Create a blacklist with known attacks and malicious input and make the application report
on detection of this input. You could also prioritise different malicious input and
classify them into different groups.

Whatever method you may choose to prefer, you should always ensure error handling logic in
security controls denies access by default. With this approach applied you will have a
higher probability that whenever an attacker manages to break your applications intended
operation, it will not fail in a way which increases his attack vector.
