Description:
In information technology, a backup, or data backup, or the process of backing up, 
refers to the copying into an archive file of computer data that is already in 
secondary storage so that it may be used to restore the original after a data loss event. 

Solution:
Backups have two distinct purposes. The primary purpose is to recover data after its loss, 
be it by data deletion or corruption. Data loss can be a common experience of computer users. 

The secondary purpose of backups is to recover data from an earlier time, according to a 
user-defined data retention policy, typically configured within a backup application for how 
long copies of data are required. 

Though backups represent a simple form of disaster recovery 
and should be part of any disaster recovery plan, backups by themselves should not be considered
a complete disaster recovery plan. One reason for this is that not all backup systems are able to
reconstitute a computer system or other complex configuration such as a computer cluster, 
active directory server, or database server by simply restoring data from a backup.

In order to always poses over the latest state of your data it is recommended to do active syncing
between the application server and the back-up service. Also, try to not only write recovery policies 
but also put them to the test regularly to verify the plans effective coverage in case if an incident.
