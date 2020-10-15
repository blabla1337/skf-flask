##Description:

Subdomain takeover is a process of registering a non-existing domain name to gain control over another domain. 

The most common scenario of this process follows:

Domain name (e.g., sub.example.com) uses a CNAME record to another domain (e.g., sub.example.com CNAME anotherdomain.com).
At some point in time, anotherdomain.com expires and is available for registration by anyone.
Since the CNAME record is not deleted from example.com DNS zone, anyone who registers anotherdomain.com has full control over sub.example.com until the DNS record is present.

The implications of the subdomain takeover can be pretty significant. Using a subdomain takeover, attackers can send phishing emails from the legitimate domain, perform cross-site scripting (XSS), or damage the reputation of the brand which is associated with the domain. 

Source: https://0xpatrik.com/subdomain-takeover-basics/

##Mitigation:

As an end user of a service, going through your organization's DNS records in a routine manner or while discontinuing or terminating a service will safely remove it's DNS records.

As a service provider, implementing stricter methods will prove (sub) domain ownership.
