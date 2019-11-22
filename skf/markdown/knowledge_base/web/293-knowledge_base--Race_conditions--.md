## Description:
A race condition is a flaw that produces an unexpected result when the timing of actions impact other actions. 
An example may be seen on a multithreaded application where actions are being performed on the same data. 
Race conditions, by their very nature, are difficult to test for.

Race conditions may occur when a process is critically or unexpectedly dependent on the sequence or timings of 
other events. In a web application environment, where multiple requests can be processed at a given time, 
developers may leave concurrency to be handled by the framework, server, or programming language.

## Solution:

One common solution to prevent race conditions is known as locking. This ensures that at any given time, 
at most one thread can modify the database. Many databases provide functionality to lock a given row when a 
thread is accessing it.

