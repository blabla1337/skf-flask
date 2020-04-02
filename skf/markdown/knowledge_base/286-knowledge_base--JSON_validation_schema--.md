Description:

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.

When adding schema's to your or JSON files you have better control over what
type of user-input can be supplied in your application. 
This dramatically decreases an attacker’s vector when implemented the right way. 
Nonetheless, you should always apply your own input validation and rejection
as an extra layer of defense. This approach is also desirable since you also 
want to do countering and logging on the user’s requests and input.

Solution:

Verify that JSON schema validation takes place to ensure a properly formed
JSON request, followed by validation of each input field before any 
processing of that data takes place.
