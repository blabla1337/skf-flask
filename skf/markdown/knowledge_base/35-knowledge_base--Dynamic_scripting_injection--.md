## Description:

When user input is used to evaluate scripting code, high-security risks could be introduced. If the input is not properly escaped an attacker can inject his own script code and gain access to the server.

## Solution:

Do not use direct user-input in the dynamic scripting function. You should first
use an input validation or encoding function on the user submitted data to clean and
sanitize the input against malicious intent.
