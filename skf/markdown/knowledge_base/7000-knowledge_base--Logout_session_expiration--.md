## Description:

Once the user hits the logout button or is logged out by inacitivity, it's expected the application terminates user's session properly. However, there are situations in which the application simply redirects the user to the logon page. Also, the modern applications relies on client side storage, as cache files, browser session storage, cookies as IndexedDB which may contain session related and sensitive information. Yet, complex applications relying on single-sign-on(SSO) mechanisms may leave the source application sesssion as open. In the described scenarios, one attacker accessing a shared computer or using an unattended computer can resume the session and operate the application on the user's behalf. 

## Solution:

Verify that absolute and timeout logout invalidates or erases any client- or server-side session storage, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties.
