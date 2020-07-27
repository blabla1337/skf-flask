##Description:

The principle of least privilege recommends that accounts have the least amount of
privilege required to perform their business processes. This encompasses user rights,
resource permissions such as CPU limits, memory, network, and file system permissions.

## Solution:

The principle means giving a user account only those privileges which are essential to
that user’s work. For example, a backup user does not need to install software: hence,
the backup user has rights only to run backup and backup-related applications.
Any other privileges, such as installing new software, are blocked.

The principle applies also to a personal computer user who usually does work in a normal
user account, and opens a privileged, password protected account (that is, a superuser)
only when the situation absolutely demands it.

This principle can also be applied to your web-applications. Instead of solely depending
on role based authentication methods using sessions, we rather want to assign privileges
to users by means of a Database-Based Authentication system.

We still use sessions in order to identify if the user was logged in correctly, only now
instead of assigning that user with a specific role we assign him with privileges to
verify which actions he is privileged to perform on the system.

Also, a big pro of this method is, whenever a user has to be assigned fewer privileges
your changes will be applied on the fly since the assigning does not depend on the session
which otherwise had to expire first.
