##Description:

It's always possible that an attacker can find a security flaw and abuse this to gain access
to the server. From here the attacker tries to further infiltrate into the network and other
important components of the application for example the database. This database should be firewalled
correctly so it's not accessible from the internet. Also this database has it own server and is in a
different segment of the network. Always apply INGRESS and EGRESS filtering for all the servers used.

##Mitigation:

Verify that components are segregated from each other via a defined security control, such as
network segmentation, firewall rules, or cloud based security groups.
