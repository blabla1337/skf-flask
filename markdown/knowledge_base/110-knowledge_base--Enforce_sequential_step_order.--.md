
Enforce sequential step order.
-------

**Description:**

Whenever an functionality consists out of following several steps to achieve some goal i.e, 
"User adds items to chart", "User enters shipping information", "User pays for goods",  
"Items will be shipped." 
You want to make sure the user can not skip the payment step in order to receive his goods. 


**Solution:**

In order to verify that this stage was run through by a sincere user you want to enforce 
the application to only process business logic flows in sequential step order, with all 
steps being processed in realistic human time, and not process out of order, skipped steps, 
process steps from another user, or too quickly submitted transactions.
	