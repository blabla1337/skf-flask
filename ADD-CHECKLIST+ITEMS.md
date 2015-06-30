####Add checklist items:
----------

In order to add new checklist items to the custom checklist
you have to know the build structure of the checklist items.

Let's break them up into peaces:

```
    479--custom--0--.md
```

Red:    Identifier, this number must increment
Blue:   Separators, must be used exactly as seen in example, otherwise the checklist engine fails
Yellow: Name of your checklist
Green:  Vulnerability, This number links to a vulnerability number from the knowledge base.

Whenever the vulnerability is set to zero, the checklist engine will interpreted this
item as a checklist head, instead of an item.

Now whenever we open the file, we find a string of text containing the checklist item
or head as so:

```
    "V3.3 Verify that sessions timeout after a specified period of inactivity."
```
The checklist engine will read this when building the checklist to create the checklists.

####Add knowledge base items:
----------

In order to add new knowledge base items to the s.k.f
you have to know the build structure of the knowledge base items.

Let's break them up into peaces:

```
    5-knowledge_base--csrf_injection--.md
```

Red:   Identifier, this number must increment.
Blue:  Separators, must be used exactly as seen in example, otherwise the checklist engine fails
Yellow: Checklist type
Green: Knowledge base item name, cannot contain special chars like (&><'") 

Now whenever we open this file we can find a small layout for styling.
This styling is also used for dividing the 'description' and 'solution' parts:

```
    CSRF injection		<-- Title as seen in your checklist head
    -------

    **Description:**	<-- Description separator, also ads a bold styling

    Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious Web site,
    email, blog, instant message...............

    **Solution:**	   <-- Solution separator, also ads a bold styling

    To arm an application against automated attacks and tooling you need to use unique tokens 
    who are included into the forms of an applicatio..........
```

In the description part we give an extended description about the attackers attack vector
as wel as in what ways this wil be harming your system.

In the solution we tell how to mitigate and what things you must take into consideration
whenever you put these mitigations into practice.


####Add code examples:
----------

In order to add new code examples to the s.k.f
you have to know the build structure of the code examples.

Let's break them up into peaces:

```
    1-code_example--File_upload--.md
```
Red:    Identifier, this number must increment.
Blue:   Separators, must be used exactly as seen in example, otherwise the checklist engine fails
Yellow: Checklist type
Green:  code example item name, cannot contain special chars like (&><'") 

What we want to achieve when presenting the code examples is teaching the developer the
defensive programming mindset, so we would like to see the examples do the following things
at a minimum:

1. Sanitising / Type checking / whitelisting of userinput
2. Encoding userinput if necessary
3. Active logging
4. mitigation
5. extensive commenting for explaining your steps

The code examples have some styling rules whenever you want to implement them in your
markdown files:

```bash
    Directory/path traversal <-- name as seen in the drop-down head
    -------

    **Example:**			 <-- Bold separator telling where the example starts

        //Your code has to indent the 4 spaces(tab) in order for the markdown engine to know
        //it has to interpreted this as written code
```












