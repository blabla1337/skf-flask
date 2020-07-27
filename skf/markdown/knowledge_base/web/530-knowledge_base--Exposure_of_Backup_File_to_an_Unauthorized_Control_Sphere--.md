##Description:

A backup file is stored in a directory or archive that is made accessible to unauthorized actors.

Often, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.

##Mitigation:


PHASE:Policy:
Recommendations include implementing a security policy within your organization that prohibits backing up web application source code in the webroot.

