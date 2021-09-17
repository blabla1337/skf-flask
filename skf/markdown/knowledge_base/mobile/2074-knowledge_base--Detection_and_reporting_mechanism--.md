## Description:

Detection mechanisms and Responses

MSTG-RESILIENCE-8: The detection mechanisms trigger responses of different types, including delayed and stealthy responses.

Attackers can force applications to work in a different way for data extraction. The client side is a un-trusted environment and the app should be ready for fake environments, application debugging or tempering attempts.


## Mitigation:

The app should detect unusual work patterns, debugging or tempering efforts in run-time and response with a different way, such as delaying or giving incorrect responses. 

And the app should also report all those abnormalities to back-end systems.