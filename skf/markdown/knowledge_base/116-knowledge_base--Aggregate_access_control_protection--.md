
Aggregate access control protection
-------

**Description:**

 Verify the system can protect against aggregation or continuous access of 
 secured functions, resources, or data. For example, possibly by the use of a 
 resource governor to limit the number of edits per hour or to prevent the entire database 
 from being scraped by an individual user.


**Solution:**

The system should contain a counter which can keep up with the number of times a certain 
users addresses database tables and should be rejected when he passes a reasonable number. 
This violation should also be reported since it could indicate an attacker scraping your 
table contents and stealing company information.
	