## Misconfiguration

Misconfiguration can happen at any level of an application stack, including the platform, web server, application server, database, framework, and custom code. Developers and system administrators need to work together to ensure that the entire stack is configured properly. Automated scanners are useful for detecting missing patches, misconfigurations, use of default accounts, unnecessary services.

The frequent misconfigurations:

- Debugging enabled

- Incorrect permissions

- Default credentials

- Default installation files

- Cloud misconfiguration

- Network and security devices misconfiguration

How the services can be used by a malicious/weaponized software?

### Debugging enabled

App server configuration allows stack traces to be returned to users, potentially exposing underlying flaws. Attackers seek the extra information error messages provide.

### Incorrect permissions

Developers/admins forget to properly set permissions on publicly exposed directories, admin consoles or dashboards. Therefore, attackers can access unauthorized files. This might be confused with the Broken Access Control vulnerability, but the root cause happens to be a misconfiguration issue, before even reaching any web application feature or other services which interact with the permissions.

### Default credentials

The app server admin console is automatically installed and default accounts are not changed. Attacker discovers the standard admin pages are on your server, logs in with default passwords, and takes over.

### Default installation files

The app server comes with sample applications that are not removed from your production server. The sample applications have well-known security flaws attackers can use to compromise your server.

### Cloud misconfiguration

Cloud misconfiguration can be defined as any errors, glitches or gaps in your cloud environment that can leave you exposed to risk. The main issues are:

- Insufficient access controls and permissive network access

- Insufficient access controls on resources:

- Access control misconfigurations can expose sensitive data or leave valuable files at risk of being stolen. Allowing attackers to read data from your databases or retrieve files from cloud storage puts your company at risk of corporate espionage, exposes users’ personal information, and enables malicious actors to delete critical data. If attackers gain access to your network or servers, they can potentially disrupt your services. This disruption can include ransomware attacks by encrypting files or servers, delete resources or even use servers to send spam or mine bitcoins illicitly.

- Network and security devices misconfiguration

- A single change to a network device can have far-reaching effects on businesses; creating security holes for cybercriminals to exploit, preventing you from passing crucial regulatory and compliance audits, and causing costly outages which can bring your business to a standstill.

- Exposing sensitive services and servers to the public

- Leftover networking rules cause unexpected behaviour
