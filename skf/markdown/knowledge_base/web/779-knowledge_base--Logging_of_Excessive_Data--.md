##Description:

The software logs too much information, making log files hard to process and possibly hindering recovery efforts or forensic analysis after an attack.

While logging is a good practice in general, and very high levels of logging are appropriate for debugging stages of development, too much logging in a production environment might hinder a system administrator's ability to detect anomalous conditions. This can provide cover for an attacker while attempting to penetrate a system, clutter the audit trail for forensic analysis, or make it more difficult to debug problems in a production environment.

##Mitigation:


PHASE:Architecture and Design:
Suppress large numbers of duplicate log messages and replace them with periodic summaries. For example, syslog may include an entry that states last message repeated X times when recording repeated events.

PHASE:Architecture and Design:
Support a maximum size for the log file that can be controlled by the administrator. If the maximum size is reached, the admin should be notified. Also, consider reducing functionality of the software. This may result in a denial-of-service to legitimate software users, but it will prevent the software from adversely impacting the entire system.

PHASE:Implementation:
Adjust configurations appropriately when software is transitioned from a debug state to production.

