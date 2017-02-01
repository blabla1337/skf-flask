Parsing data exchange formats
-------

**Description:**

Whenever you are parsing data exchange formats such as, XML, JSON, CSV, etc, you
have to make sure that whenever these data files contain malicious code this will not be
executed by your application. You should also not solely depend on your parser to do all
the encoding and escaping for you since there could always be an edge case that does
execute certain attacks.


**Solution:**

We highly recommend to do your own escaping, sanitising, encoding on all data before
entering your application. The risk also depend on the context of wherever you are putting
this data into. So before you are doing any mutations with your data after getting it from
the resources, make sure you have applied the right mitigations.

Also another reason to build an extra layer of escaping, sanitising, encoding routines
in your application is because of the logging you want to apply on the data.

Recommended knowledge base items:

- Input rejection
- Input validation
- Audit logs
