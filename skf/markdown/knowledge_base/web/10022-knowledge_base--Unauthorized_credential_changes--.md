##Description:

An application which offers user login functionality, usually has an administration page
where user-data can be modified. When the user wants to change this data he should
specify his current password.

##Mitigation:

When changing user credentials or email address the user must always enter a valid
password in order to implement the changes. This is also called re-authentication or
step-up / adaptive authentication. Whenever a user "re-authenticates" himself the current
session ID value should also be refreshed in order to fend oFf so called "session hijackers"
