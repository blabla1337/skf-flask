# Length checking

Length checking is an important aspect of software security. It involves setting a maximum limit on the number of characters a variable can contain, known as the "length" of the variable. This technique ensures that the variable is only accepting the expected amount of data, preventing the input of unexpected, large amounts of data which could potentially cause security vulnerabilities. For example, if a user input field is only meant to accept a single word, a length check can be used to limit the number of characters the field can contain to prevent malicious input such as a long string of code. By enforcing length restrictions, the risk of attacks such as buffer overflows is reduced. Length checking is a simple yet effective method to enhance the security of an information system.

---

## Implementing type checking

For the sake of example let us use this poorly written SQL query.

```python    
def getPage(self, pageId):
    db = database_con()
    cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
    return cur.fetchall()
```

Can we spot the coding mistake?

The ```pageId``` parameter in this code example is under the control of a user and is directly
concatenated into this SQL statement. This renders the SQL query displayed above susceptible to SQL injection attacks.

Now, in our hypothetical story, we would most likely never exceed `9999` pages that are being published
by this specific application. 

### method 0

The first solution could be something like displayed below. Although not the ideal solution, we do want to have a centralized means of doing validity checks, instead of having separate functions all over your code. But it helps you get the gist of the story.

```python

def getPage(self, pageId):
    db = database_con()
    filtered = validate_input(pageId)
    cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+filtered)
    return cur.fetchall()

def validate_input(input_string):
    max_length = 100
    if len(input_string) > max_length:
        raise ValueError("Input exceeds the maximum length of {} characters".format(max_length))
    # Proceed with the rest of the processing, now knowing the input has a valid length
    # ...

```

### method 1
There are of course also other methods to limit the # of characters being used by a parameter.
such as in the example below:

```python
#Data validation and settings management using Python type annotations
from pydantic import BaseModel, Field 

class MyPydanticModel(BaseModel):
    pageId: int = Field(..., max_length=5)
```

```c#
//EF code first
 public class Pages
 {
    [MaxLength(5)] 
    public number pageId { get; set; }
 }
```

Now, an attacker could still trigger a SQL error in both scenarios. But the attacker will not be able to deliver a full payload to perform a successful injection. Let's look at a classic ```union select``` payload
that is used in these types of scenarios to read arbitrary data from the database:

```union select username,password from users```

This payload will already be cut short at: 

```union```

As a result, the SQL query is still vulnerable to SQL injection. But exploitation is no longer possible!

As an additional layer, you could add to this also the "type" check to only allow integers
to go into the query and you have an even more solid solution.

These defense mechanisms do not take away from the fact that when you start to write raw
SQL queries you need to use a standardized library that allows you to write queries with
```Parameterized Strings``` and ```prepared statements```. But that is what security is all about, making a layered defense as fail saves when things do not work as expected.

in raw SQL a safe parameterized statement would look a little like this:
```python
def getPage(self, pageId):
    db = database_con()
    sql_select_query = """SELECT pageId, title, content FROM pages WHERE pageId=?"""
    cur = db.execute(sql_select_query, (pageId,))
    return cur.fetchall()
```
---
## in summary

Length checking is a critical aspect of input validation and plays a crucial role in ensuring the security of software systems. By imposing limits on the length of parameters, we prevent potential attackers from exploiting vulnerabilities such as buffer overflows and stack overflows, which can result in arbitrary code execution and compromise the system. Length checking can also prevent SQL injection attacks by limiting the size of user input that is entered into the database. It is important for developers to understand the significance of length checking and to include it as part of their security testing and development practices. Incorporating length checks in the input validation process can significantly reduce the risk of security breaches and ensure that software systems are protected against malicious attacks.

### Lab time!

You will shortly engage with the hands-on security lab! In this lab, you will have the opportunity to witness the real-world consequences of a common type of vulnerability in web applications known as an injection flaw. You will gain a deeper understanding of how these types of attacks can be carried out, and the damage they can cause. By conducting various simulated security tasks, you will learn about the techniques used to detect and prevent injection flaws, and the steps that can be taken to mitigate the risk of such attacks. This lab will provide you with a hands-on experience that will help you better understand the importance of secure coding practices and the consequences of ignoring them. Get ready to dive into the world of injection flaws and see the impact they can have!