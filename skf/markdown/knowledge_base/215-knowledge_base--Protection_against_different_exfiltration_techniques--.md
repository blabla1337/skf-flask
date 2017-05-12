# Protection against different exfiltration techniques
-------

## Description:

The mobile application should not leak sensitive information. This information could be leaked for example whenever:

- Screenshots are saved of the current application as the primary  application is backgrounded 
- Sensitive information is written to the console of the mobile device
- The Activitymanager should show the application name and a blank page and not show information

## Solution:

- Disallow screenshots of the application whenever the application is backgrounded
- Do not write sensitive information to the applications console, this information is accessible by attackers.
- Create a custom window for whenever the application is shown in the ActivityManager, so it does not give away sensitive
  information.
