# Authentication integrity checks 
-------

## Description:

Whenever security logs can be modified by unauthorized users, potential attackers could use these
privileges to erase and cover their attacks against the application or simply soil the log files.

## Solution:

Use host intrusion detection systems (file-integrity monitoring or change-detection software) on logs
to ensure that existing log data or other important files cannot be changed without generating alerts, 
depending on the context like a log file then new data being added should not cause an alert.
