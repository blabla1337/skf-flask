## Description:

Multiple mechanisms in each defense category

MSTG-RESILIENCE-7: The app implements multiple mechanisms in each defense category (8.1 to 8.6). Note that resiliency scales with the amount, diversity of the originality of the mechanisms used.

Security is a layered approach and only creating one simple layer is in most cases not good enough and can easily be bypassed. When we are thinking of the detection and resiliency controls we need to take into account that an attacker can invest time and effort to bypass that security layer. The more layers of protection the harder and more intense effort is needed by an attacker to overcome these.


## Mitigation:

We should have multiple implementations of the layers of controls mentioned (8.1 - 8.6) so we are not only relying on 1 technique for example to detect if the application is running in an emulator. The more different techniques for the mechanisms the harder and time-consuming it will be for an attacker to bypass this. 