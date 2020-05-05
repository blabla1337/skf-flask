## Description:

Configiring the web server to only serve files with an expected
file extension helps prevent information leakage whenever developers
forget to remove backup files or zipped versions of the web application
from the webserver.


## Solution:

Verify that the web tier is configured to serve only files with specific
file extensions to prevent unintentional information and source
code leakage. For example, backup files (e.g. .bak), temporary working
files (e.g. .swp), compressed files (.zip, .tar.gz, etc) and other extensions
commonly used by editors should be blocked unless required.
