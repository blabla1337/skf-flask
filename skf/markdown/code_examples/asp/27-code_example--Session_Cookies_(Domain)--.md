Session cookies (domain)
-------

## Example:


	/*
	Setting the "Domain" attribute to a too permissive value, such as "example.com" 
	allows an attacker to launch attacks on the session IDs between different hosts and 
	web applications belonging to the same domain, known as cross-subdomain cookies.
	For example, vulnerabilities in www.example.com might allow an attacker to get access 
	to the session IDs from secure.example.com.
	*/
	
	<system.web>
		<httpCookies domain="demo.mySite.com" />
	</system.web>
	
