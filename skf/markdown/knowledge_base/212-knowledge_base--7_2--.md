#Description

The mobile application should not store sensitive data into unencrypted shared
resources on the device. These resources can be accessible by other applications or 
physically accessible whenever a device gets lost or stolen. 

#Solution

Sensitive information should always be stored encrypted and preferably on the server side
and retrieved using an object reference with proper authorization mechanisms in place. 

Do not implement an existing cryptographic algorithm on your own, no matter how easy 
it appears. Instead, use widely accepted algorithms and widely accepted implementations.

The cardinal rule of mobile apps is to not store data unless absolutely necessary. 
As a developer you have to assume that the data is forfeited as soon as it touches the phone. 
You also have to consider the implications of losing mobile users' data to a silent 
jailbreak or root exploit.
