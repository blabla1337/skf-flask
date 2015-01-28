
Double decoding of headers/parameters
-------


**Description:**

Double decoding is a problem which often occurs when multiple servers are used in which a configuration error is made?. 
A hacker can thus bypass the escaping to implement injections into the application.


**Solution:**

Only one webserver should decode/encode the data.	