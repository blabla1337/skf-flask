## Description:

Client-side storage (also known as offline storage or web storage) is a functionality provided by browsers to allow applications to save information on the user's computer and retrieve them when necessary. 
Since this operations are performed by client-side scripting languages (notably Javascript), this information can be retrieved by third-party codes included in the webpages or by Cross-site scripting attacks (XSS) performed by attackers.
Moreover, attackers with local privileges on the user's machine are able to access these storages and possibly compromise their sessions.

## Solution:

Sensitive data (like session tokens or Personal Identifiable Information) should never be stored in client-side storages. 
This means to carefully verify that the application never saves at any time this kind of information in:
* Local Storage
* Session Storage
* Web SQL
* Cache Storage
* Application Cache
* IndexDB
