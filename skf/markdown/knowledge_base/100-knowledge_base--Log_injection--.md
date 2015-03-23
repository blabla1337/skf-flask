
Log injection
-------

**Description:**

Log injection problems are a subset of injection problem, in which invalid entries taken 
from user input are inserted in logs or audit trails, allowing an attacker to mislead 
administrators or cover traces of attack. Log injection can also sometimes be used to 
attack log monitoring systems indirectly by injecting data that monitoring systems will 
misinterpret. 


**Solution:**

You should consider these three controls when implementing logging systems. 

- Design: If at all possible, avoid logging data that came from external inputs.

- Implementation: Ensure that all log entries are statically created, or if they must 
  record external data that the input is vigorously white-list checked. 

- Run time: Avoid viewing logs with tools that may interpret control characters in the file, 
  such as command-line shells.

	