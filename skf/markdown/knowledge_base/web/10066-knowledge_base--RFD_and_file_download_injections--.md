##Description:

Reflective file download occurs whenever an attacker can "forge" a download through misconfiguration in your "disposition" and "content type" headers. Instead of having the attacker to upload an evil file to the web server he can now force the browser to download a malicious file by abusing these headers and setting the file extension to any type he wants.

Now, whenever there is also user-input being reflected back into that download it can be used to forge evil attacks. The attacker can present an evil file to ignorant victim's who are trusting the domain of which the download was presented from.

File download injection is a similar type of attack except this attack is made possible whenever there is user-input that is reflected into the "filename=" parameter in the "disposition" header. The attacker again can force the browser to download a file with his own choice of extension and set the content of this file by injecting this directly into the response like filename=evil.bat%0A%0D%0A%0DinsertEvilStringHere

Whenever the user now opens the downloaded file the attacker can gain full control over the target’s device.


##Mitigation:

First, never use user input directly into your headers since an attacker can now take control over it.

Secondly, you should check if a filename really does exist before presenting it towards the users. You could also create a whitelist of all files which are allowed to be downloaded and terminate requests whenever they do not match.

Also, you should disable the use of "path parameters". It increases the attacker’s attack vector and these parameters also cause a lot of other vulnerabilities.
And last you should sanitize and encode all your user-input as much as possible. Reflective file downloads depend on user-input being reflected in the response header. Whenever this input has been sanitized and encoded it should not do any harm to any system it is being executed on

