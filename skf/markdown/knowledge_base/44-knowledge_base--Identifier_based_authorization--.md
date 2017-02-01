Identifier-based authorization
-------

**Description:**

An application uses parameters in order to process data.
These parameters can also be used to assign certain roles and retrieve

Content corresponding with those parameters. Imagine the following example:

    www.target.com/index.php?loggedin=user

In this situation the application will get content and subscribe user roles corresponding to the user parameter

    www.target.com/index.php?loggedin=admin

In this situation the application will get content and subscribe user roles corresponding to the admin parameter.


**Solution:**

Whenever you are checking whether a user is restricted to review certain data, the access
restrictions should be processed server-side.

The userID should be stored inside of a session variable on login and should be used to
retrieve user data from the database like : SELECT data from personaldata where userID=:id <- session var

Now an possible attacker can not tamper and change the application operation since the
identifier for retrieving the data is handled server-side.
