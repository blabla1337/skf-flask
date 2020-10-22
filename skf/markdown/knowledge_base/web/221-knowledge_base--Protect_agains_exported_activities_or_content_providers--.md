## Description:

Whenever input from exported activities intents or content provided is not properly validated
this input could potentially exploit vulnerabilities on the mobile application depending on
the context in where the input is being used.

## Solution:

Input from exported activities, intents or content providers should be validated against 
the applications intended operation, i.e if the application expects a field with an integer value,
all other incoming data that work out of this intended operation should be logged and rejected
by the application.
