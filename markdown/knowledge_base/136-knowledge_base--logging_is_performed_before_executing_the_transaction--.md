
Logging is performed before executing the transaction
-------

**Description:**

Whenever the logging is performed before executing a transaction you can be ensured that 
the transactions are logged. This increases the integrity of your log files.


**Solution:**

Verify that logging is performed before executing the transaction. If logging was 
unsuccessful (e.g. disk full, insufficient permissions) the application fails safe. 
This is for when integrity and non-repudiation is a must.
