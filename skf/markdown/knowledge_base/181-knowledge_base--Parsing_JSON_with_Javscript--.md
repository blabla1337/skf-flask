JSON parsing
-------

**Description:**

The eval() function evaluates or executes an argument.

If the argument is an expression, eval() evaluates the expression. If the argument is one
or more JavaScript statements, eval() executes the statements.

This is exactly the reason why eval() should **NEVER** be used to parse JSON or other
formats of data which could possible contain malicious code.


**Solution:**

For the purpose of parsing JSON we would recommend the use of the json.parse functionality.
Even though this function is more trusted you should always build your own security checks
and encoding routines around the json.parse before mutating the data or passing it on to
a view to be displayed in your HTML.
