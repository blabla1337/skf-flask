
Data from untrusted sources
-------

**Description:**

Whenever data from untrusted servers is executed by your application there is a high 
probability this data could be contaminated with malicious code. such as for example 
XSS from JSON files, or XXE when parsing XML files. 


**Solution:**

Verify the application code does not execute uploaded data obtained from untrusted sources. 
You could consider sandboxing this data when showing the content on your application.

	