## Description:

We want to test our applications and infrastructure for out of date and
insecure components and services that are running periodically. 

We can configure our CI environment in such a way that we have
jobs running that do automated continuous (hourly, daily, weekly, monthly)
security scanning on our infrastructure and applications. 

## Solution:

Integrate security tooling into your CI/CD pipelines that do
continuous security scanning against your applications and infrastructure
such as but not limited to the following tools,

* Nessus
* OpenVas
* Nmap
* Nikto
* OWASP Zap (passive scans)

These tools should than run periodically to scan your system for known
vulnerabilities and report high/critical findings to your engineers so
they can take appropriate actions.
