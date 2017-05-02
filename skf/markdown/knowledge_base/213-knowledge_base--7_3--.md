#Description

The mobile application should not store sensitive data into unencrypted manner, even in
the applications key chains since these can be easily accessed once a phone is jailbroken 
or exploited the keychain can be easily read. 

#Solution

Determine the context of where the sensitive information is being stored, is it a small 
data set or is the data stored in an SQLite database. For every context determine the 
applications platform recommended native options settings and follow these 
recommendations accordingly. 

 
