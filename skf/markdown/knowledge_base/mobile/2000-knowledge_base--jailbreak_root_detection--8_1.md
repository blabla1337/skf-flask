## Description:

Jailbreak/Root Detection

MSTG-RESILIENCE-1: The app detects, and responds to, the presence of a rooted or jailbroken device either by alerting the user or terminating the app.

In the context of anti-reversing, the goal of root/jailbreak detection is to make running the app on a rooted/jailbreak device a bit more difficult, which in turn blocks some of the tools and techniques reverse engineers like to use. Like most other defenses, root/jailbreak detection is not very effective by itself, but implementing multiple root/jailbreak checks that are scattered throughout the app can improve the effectiveness of the overall anti-tampering scheme.


## Mitigation:

A [list of typical jailbreak detection techniques for iOS was published by Trustwave](https://www.trustwave.com/Resources/SpiderLabs-Blog/Jailbreak-Detection-Methods/ "Jailbreak Detection Methods on the Trustware Spiderlabs Blog").

Some of root detection techniques for Android implemented in the [crackme examples](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes "OWASP Mobile Crackmes") that accompany the OWASP Mobile Testing Guide.