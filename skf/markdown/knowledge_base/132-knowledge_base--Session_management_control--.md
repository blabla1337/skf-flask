
Session management control
-------

**Description:**

The ability to restrict and maintain user actions within unique sessions is critical to 
web security. Most users of this guide will be using an application framework with built 
in session management capabilities. Others will use languages such as Perl CGI that do not. 
Those without a built in session management system and those who override the existing 
session management systems are at an immediate disadvantage. Implementations built from 
scratch are often weak and breakable. Developers are strongly discouraged from 
implementing their own Session Management.


**Solution:**

Always use the frameworks default session management control implementation 
in your application.

	