
Sandboxing
-------

**Description:**

A sandbox is a security mechanism for separating running programs. 
It is often used to execute untested code, or untrusted programs from 
unverified third parties, suppliers, untrusted users and untrusted websites. It's creating 
an extra layer of security where an attacker first need to break out from.


**Solution:**

Use the sandbox attribute of an iframe for untrusted content. The sandbox attribute of an 
iframe enables restrictions on content within a iframe. The following restrictions are 

active when the sandbox attribute is set: 
- All markup is treated as being from a unique origin
- All forms and scripts are disabled. 
- All links are prevented from targeting other browsing contexts 
- All features that triggers automatically are blocked 
- All plugins are disabled 

It is possible to have a fine-grained control over iframe capabilities using the value of 
the sandbox attribute. In old versions of user agents where this feature is not supported, 
this attribute will be ignored. Use this feature as an additional layer of protection or 
check if the browser supports sandboxed frames and only show the untrusted 
content if supported. Apart from this attribute, to prevent Clickjacking attacks and 
unsolicited framing it is encouraged to use the header X-Frame-Options which supports 
the deny and same-origin values. Other solutions like framebusting: 
 
    if(window!== window.top) { window.top.location = location; } #Only for legacy browser support

	