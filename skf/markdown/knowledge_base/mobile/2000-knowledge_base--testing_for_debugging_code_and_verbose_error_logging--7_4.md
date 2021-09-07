## Description:

Testing for Debugging Code and Verbose Error Logging

MSTG-CODE-4: Debugging code and developer assistance code (e.g. test code, backdoors, hidden settings) have been removed. The app does not log verbose errors or debugging messages.

To speed up verification and get a better understanding of errors, developers often include debugging code about responses from their APIs and about their application's progress and/or state. Furthermore, there may be debugging code for "management-functionality", which is used by developers to set the application's state or mock responses from an API. Reverse engineers can easily use this information to track what's happening with the application. 


## Mitigation:

Verbose logging features and debugging code should be removed from the application's release version.