## Description:

Sensitive Information in Auto-Generated Screenshots

MSTG-STORAGE-9: The app removes sensitive data from views when moved to the background.

Manufacturers want to provide device users with an aesthetically pleasing experience at application startup and exit, so they introduced the screenshot-saving feature for use when the application is backgrounded. This feature may pose a security risk. Sensitive data may be exposed if the user deliberately screenshots the application while sensitive data is displayed. A malicious application that is running on the device and able to continuously capture the screen may also expose data. Screenshots are written to local storage, from which they may be recovered by a rogue application or someone who has stolen the device.

For example, capturing a screenshot of a banking application may reveal information about the user's account, credit, transactions, and so on.


## Mitigation:

Application should remove all sensitive data from its screens/views when the it is not actively in use.