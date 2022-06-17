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
