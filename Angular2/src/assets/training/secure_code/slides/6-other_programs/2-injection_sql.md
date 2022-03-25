## Calling Other Programs: Injection and Filenames

### SQL Injection

#### SQL Injection Vulnerability

![image alt text](../../exploits_of_a_mom.png)

**Exploits of a Mom**, retrieved from [xkcd.com](https://xkcd.com/327/), provided under [CC-BY-NC-2.5](https://creativecommons.org/licenses/by-nc/2.5/)

Most database systems include a language that can let you create arbitrary queries, and typically many other functions too (e.g., creating and modifying things). The SQL language is especially common, and while some database systems use other languages, those other languages often have similarities with SQL. Such languages, including SQL, include metacharacters. When attackers can insert metacharacters into a SQL command to cause a security problem, the attack is called an *SQL injection attack*, and the vulnerability is called an *SQL injection vulnerability*.

Even if the database language is not SQL, if it is an attack on a language for a database system it is often called an SQL injection attack (even though this is technically not accurate). We will focus on SQL, because SQL is very common and once you understand how to counter SQL injection attacks, it is easy to generalize this to any database language.

Here is a trivial example; here is a snippet of Java that tries to do an SQL query:

~~~~
    String QueryString = "select * from authors where lastname = ' " + search_lastname + " '; ";
    rs = statement.executeQuery(QueryString);
~~~~

The intent is clear; if **search_lastname** has the value **Fred**, then the database will receive the query “**select * from authors where lastname='Fred';**” - a reasonable SQL query. But remember our warning signs - this code concatenates strings, some of that data is probably provided by an attacker, and we’re doing something called “execute”.  The warning signs are right. Imagine that the attacker provides the input “**Fred’ OR ’a’=’a**”. This will produce the query “**select * from authors where lastname='Fred' OR ’a’=’a’;**” and now the attacker can retrieve the entire database. The attacker could even modify or delete data this way, depending on various factors. This is a simple example of an SQL injection attack; an attacker can insert some characters and inject new or modified commands.

There are many ways to trigger SQL injection attacks; attackers can insert single quotes (used to surround constant character data), semicolons (which act as command separators), “**--**” which is a comment token, and so on. This is not a complete list; different database systems interpret different characters differently. For example, double quotes are often metacharacters, but with different meanings. Even different versions of the *same* database system, or different configurations, can cause changes to how the characters are interpreted. We already know we should not create a list of “bad” characters, because that is a denylist. We could create an allowlist of characters we know are not metacharacters and then escape the rest, but this process is hard to do correctly for SQL.

If you are using a database, you shouldn’t ever be concatenating strings to create a query, because that is easy to get wrong. Remember, we want to try to use a routine that is easy to use correctly.

SQL injection is a special case of injection attacks, and we have already noted that injection attacks are so common and dangerous that they are 2017 OWASP Top 10 #1. SQL injection specifically is such a common cause of security vulnerabilities that just SQL injection is 2019 CWE Top 25 #6. SQL injection is also identified as [CWE-89](https://cwe.mitre.org/data/definitions/89.html), *Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’)*. 

For databases, there are well-known solutions that are far easier to use securely.

#### SQL Injection Solutions

SQL injection vulnerabilities are one of the most common and devastating vulnerabilities, especially in web applications. They are also easy to counter, once you know how to do it.

*Prepared statements* are perhaps the best way to counter SQL injection attacks if you are directly creating SQL commands that need to be secure. Most programming languages have at least one library that implements prepared statements.

Prepared statements allow you to identify placeholders (often a “**?**”) for data that needs to be escaped. A pre-existing library that you call then escapes the data properly for that specific implementation. This approach has many advantages:

1. Since the library does the escaping for you, it is simpler to use and more likely to be right.

2. It tends to produce easier-to-maintain code, since the code tends to be easier to read.

3. It can handle variation in different SQL engines (which is important because different systems often have different syntax rules).

Here is an example of using prepared statements in Java:

~~~~java
    String QueryString = "select * from authors where lastname = ?";
    PreparedStatement pstmt = connection.prepareStatement(QueryString);
    pstmt.setString(1, search_lastname);
    ResultSet results = pstmt.execute( );
~~~~

There are more statements, but the statements are simpler; in particular, the complicated concatenation is now a simple string constant. We still call something called “**execute**” - but remember, avoiding methods named “execute” is just a rule of thumb to help us detect potential problems.

Of course, like any technique, if you use it wrongly then it won’t be secure. Here is an example of how to use prepared statements in Java to produce a probably-insecure program:

~~~~java
    String QueryString = "select * from authors where lastname = '" + search_lastname + "';";
    PreparedStatement pstmt = connection.prepareStatement(QueryString);
    ResultSet results = pstmt.execute( ); // Probably insecure, don’t do this!
~~~~

This insecure program uses a prepared statement, but instead of correctly using “**?**” as a value placeholder (which will then be properly escaped), this code directly concatenates data into the query. Unless the data is properly escaped (and it almost certainly isn’t), this code can quickly lead to a serious vulnerability if this data can be controlled by an attacker.

Many programs use object-relational mapping (ORM). This is just a technique to automatically convert data in a relational database into an object in an object-oriented programming language and back; lots of libraries and frameworks will do this for you. This is fine, as long as the ORM is implemented using prepared statements or something equivalent to them. In practice, any good ORM implementation will do so. So if you are using a respected ORM, you are already doing this. That said, it is common in systems that use ORMs to occasionally need to use SQL queries directly… and when you do, use prepared statements.

There are other approaches, of course. You can write your own escape code, but this is difficult to get correct, and typically a waste of time since there are usually existing libraries to do the job. You can also use stored procedures, which can also help prevent SQL injection, but using them correctly can be a little tricky so we emphasize prepared statements here.

Properly using prepared statement libraries makes it much easier to write secure code. In addition, they typically make code easier to read, automatically handle the variations between how databases escape things, and sometimes they are faster than doing metacharacter escapes yourself.