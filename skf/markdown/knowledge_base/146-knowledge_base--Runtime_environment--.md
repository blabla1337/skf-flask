
Runtime environment
-------

**Description:**

Whenever you use runtime environments you want to make sure these are not susceptible for 
buffer overflows since this could lead to compromise of your application. 


**Solution:**

There are a number of runtime solutions that can detect stack corruption and buffer 
overruns or guard against attacks. These solutions typically terminate the program 
when an anomaly is detected, preventing the execution of arbitrary code.

	