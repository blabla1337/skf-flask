## Description:

The application is deployed to unauthorized actors with debugging code still enabled or active, which can create unintended entry points or expose sensitive information.

A common development practice is to add back door code specifically designed for debugging or testing purposes that is not intended to be shipped or deployed with the application. These back door entry points create security risks because they are not considered during design or testing and fall outside of the expected operating conditions of the application.

## Mitigation:


PHASE:Build and Compilation Distribution:
Remove debug code before deploying the application.

