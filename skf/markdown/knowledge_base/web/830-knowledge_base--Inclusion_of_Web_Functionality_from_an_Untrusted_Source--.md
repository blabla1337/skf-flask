##Description:

The software includes web functionality (such as a web widget) from another domain, which causes it to operate within the domain of the software, potentially granting total access and control of the software to the untrusted source.

Including third party functionality in a web-based environment is risky, especially if the source of the functionality is untrusted. Even if the third party is a trusted source, the software may still be exposed to attacks and malicious behavior if that trusted source is compromised, or if the code is modified in transmission from the third party to the software. This weakness is common in mashup development on the web, which may include source functionality from other domains. For example, Javascript-based web widgets may be inserted by using '<SCRIPT SRC=http://other.domain.here>' tags, which causes the code to run in the domain of the software, not the remote site from which the widget was loaded. As a result, the included code has access to the local DOM, including cookies and other data that the developer might not want the remote site to be able to access. Such dependencies may be desirable, or even required, but sometimes programmers are not aware that a dependency exists.

##Mitigation:
