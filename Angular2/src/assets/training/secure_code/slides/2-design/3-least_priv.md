### Least Privilege

We already noted  that least privilege is an important secure design principle. The basic idea is that each user (human or program) should operate using the fewest privileges possible. In general, don’t allow reading or writing of information unless you need to do that for that user.

Least privilege limits the potential damage from an attack, and also reduces the complexity of security-related interactions. This even extends to the internals of a program: only the smallest portion of a program which needs privileges should (ideally) have them. Of course, at some point, this becomes too complicated to do (and we also want to keep the program as simple as reasonably possible).

#### Ways to Implement Least Privilege

Here are several ways to implement least privilege, depending on the circumstance:

1. **Don’t give a program any special privileges (where practical)**
If this can be done, do it, as this is the best from a security point of view. For example, Linux supports making programs **setuid** or **setgid**, so that simply running the program gives the program the privileges of its owner. If you can completely avoid using this mechanism, consider doing it, because it gives special privileges to programs. There are often safer alternatives; for example, requiring people to log in specifically with privileges (this is the purpose of **sudo**).

2. **Minimize the special privileges a program gets, including minimizing whatever data is accessible to it**
On Linux, you might have a program below (or run on the behalf of) a special group or user that only has specific rights, instead of something more privileged (like root). If you are calling a database system query interface, limit the rights of the database user that the application uses. If your database system uses SQL, you might be able to use the SQL GRANT command to limit the privileges the program gets. Redis users might use Redis’ ACL command to limit privileges.

3. **Permanently give up privileges as soon as possible**
For example, if you are using Linux saved group IDs, user IDs, or capabilities, permanently drop those extra privileges as soon as possible. That way, if the attack happens afterwards, the attacker cannot exploit those privileges.

4. **If you cannot permanently give up privileges, try to minimize the time the privilege is active**
This is less effective, because some attacks can force programs to run arbitrary code. But some attacks can only make programs do a limited number of things, and minimizing when the privilege is active will reduce what an attacker can do.

5. **Break the program into different modules, and give special privileges to only one or a few modules (portions of the program)**
The privileged module will ideally not even fully trust the other parts of your program (aka a *mutually suspicious design*). If you do that, then if some part of your program is subverted, it will limit what an attacker can immediately do. For example, you might split the part of a program that implements a GUI from a different part with privileges. Separation mechanisms like containers, virtual machines, Linux seccomp, and various kinds of security wrappers can help you separate parts of your program so that subversion of one part does not necessarily break another. **_Beware:_** *make sure that you configure these mechanisms to securely separate the modules, and limit the privileges in each part.* These separation mechanisms are often not foolproof, so don’t assume that using them automatically makes your program secure. That said, they can make your program harder to attack and may reduce damage if an attack is successful.

6. **Minimize (limit) the attack surface**
The *attack surface* is the set of operations (e.g., its API and its open network ports) that a potential attacker can access. For example, if you allow public access to some method, then you are giving all attackers access to that method - are you sure you need to? Where possible, limit the operations that a potential attacker can access. If the public does not need access, do not give the public access. In particular, avoid leaving debug operations in production systems that an attacker can access; debug operations are a common source of problems.

7. **Validate (check) input before you accept it**
Don’t just accept data from a potential attacker; check it thoroughly before accepting it. We will discuss input validation in more detail later. Of course, you need to make sure that attackers cannot bypass this input validation; this is such a big issue that it has its own principle, *complete mediation*, aka *non-byassability*. We will be talking about that next.

8. **Sandbox your program**
Intentionally run your program (or part of it) in an environment with intentionally-restricted capabilities.

9. **Minimize privileges for files & other resources**
For example, normally you should not have files writable by everyone (even readable by everyone is often dubious). On Android, a file writable by all could be changed by a different (possibly malicious) application.

Incorrect permissions are such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #15. It is [CWE-732](https://cwe.mitre.org/data/definitions/732.html) (*Incorrect Permission Assignment for Critical Resource*).

#### Examples of Least Privilege

Let’s take a look at a few specific examples.

When developing web-based applications, do not allow users to access (read) files such as the server’s **include** and **configuration** files. This data may accidentally provide enough information (e.g., passwords) to break into the system. If you are using a traditional web server, keep everything you don’t need to serve directly to users outside the “documentation root” (**DOCROOT**); that way, attackers cannot even easily request the information. Deny serving files that you know should not be directly served (such as **include** files).

Don’t allow users to write system configuration files by default (e.g., system files in **/etc** on Linux and Unix), and, where practical, consider preventing reads by normal users as well. The problem is that system administrators often put passwords and keys in configuration files. If there are reasons to give broader read permissions to some of the system configuration information (e.g., in **/etc**), consider creating a system configuration directory instead of a system configuration file where the directory name conventionally ends in **.d**. System configuration directories are often better anyway, because they make it trivial for package managers to add and remove specific configuration files. For security, system configuration directories not only reduce the risk of error, but specific files (such as those with secret keys and passwords) can have more restricted permissions. If you use a system configuration directory, it is less of a problem to allow user read, because it is much easier to protect the secret keys and passwords.

If you implement an external API (e.g., with REST or GraphQL), don’t provide a “write” operation unless you expect it to be used. If you allow writes, try to maximally limit *who* can write. For example, have owners of specific data and only let owners modify that data, instead of allowing anyone to modify anything. If practical, design your software so it cannot write data *even* if it is subverted by an attacker (though this often is not practical).

It is unfortunately common to mismanage privileges. For example, there are many cases where programs have failed to drop privileges in all cases (e.g., because raising an exception skipped the code that dropped privileges, or because the code that was supposed to drop privileges does not work in all cases).

Improper privilege management is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #24. It is [CWE-269](https://cwe.mitre.org/data/definitions/269.html) (*Improper Privilege Management*).