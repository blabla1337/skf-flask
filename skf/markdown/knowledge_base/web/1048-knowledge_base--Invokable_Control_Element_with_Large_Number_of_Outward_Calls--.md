##Description:

The code contains callable control elements that contain an excessively large number of references to other application objects external to the context of the callable, i.e. a Fan-Out value that is excessively large.

While the interpretation of excessively large Fan-Out value may vary for each product or developer, CISQ recommends a default of 5 referenced objects. This issue makes it more difficult to maintain the software, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

##Mitigation:
