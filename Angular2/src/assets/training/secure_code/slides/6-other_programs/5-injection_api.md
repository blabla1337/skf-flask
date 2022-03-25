## Calling Other Programs: Other Issues

### Call APIs for Programs and Check What Is Returned

When writing programs, try to call only application programming interfaces (APIs) that are intended for use by programs.

Usually a program can invoke any other program, including those that are really designed only for human interaction. However, it is usually unwise to invoke a program intended for human interaction in the same way a human would. The problem is that programs’ human interfaces are intentionally rich in functionality and are often difficult to completely control. For example, interactive programs often have “escape” codes, which might enable an attacker to perform undesirable functions. Also, interactive programs often try to intuit the “most likely” defaults; this may not be the default you were expecting, and an attacker may find a way to exploit this.

Usually there are parameters to give you safer access to the program’s functionality, or a different API or application that is intended for use by programs; use those instead.

This goes the other way, too. If you are developing an application with an interactive user interface for humans, make sure there is a way for a program to directly access that functionality as well. That will make it much easier to integrate your application into something larger.

Of course, once you receive information, make sure that you check for error conditions (either directly or via raising an exception). If a request with untrusted data fails, your program should not just blithely go on as if it succeeded. Error handling is such an important topic that we will cover that next.