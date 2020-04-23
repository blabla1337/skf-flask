## Description:

The web application uses the HTTP GET method to process a request and includes sensitive information in the query string of that requests.

The query string can be saved in the browser's history, passed through Referers to other web sites, stored in web logs, or otherwise recorded in other sources. If the query string contains sensitive information such as session identifiers, then attackers can use this information to launch further attacks.

## Mitigation:


PHASE:Implementation:
When sensitive information is sent, use the POST method (e.g. registration form).

