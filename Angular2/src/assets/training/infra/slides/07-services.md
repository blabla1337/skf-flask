### File Transfer Protocol (FTP)

FTP is a communication protocol used for transferring files between computer systems.  
|Exploit|Description|
|--|---|
|Anonymous access|A misconfigured FTP service can allow an anonymous user access to sensitive information. Anonymous access can be checked by running the following FTP command and providing **_anonymous:password_** credentials when requested: <pre>ftp &lt;SERVER_[HOSTNAME\|IPADDRESS]&gt;</pre> The same can be achieved using the Metasploit FTP Anonymous Auxiliary Module[^metasploit_ftp]|
|Brute force attacks | FTP services are not protected against brute-force attacks by default. This verification can be done using the Metasploit FTP Login Auxiliary Module[^metasploit_ftp]|
|MitM Sniffing/Spoofing| FTP protocol is unencrypted, turning it vulnerable to Man-in-the-Middle (MitM) attacks.|
|Service specific vulnerabilities| Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|


### Telnet

Telnet is an application protocol built for providing a command-line interpreter normally used for remote server management.

|Exploit|Description|
|---|---|
|User enumeration|Telnet servers responds differently whether the username is valid or invalid. The telnet command **_vrfy &lt;USERNAME&gt;_** will return 550 error if the username is incorrect. User enumeration can be also done using Metasploit Telnet Login auxiliary module[^metasploit_telnet].|
|Brute force attacks|Authentication brute force attacks can be done using Metasploit Telnet Login auxiliary module[^metasploit_telnet].|
|MitM Sniffing/Spoofing| Telnet protocol is unencrypted, turning it vulnerable to Man-in-the-Middle (MitM) attacks.|
|Service specific vulnerabilities| Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|


### Secure Shell (SSH)

SSH is a network protocol built for providing a command-line interpreter normally used for secure remote server management and secure file transfer.

|Exploit|Description|
|---|---|
|Brute force attacks| Authentication brute force attacks can be done using Metasploit SSH Login auxiliary module[metasploit_ssh].|
|User enumeration|The response to specially crafted packets sent to vulnerable servers may indicate if the username is valid. The verification can be done using the Metasploit SSH Enumusers auxiliary module[metasploit_ssh_enumusers].|
|Service specific vulnerabilities| Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE websites for public exploits.|


### Simple Mail Transfer Protocol (SMTP)

SMTP is a communication protocol used for email transmission.
|Exploit|Description|
|---|---|
|Open relay| It is a SMTP server misconfiguration that allows anyone on the internet or in the same network to send any email through it. The sender and receiver can be forged using open relay servers. Open relay can be verified with Metasploit SMTP Relay auxiliary module [metasploit_smtp_relay].|
|User enumeration| The verification can be done using the Metasploit SSH Enumusers auxiliary module[metasploit_smtp].|
|MitM Sniffing/Spoofing| Telnet protocol is unencrypted, turning it vulnerable to Man-in-the-Middle (MitM) attacks.|
|Service specific vulnerabilities| Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|


### Domain Name System (DNS)

DNS is a naming system used to identities computers reachable through the internet or LANs.
|Exploit|Description|
|---|---|
|Record enumeration| DNS record enumeration can be achieved by different means: Zone Transfer, Brute forcing, reverse lookups, and others. Different tools can be used for record enumeration: Fierce DNS[fierce_dns], Metasploit DNS Enum auxiliary module [metasploit_dns_enum], GoBuster[gobuster], Amass[amass], etc.|
|Service specific vulnerabilities| Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|


### Hypertext Transfer Protocol (HTTP)

HTTP is an application-layer protocol for transmitting hypermedia documents, such as HTML.

|Exploit|Description|
|---|---|
|Application related attacks| HTTP is the industry standard used for Web-Applications and APIs communication and thus, most of targeted attacks will use the HTTP protocol. HTTP Interception proxy tools such as Portswigger Burpsuite[burpsuite] and OWASP ZAP[owasp_zap] are used for testing Web Applications and APIs.|
|MitM Sniffing/Spoofing| HTTP protocol is unencrypted, turning it vulnerable to Man-in-the-Middle (MitM) attacks.|
|Web server specific vulnerabilities|Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|


### Server Message Block (SMB)

SMB is a network sharing protocol developed by Microsoft, used for sharing to access files, printers, serial ports, and other resources between different systems.

|Exploit|Description |
|---| --- |
|Shares enumeration|Shares available in a server may be listed with or without authentication. The command <pre>smbclient –L <SERVER_HOSTNAME\|IPADDRESS></pre> can be used to identify interesting open network shares. The same can be achieved with Metasploit SMB Enum Shares auxiliary module[^metasploit_smb].|
|Unauthenticated access|Misconfigured SMB shares may allow unauthenticated access to sensitive data. Shares can be accessed by using <pre>smbclient '\\\\<SERVER_HOSTNAME\|IP>\<SHARE>'</pre>|
|Users enumeration|Valid users can be enumerated with Metasploit SMB Enum Users auxiliary module[^metasploit_smb]|
|Login Brute force|Login brute force can be done via Metasploit SMB Login auxiliary module[^metasploit_smb]|  
|Protocol specific vulnerabilities|Based on the Service Fingerprinting results, it is possible to determine the software and version running the service. The information can be looked up at ExploitDB and CVE databases for public exploits.|
