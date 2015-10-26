
Reflective file download and File download injections
-------

**Description:**

Reflective file download occurs whenever an attacker can "forge" a download through
misconfigurations in your "disposition" and "content type" headers. Instead of having
the attacker to upload a evil file to the webserver he can now force the browser to 
download a malicious file by abusing these headers and setting the file extension to any 
type he wants.

Now, whenever there is also userinput being reflected back into that download it can be 
used to forge evil attacks. the attacker can present an evil file to ignorant vicim's who 
are trusting the domain of which the download was presented from. 

File download injection is a similar type of attack except this attack is made possible
whenever there is userinput that is reflected into the "filename=" paramater in the 
"disposition" header. The attacker again can force the browser to download a file with his
own choice of extension and set the content of this file by injecting this directly
into the response like: filename=evil.bat%0A%0D%0A%0DinsertEvilStringHere

Whenever the user now opens the downloaded file the attacker can gain full control over
the targets device.

**Solution:**

First of al never use userinput directly into your headers since an attacker can now
take control over it. 

Secondly you should check if a filename really does exist before 
presenting it towards the users. You could also create a whitelist of al files which
are allowed to be downloaded and terminate requests whenever they do not match.

Also you should disable the use of "path parameters". It increases the attackers attack 
vector and these parameters also cause a lot of other vulnerabilities.

And last you should sanitise and encode al your userinput as much as possible.
reflective file downloads depends on user-input being reflected in the response header.
Whenever this input has been sanitised and encoded it should not do any harm to any 
system it is being executed on.

 



   
