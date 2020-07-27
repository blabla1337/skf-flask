##Description:

Information exposure through query strings in URL is when sensitive data is passed to parameters in the URL. This allows attackers to obtain sensitive data such as usernames, passwords, tokens (authX), database details, and any other potentially sensitive data. Simply using HTTPS does not resolve this vulnerability.

Regardless of using encryption, the following URL will expose information in the locations detailed below: https://vulnerablehost.com/authuser?user=bob&authz_token=1234&expire=1500000000

The parameter values for 'user', 'authz_token', and 'expire' will be exposed in the following locations 
when using HTTP or HTTPS:

- Referer Header
- Web Logs
- Shared Systems
- Browser History
- Browser Cache
- Shoulder Surfing

When not using an encrypted channel, all of the above and the following:
- Man-in-the-Middle


## Solution:

Sensitive informtion should never be included in the URL.
