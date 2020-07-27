##Description:

Using build platforms on premise or as a service is one of the core components in a SDLC.
These build and deploy servers are sometimes not perfect for performing secure builds or deploys.
This is because the lack of hardening of the OS for security improvements where the application
could also benefit from this hardening. Also the access of third party services can lead to
compromise of the secrets or integrity of the code of the application.

## Solution:

Building your application should always be done on a server that you trust, you are in control and
has the latest security patches and hardening configured. For deploying the application the same
rules apply, also think about what type of third party services can access the code or modify it.
Creating scripts to monitor for bad behavior of a third party service can be an option as an extra
quality control check.
