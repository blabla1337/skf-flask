## Description:

Logs for Sensitive Data

MSTG-STORAGE-3: No sensitive data is written to application logs.

There are many legitimate reasons for creating log files on a mobile device, including keeping track of crashes or errors that are stored locally while the device is offline (so that they can be sent to the app's developer once online), and storing usage statistics. However, logging sensitive data, such as credit card numbers and session information, may expose the data to attackers or malicious applications.


## Mitigation:

The following checks should be performed:
	- Analyze source code for logging related code.
	- Check application data directory for log files.
	- Gather system messages and logs and analyze for any sensitive data.

As a general recommendation to avoid potential sensitive application data leakage, logging statements should be removed from production releases unless deemed necessary to the application or explicitly identified as safe, e.g. as a result of a security audit.