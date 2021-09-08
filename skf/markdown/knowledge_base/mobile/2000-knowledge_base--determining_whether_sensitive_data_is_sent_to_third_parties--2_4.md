## Description:

Determining Whether Sensitive Data is Sent to Third Parties

MSTG-STORAGE-4: No sensitive data is shared with third parties unless it is a necessary part of the architecture.

Various third-party services can be embedded in the app. The features these services provide can involve tracking services to monitor the user's behavior while using the app, selling banner advertisements, or improving the user experience.

The downside to third-party services is that developers don't know the details of the code executed via third-party libraries. Consequently, no more information than is necessary should be sent to a service, and no sensitive information should be disclosed.


## Mitigation:

Only necessary data should be shared with relevant third parties. 