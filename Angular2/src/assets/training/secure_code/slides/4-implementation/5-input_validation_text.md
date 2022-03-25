### Validating Text

Now that we have an understanding about text, let’s talk about validating it. In almost all cases there are at least two checks to do on text from an untrusted source:

* Validate that the text is in the expected text encoding. As noted earlier, unless you have a reason to do otherwise, we recommend using the UTF-8 encoding. UTF-8 will let you work with scripts from arbitrary languages, is backwards-compatible with ASCII, and is widely supported. UTF-8 is a good encoding, but not every sequence of bytes is valid UTF-8. Many vulnerabilities have occurred because a system accepted bytes from an attacker that are not valid UTF-8. So it is really important to validate UTF-8 text before you accept it from an untrusted source.

* Check if it is within the minimum and maximum lengths, if there are minimum and maximum lengths. Many systems will want to have a maximum simply to prevent attackers from sending absurdly-large amounts of data.

In some cases it may be very difficult to check much more. Personal names, in particular, are challenging, especially if you must deal with names in all locales. Many locales have conventions that are different from other locales; for example, is the given name or the surname (e.g., family name) listed first? There may not even be a surname or a given name. Names may contain spaces (even within a given name or surname), and, of course, there is no guarantee that the name uses only Latin or Chinese characters. For a discussion of the challenges, see the [*Falsehoods Programmers Believe About Names – With Examples*](https://shinesolutions.com/2018/01/08/falsehoods-programmers-believe-about-names-with-examples/) article by Tony Rogers (2018). 

In many cases, though, there is more that you should do to validate text. In many cases, text values have additional rules they need to obey, and those rules vary depending on each text input.

Sometimes the text value must be one of a short list of values. That’s easy, just store the allowed collection somewhere (e.g., in a set or dictionary). Then, every time you receive input, validate that the input is one of the allowed values.

But that leaves us with the many text inputs that have rules, but they are not just a list of allowed values. They may be dates, times, part numbers, phone numbers, locations, and a host of other kinds of data. We still need to validate those inputs, and many programs have many different kinds of data. That means we need some way to *easily* describe those validation rules. The common tool for this purpose is regular expressions. In the next unit, we will optionally explain regular expressions (regexes) if you are not familiar with them; the unit after that will explain how to use regular expressions to validate inputs.
