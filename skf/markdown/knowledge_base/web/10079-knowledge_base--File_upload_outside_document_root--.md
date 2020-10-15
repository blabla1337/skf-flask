##Description:

Files that are uploaded by users or other untrusted services should always be placed outside
of the document root. This is to prevent malicious files from being parsed by attackers such as PHP/HTML/Javascript files.

Should an attacker succeed to bypass file upload restrictions and upload a malicous file, it would
be impossible for the attacker to parse these files since they are not located inside of the
applications document root.

##Mitigation:

Files should be stored outside of the applications document root. Preferably files should be stored
on a seperate file server which serves back and forth to the application server. 

Files should always be stored outside of the scope of the attacker to prevent files from
being parsed or executed.

When storing files outside of the document root, take into consideration potential path traversal injections
in the applications file name such as "../html/backtoroot/file.php". Whenever this filename is being used directly
into the path that is used to store files, it could be used to manipulate the storage path.
