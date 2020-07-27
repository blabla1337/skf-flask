##Description:

The product makes files or directories accessible to unauthorized actors, even though they should not be.

Web servers, FTP servers, and similar servers may store a set of files underneath a root directory that is accessible to the server's users. Applications may store sensitive files underneath this root without also using access control to limit which users may request those files, if any. Alternately, an application might package multiple files or directories into an archive file (e.g., ZIP or tar), but the application might not exclude sensitive files that are underneath those directories.

##Mitigation:
