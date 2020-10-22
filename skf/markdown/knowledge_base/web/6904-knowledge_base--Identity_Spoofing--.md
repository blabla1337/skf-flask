##Description:

It is important to uniquely identify the users of an application for traceability. Therefore it should not be possible to use shared accounts,
nor should it be possible to re-bind identities to a different identity (spoofing)

##Mitigation:

Verify identities cannot be re-bound to a different identity and shared accounts are not present ("root", "admin", or "sa").
Administrative accounts like root, admin, sa,... should not be shared, should be renamed and should not be exposed to the front end of the application.
