
X-Path injections
-------

**Description:**

Web applications heavily use databases to store and access the data they need for their
operations. Historically, relational databases have been by far the most common 
technology for data storage, but, in the last years, we are witnessing an increasing 
popularity for databases that organise data using the XML language. 
Just like relational databases are accessed via SQL language, XML databases use X-Path as 
their standard query language.



**Solution:**

Just like the techniques to avoid SQL injection, you need to use a parameterised X-Path 
interface if one is available, or escape the user input to make it safe to include in a 
dynamically constructed query. If you are using quotes to terminate untrusted input in a 
dynamically constructed X-Path query, then you need to escape that quote in the untrusted 
input to ensure the untrusted data can not try to break
out of that quoted context.
	