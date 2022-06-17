# C3: Secure Database Access

## Description
This section describes secure access to all data stores, including both relational databases and NoSQL databases. Some areas to consider:

1. Secure queries
2. Secure configuration
3. Secure authentication
4. Secure communication

### Secure Queries
SQL Injection occurs when untrusted user input is dynamically added to a SQL query in an insecure manner, often via basic string concatenation. SQL Injection is one of the most dangerous application security risks. SQL Injection is easy to exploit and could lead to the entire database being stolen, wiped, or modified. The application can even be used to run dangerous commands against the operating system hosting your database, thereby giving an attacker a foothold on your network.

In order to mitigate SQL injection, untrusted input should be prevented from being interpreted as part of a SQL command. The best way to do this is with the programming technique known as 'Query Parameterization'. This defense should be applied to SQL, OQL, as well as stored procedure construction.

A good list of query parameterization examples in ASP, ColdFusion, C#, Delphi, .NET, Go, Java, Perl, PHP, PL/SQL, PostgreSQL, Python, R, Ruby and Scheme can be found at [http://bobby-tables.com](http://bobby-tables.com/) and the [OWASP Cheat Sheet on Query Parameterization](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html).

**Caution on Query Parameterization**

Certain locations in a database query are not parameterizable. These locations are different for each database vendor. Be certain to do very careful exact-match validation or manual escaping when confronting database query parameters that cannot be bound to a parameterized query. Also, while the use of parameterized queries largely has a positive impact on performance, certain parameterized queries in specific database implementations will affect performance negatively. Be sure to test queries for performance; especially complex queries with extensive like clause or text searching capabilities.

### Secure Configuration
Unfortunately, database management systems do not always ship in a "secure by default" configuration. Care must be taken to ensure that the security controls available from the Database Management System (DBMS) and hosting platform are enabled and properly configured. There are standards, guides, and benchmarks available for most common DBMS. 

A quick guidance on providing a secure configuration can be found in the [Database Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html#database-configuration-and-hardening).

### Secure Authentication
All access to the database should be properly authenticated. Authentication to the DBMS should be accomplished in a secure manner. Authentication should take place only over a secure channel. Credentials must be properly secured and available for use.

A quick guidance on providing a secure authentication process can be found in the [Database Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html#authentication).

### Secure Communication
Most DBMS support a variety of communications methods (services, APIs, etc) - secure (authenticated, encrypted) and insecure (unauthenticated or unencrypted). It is a good practice to only use the secure communications options per the *Protect Data Everywhere* control.

A quick guidance on providing a secure communication mean can be found in the [Database Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html#connecting-to-the-database).

## Vulnerabilities Prevented
* [OWASP Top 10 2021-A3: Injection](https://owasp.org/Top10/A03_2021-Injection/)
* [OWASP Mobile Top 10 2014-M1 Weak Server Side Controls](https://www.owasp.org/index.php/Mobile_Top_10_2014-M1)

## References
* [OWASP Cheat Sheet: Query Parameterization](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)
* [OWASP Cheat Sheet: Database Security](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)
* [Bobby Tables: A guide to preventing SQL injection](http://bobby-tables.com/)
* [CIS Database Hardening Standards](https://www.cisecurity.org/cis-benchmarks/)
