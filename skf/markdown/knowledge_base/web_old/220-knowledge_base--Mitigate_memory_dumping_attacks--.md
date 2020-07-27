##Description:

Whenever sensitive information in stored in the devices’ memory, this information can 
be dumped by various tool such as “android debugger (ADB)“ on android devices. This 
information could give critical information about the application and could aid attackers 
in their attacks.

## Solution:

Sensitive information maintained in memory must be overwritten with zeros as soon as it 
no longer actively used, to mitigate memory dumping attacks.

Note: 
Whenever the programming language has a garbage collector make sure whenever values are zeroed the GC is also
emptied.
