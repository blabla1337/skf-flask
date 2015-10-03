
SQL injection 
-------

**Description:**

SQL stands for simple query language and is designed in order for the application to 
communicate with a database in which it can write and get content from. However, 
when a attacker can inject malicious code into these queries he gains the ability to 
manipulate them and now he can withdraw, update and delete data which is stored on the 
target database.


**Solution:**

The use of prepared statements (aka parameterised queries) is how all developers should 
first be taught how to write database queries. They are simple to write, and easier to 
understand than dynamic queries. parameterised queries force the developer to first define 
all the SQL code, and then pass in each parameter to the query later. This coding style 
allows the database to distinguish between code and data, regardless of what user input 
is supplied.


	