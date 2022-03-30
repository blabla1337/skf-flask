# Question

Which of the following are objectives of testing application platform configuration? Can choose multiple answers.

* ( ) Ensure that defaults and known files have been removed.
* ( ) Validate that no debugging code or extensions are left in the production environments.
* ( ) Review the logging mechanisms set in place for the application.
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) Ensure that defaults and known files have been removed.
* (x) Validate that no debugging code or extensions are left in the production environments.
* (x) Review the logging mechanisms set in place for the application.
* ( ) None of the above 

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Comment review should be done in order to determine if any information is being leaked through comments. This review can only be thoroughly done through an analysis of the web server static and dynamic content and through file searches."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"It is safe to store sensitive data in machine.config and root web.config."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False


Explanation: All users can read .NET Framework machine.config and root web.config files by default. Do not store sensitive information in these files if it should be for administrator eyes only.

-----SPLIT-----


# Question

Which of the following can be applied while configuring application platform? Can choose multiple answers.

* ( ) Make sure that the server software runs with *administrative* privileges in the operating system.
* ( ) Make sure the server software properly logs both legitimate access and errors.
* ( ) Encrypt sensitive information that should be read by the IIS worker processes only and not by other users on the machine.
* ( ) Do not grant Write access to the identity that the Web server uses to access the shared applicationHost.config. This identity should have only Read access.
* ( ) None of the above 

-----SPLIT-----

# Answer

* ( ) Make sure that the server software runs with *administrative* privileges in the operating system.
* (x) Make sure the server software properly logs both legitimate access and errors.
* (x) Encrypt sensitive information that should be read by the IIS worker processes only and not by other users on the machine.
* (x) Do not grant Write access to the identity that the Web server uses to access the shared applicationHost.config. This identity should have only Read access.
* ( ) None of the above 

Explanation: Make sure that the server software runs with least privileges in the operating system.


-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"it is better to keep logs in a separate location and not in the web server itself."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


Explanation: it is wiser to keep logs in a separate location and not in the web server itself. This also makes it easier to aggregate logs from different sources that refer to the same application (such as those of a web server farm) and it also makes it easier to do log analysis (which can be CPU intensive) without affecting the server itself.

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"As having logs help to analyze actions, it is better filling up the web server storage as much as possible with log files."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False


Explanation: Logs can introduce a Denial of Service condition if they are not properly stored. Any attacker with sufficient resources could be able to produce a sufficient number of requests that would fill up the allocated space to log files, if they are not specifically prevented from doing so. 

-----SPLIT-----


# Question

Which of the following conditions are seeked for log rotation? Can choose multiple answers.

* ( ) The logs will be rotated when reached a defined time interval.
* ( ) Rotate logs when they reach a given size.
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) The logs will be rotated when reached a defined time interval.
* (x) Rotate logs when they reach a given size.
* ( ) None of the above 


-----SPLIT-----

# Question

Which of the followings should be considered when log rotation is applied ? Can choose multiple answers.

* ( ) Logs are kept for the time defined in the security policy, not more and not less.
* ( ) Logs are compressed once rotated (this is a convenience, since it will mean that more logs will be stored for the same available disk space)
* ( ) File system permission of rotated log files are the same (or stricter) that those of the log files itself. 
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) Logs are kept for the time defined in the security policy, not more and not less.
* (x) Logs are compressed once rotated (this is a convenience, since it will mean that more logs will be stored for the same available disk space)
* (x) File system permission of rotated log files are the same (or stricter) that those of the log files itself. 
* ( ) None of the above 


-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"Log files can be accessed by all applications and users with least privileges."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: Log information should never be visible to end users. Even web administrators should not be able to see such logs since it breaks separation of duty controls. Ensure that any access control schema that is used to protect access to raw logs and any applications providing capabilities to view or search the logs is not linked with access control schemas for other application user roles. Neither should any log data be viewable by unauthenticated users.
