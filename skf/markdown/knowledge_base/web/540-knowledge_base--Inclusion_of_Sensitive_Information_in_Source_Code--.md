##Description:

Source code on a web server or repository often contains sensitive information and should generally not be accessible to users.

There are situations where it is critical to remove source code from an area or server. For example, obtaining Perl source code on a system allows an attacker to understand the logic of the script and extract extremely useful information such as code bugs or logins and passwords.

##Mitigation:


PHASE:Architecture and Design System Configuration:
Recommendations include removing this script from the web server and moving it to a location not accessible from the Internet.

