## Input Validation: Numbers and Text

### Input Validation: A Few Simple Data Types

So, how do you do input validation that uses an allowlist (that is, a pattern that is as narrowly-defined as possible)? In short, you do it on each input, and what you check for depends on the type of data. Let’s discuss a few common cases next.

#### Numbers

One common input is a sequence of characters representing a number. Typically, you check numbers (especially integers) to make sure they are between a minimum and maximum value. It is good to do some checking before you convert the text to a number, but in this particular case, check the value *after* converting to a number, to be certain that the *rest* of the program will only see that number if it is in a valid range. Common minimums are 0 and 1. If the number is supposed to be an integer, make sure it is an integer and reject anything else.

Where practical, store the numeric result in a type that is narrowly defined for the purpose. For example, store the number in an integer type if the number is an integer, use an unsigned type if negative numbers are not allowed, and so on. If you have to accept floating point data from an untrusted user (and try not to!), store it in an appropriate type and watch out for its many special cases (such as NaN, infinities, negative 0, underflows, and overflows). For example, normally the floating point value NaN is not equal to any value; it is not even equal to itself. Limiting the type is not always practical because this is very language-dependent; not all languages have such types. For example, JavaScript does not have an unsigned type.

Note that *“only allow an integer between 0 and 200 including those endpoints”* is an allowlist; you have identified the pattern of what is allowed, and anything else will be rejected.

#### Well-Known Special Text Formats

Sometimes your inputs are text with a standard format and there is a library that can do the validation for you. For example, most languages have some routine that can check the format of email addresses. When you have one you can trust, use it!

Sometimes the validation libraries you can use require some configuration. Again, configure them to be as narrow (limiting) as possible. For example, if you accept HTML, limit it to only the tags and attributes that you need. Often when you accept HTML, you need to only accept a few tags (e.g., **&lt;i>** for italics, **&lt;b>** for bold, **&lt;a>** for hyperlinks) and attributes (e.g., the **href** attribute of the **&lt;a>** tag so that you can say where to link to, and maybe an **id** attribute so others can refer to a particular point). Then, when an attacker tries to provide HTML with other tags (for example, a malicious **&lt;script>**), the validator simply will not accept it at all.

Some input formats are composite structures of a lot of other data. For example, JSON, XML, and CSV files can contain lots of other data. You would typically use a trustworthy library to examine and extract the portions of the data you need, and then you would validate each piece. So again, if you extract a sequence of characters representing a number, you would validate the number (e.g., to see if it is within the minimum and maximum range). In many cases, it is a text value. We will further discuss handling composite structures later, but at some point, they will decompose to specific values, often as numbers or text.

Many programs need to validate text fields, but those fields’ rules are not defined in a pre-existing library. Some tools allow us to easily handle them, but to use them, we need to understand some background. We will first need to discuss more about text, unicode, and locales in general. Then we will discuss text validation in general and the common way of doing so - regular expressions.