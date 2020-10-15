##Description:

Whenever sensitive data is accessed by a user this event should be logged to later verify
the integrity of the access to the data. The same principle applies to whenever the data is collected
and under which protection directives the data is accessed to.

Example:
Imagine an insurance company and an accident has happened that is being showed on the news. 
Workers of that insurance company must not be able to randomly fill in license plates 
they see on the news to find PI about the people having the accident if it is not related
to their jobs. I.E, an insurance holder calls the company to file in an accident report. 

##Mitigation:

Verify accessing sensitive data is logged, if the data is collected 
under relevant data protection directives or where logging of accesses is required.
