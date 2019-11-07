## Description:

Hardening of session cookies is possbile by using the '__Host" prefix. With this we can prevent the mis configuration of example the Path=/, Secure cookie and Domain attributes. 


## Solution:

The '__Host" prefix signals to the browser that both the Path=/ and Secure attributes are required, 
and at the same time, that the Domain attribute may not be present.