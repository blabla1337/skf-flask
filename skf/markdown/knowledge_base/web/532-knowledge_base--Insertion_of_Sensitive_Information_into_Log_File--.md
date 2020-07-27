##Description:

Information written to log files can be of a sensitive nature and give valuable guidance to an attacker or expose sensitive user information.

While logging all information may be helpful during development stages, it is important that logging levels be set appropriately before a product ships so that sensitive user data and system information are not accidentally exposed to potential attackers. Different log files may be produced and stored for: Server log files (e.g. server.log). This can give information on whatever application left the file. Usually this can give full path names and system information, and sometimes usernames and passwords. log files that are used for debugging

##Mitigation:


PHASE:Architecture and Design Implementation:
Consider seriously the sensitivity of the information written into log files. Do not write secrets into the log files.

PHASE:Distribution:
Remove debug log files before deploying the application into production.

PHASE:Operation:
Protect log files against unauthorized read/write.

PHASE:Implementation:
Adjust configurations appropriately when software is transitioned from a debug state to production.

