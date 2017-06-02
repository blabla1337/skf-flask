# SQL injection
-------

## Description:

All SQL queries, HQL, OSQL, NOSQL and stored procedures, related to stored procedures should be
protected by the use of query parameterization.
If not an attacker can inject malicious code into these queries and gain the ability to
manipulate them and can withdraw, update and delete data which is stored on the
target database.

## Solution:

The use of prepared statements and parameterized queries is how all developers should
first be taught how to write database queries. They are simple to write, and easier to
understand than dynamic queries. Parameterized queries force the developer to first define
all the SQL code, and then pass in each parameter to the query later. This coding style
allows the database to distinguish between code and data, regardless of what user input
is supplied.
