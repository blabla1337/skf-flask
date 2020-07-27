##Description:

Whenever the document root contains extraneous files, these files could be accessed by an
attacker or could possibly contain functionality which could contain other vulnerabilities.

## Solution:

Extraneous files in document root should be investigated and deleted if it's not necessary
for the operation of the application.

There are more chances of accessing hidden folders, files and some configuration files to be
accessed through document root.

For example if you are using some version control system like git or svn. You may have .git,
.svn folders and .gitignore files. If you are using IDE project files, you may have .idea hidden folder. Even there are chances of configuration files with common extensions, like config.json, config.yml, config.xml, package.json, .htaccess, README.md files to be present in the document root.
Even there are chances of having swap files, backup files to be there in the document root.

The solution for this problem is to prevent directory listing , remove the hidden folders, files and configuration files. We can even prevent the users from accessing this files with properly 
configuring the configuration files of the server like .htaccess files.