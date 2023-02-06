# White listing

A whitelist, also known as an allowlist or passlist, is a crucial mechanism in ensuring the security of an application. By default, it denies all entities access to specific privileges, services, or recognition, but allows a pre-determined and explicitly identified set of entities.

In the context of software development and application security, a whitelist serves the same purpose but with a different implementation. Consider the example of a directory traversal vulnerability and the Local File Inclusion (LFI) attack that was previously mentioned in the introduction. Implementing a whitelist helps to prevent unauthorized access to sensitive information and resources, as well as the exploitation of security vulnerabilities. By explicitly specifying which entities are allowed, a whitelist helps to increase the overall security of the application and reduce the risk of potential attacks.

---
## example 1

Whitelisting is a technique for implementing access control in a secure manner, by defining a list of acceptable inputs or actions and denying all others. Here are a few steps to implement whitelisting in software development, along with examples to help illustrate each step:

* Identify the inputs that need to be validated: In order to apply whitelisting, you first need to identify the inputs that need to be validated. This might include form inputs, user-supplied data in API calls, or any other type of data that is being passed into your application.

* Define the acceptable inputs: Once you have identified the inputs that need to be validated, you can define the acceptable inputs for each field. For example, you might want to allow only alphanumeric characters for a username field, or limit the length of a message field to a certain number of characters.

* Validate inputs against the whitelist: Once you have defined the acceptable inputs, you need to validate the user-supplied data against the whitelist. This can be done using string functions, regular expressions, or other methods, depending on the programming language and libraries you are using. For example, in Python you might use the re library to validate a string against a pattern.

* Reject invalid inputs: If the user-supplied data does not match the acceptable inputs defined in the whitelist, it should be rejected. This could be done by raising an error or exception, returning an error message to the user, or taking some other action to prevent the data from being processed further.

Here's a code example in Python to illustrate these steps:

```python
import re

def validate_username(username):
    # Define the acceptable inputs for a username
    whitelist = re.compile("^[a-zA-Z0-9]+$")

    # Validate the input against the whitelist
    if not whitelist.match(username):
        # Reject the input if it does not match
        raise ValueError("Invalid username")

# Example usage
try:
    validate_username("john.doe")
except ValueError as e:
    print(e)  # Output: Invalid username
```
---

## example 2

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

We want to take control away from an attacker.
Let's assume in this situation there is only but a subset of text files the person should be able to read from the server. Then we could simply define these file names in an ```array``` or a ```list``` and check if they match the user input.

```python
@app.route("/home", methods=['POST'])
def home():
    filename = isAllowed(request.form['filename'])
    content = readFileContent(filename)
    return render_template("index.html",read = content)

def isAllowed(filename):
    list = ["default.txt", "intro.txt", "other-text.txt"]
    return "default.txt" if not filename in list

def readFileContent(filename):
    f = open(filename,'r')
    read = f.read()
    return read
```

As you can see from the new example, we check the filename against a pre-defined subset of filenames to verify if the input that comes into the application is allowed to get into the **file read operator**. If the input does not match the whitelist we default to a default value namely ```default.txt```.

The **white list** approach is the opposite of using a **blacklist**, which is a list of things denied when everything is allowed by default.

---

## Why not a blacklist?
Blacklisting is an overall discouraged strategy. This has to do with the fact that for every "filter" you introduce in the application, hackers will find smart bypasses around them to exploit your application still.

**Example**, before there were standard libraries to prevent [XSS](https://owasp.org/www-community/attacks/xss/) developers created filters (blacklists) to prevent this attack. They started with matching on ```<script>``` tags and reject input if the pattern was matched by the blacklist. Now, hackers were smart and tried to inject ```<ScripT>``` and bypassed the filter. After which developers would normalize input to lowercase and pattern matched to prevent the hacker's last iteration of injecting script tags into the application. By then hackers found another bypass for the normalization and started to use **javascript event handlers** to achieve their goal such as ```<h1 onload='alert("XSS")'>HACK</h1>```.

---

## In summary

As you can already tell, the blacklisting approach becomes a cat-and-mouse game fairly quickly and is therefore not a recommended approach to go about.

Blacklisting, or maintaining a list of forbidden items, can be an inadequate approach to software security for several reasons:

* Maintenance: Blacklists need to be constantly updated to reflect the latest threats, making them a maintenance-intensive approach.

* Incomplete coverage: New security threats can arise and the blacklist may not have entries for these, making the system vulnerable.

* False positives: Sometimes, legitimate input may be accidentally blocked by the blacklist.

* Easy to bypass: Attackers can easily evade blacklists by simply changing their attack vectors, making them an easily bypassable security measure.

In summary, blacklists can be difficult to maintain, provide incomplete coverage, lead to false positives, and can be easily bypassed by attackers. It is recommended to use other security measures such as whitelisting, input validation, and least privilege instead of solely relying on blacklists for security.

### Lab time!


You will shortly engage with the hands-on security lab! In this lab, you will have the opportunity to witness the real-world consequences of a common type of vulnerability in web applications known as an injection flaw. You will gain a deeper understanding of how these types of attacks can be carried out, and the damage they can cause. By conducting various simulated security tasks, you will learn about the techniques used to detect and prevent injection flaws, and the steps that can be taken to mitigate the risk of such attacks. This lab will provide you with a hands-on experience that will help you better understand the importance of secure coding practices and the consequences of ignoring them. Get ready to dive into the world of injection flaws and see the impact they can have!

![Possibilities](assets/edison.png)

#### Sources:
[White list](https://en.wikipedia.org/wiki/Whitelist)
