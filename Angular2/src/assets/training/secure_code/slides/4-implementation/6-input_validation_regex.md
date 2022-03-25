### Introduction to Regular Expressions

If you already know about regular expressions, feel free to skip this unit.

A regular expression (a *regex*) is a sequence of characters that defines a text pattern. Practically all programming languages have a built-in system or easily-acquired library that implements a regular expression language, so it is usually easy to start using regular expressions in a program regardless of how it is implemented.

However, some software developers have never used regexes. This unit provides a brief introduction if you are not already familiar with them. If you already understand regexes, feel free to skip to the next unit!

Historically regexes were developed to make it easy to search for text, though they are now often used to determine if some text matches a pattern. There are many implementations of regex systems, but since they all come from the same historical root they have much in common.

The most trivial rule is that a letter or digit matches itself. That is, the regex “**d**” matches the letter “**d**”. Most implementations use case-sensitive matches by default, and that is usually what you want.

Another rule is that square brackets surround a rule that specifies any of a number of characters. If the square brackets surround just alphanumerics, then the pattern matches any of them. So **[brt]** matches a single “**b**”, “**r**”, or “**t**”.

The pattern “**.**” matches any one character, with the possible exception of the newline character. If you want to match a literal period, precede it with a backslash (“**\.**”). Practically every implementation of regexes has a mechanism to let you decide if “**.**” should match a newline.

A regex pattern is usually a sequence of rules, stated one after the other. For example, the regex pattern “**ca[brt]**” will match the text “**cab**”, “**car**”, or “**cat**”, because the letters “**c**” and “**a**” match themselves, and “**[brt]**” matches a single “**b**”, “**r**”, or “**t**”.

In fact, by default, regexes *search* for the given pattern in a string. That is, normally a regex implementation will see if a pattern matches some text if it starts at the first character, then second character, and so on, reporting if it can find *any* match. So the pattern “**ca[brt]**” will also match “**abdicate**” because there is a “**cat**” in the word “**abdicate**”.

Regular expressions can do much more, though. If you follow a pattern with “**&#42;**”, that means “*0 or more times*”. So the regex pattern “**a&#42;b&#42;x**” describes a pattern of 0 or more **a**’s, followed by 0 or more **b**’s, followed by **x**. This pattern matches strings like “**aabx**”, “**bbbx**”, and “**abx**”, but not “**bax**” or “**aabb**”. Most regex implementations also support “**+**” for “*1 or more times*” and “**?**” for “*0 or 1 times*”. Most regex implementations also let you use parentheses to group expressions, for example, “**f(abc)&#42;d**” matches if there is an “**f**”, followed by 0 or more instances of the sequence “**abc**”, followed by the letter “**d**”.

You can usually do a case-insensitive match through some option. Make sure you set the locale if you use case-insensitive matching, since different languages have different rules, and sometimes the rules can be complex. For example, in German the lowercase “sharp-s” character “**ß**” is equivalent to the uppercase “**SS**” when using a case-insensitive match. In some cases, you may only want to do “*ASCII case-insensitive matching*”; this compares a sequence of code points as if all ASCII code points in the range 0x41 to 0x5A (A to Z) were mapped to the corresponding code points in the range 0x61 to 0x7A (a to z).

There is far more to regexes. In fact, there is a whole book on just regular expressions, [*Mastering Regular Expressions, 3rd Edition*](https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/), by Jeffrey Friedl (2006), and there are many tutorials on regexes such as the  [Regular Expressions for Regular Folk](https://refrf.shreyasminocha.me/) tutorial by Shreyas Minocha. But that introduction will get us started, because we are now going to discuss how regexes can be used for input validation.

### Using Regular Expressions for Text Input Validation

Many programs need to quickly validate input text from untrusted sources. While there are many ways to do that, regexes are often an especially useful tool for input validation of text. Regexes are generally quick to write down (so they take very little development time), easy to use, and widely available. They’re also flexible enough for many input validation tasks, compact, and normally execute very quickly. They are also widely known and understood. These are important advantages; if writing input validation is too hard, it won’t be done. They don’t solve all possible input validation problems, but they are useful enough that they are important to know.

Regular expressions were originally used in software for *searching* for text patterns, not for validating text inputs against a pattern. Regexes are also good at text input validation, but there are a few things you need to know so you can use regexes correctly for text input validation.

#### Match, Don’t Search

A key issue with regexes is that by default most regex implementations *search* to see if a given pattern can be found anywhere within some text. When we are doing input validation we don’t want to search; we want to know if all the text input *exactly matches* a pattern. That means we need to be able to ask the regex implementation *“does this input text exactly match this pattern”* - and reject the input if it doesn’t match. As with any other input validation, we need to make our pattern as limiting as possible, and if the input doesn’t match, then reject the input.

The usual way to require a regex to match an entire input is to include *anchors* in the regex. Just start your regex pattern with a *start anchor* - usually represented by “**^**” or sometimes “**\A**” - and end the pattern with “**$**” or sometimes “**\z**”. With these, the entire input must match the pattern. For example, this regex will match *any* text that contains “**cab**”, “**car**”, or “**cat**” - it will even match “**abdicate**” - so you should *not* use a regex like this for input validation:

**ca[brt]**

In contrast, this regex will only match *exactly* the words “**cab**”, “**car**”, or “**cat**” in most regex implementations, because “**^**” means *“match the beginning”* and “**$**” means *“match the end”*:

**^ca[brt]$**

In some implementations (depending on the option), “**^**” may mean *“beginning of any line”* not *“beginning of the string”* - and you usually want *“beginning of the string”*. A similar thing can happen with “**$**”. From here on we will assume that “**^**” and “**$**” mean beginning and end of the entire string.

#### Know Your Regex Implementation

Almost every programming language has at least one good regex implementation. They all share many features, but many are slightly different. So, when you use a regex implementation you have not used before, look at its documentation every time you use an operation that you have not used before. Here are some variations to look for.

There are three major families of regex language notations:

1. Basic regular expression (BRE)
This is the default for **grep** and **sed**. This is defined by the POSIX standard. However, its syntax is sometimes a little awkward, so in most cases, it is easier to use extended regular expressions instead for input validation.

2. Extended regular expression (ERE)
This is defined by the POSIX standard and adds capabilities like using parentheses for grouping and “**+**” for *“one or more”*. This is often used in C programs. So for example, “**[B-D]+**” means *“one or more of the letters B, C, or D”*.

3. Perl Compatible Regular Expressions (PCRE)
This is mostly an extension of the ERE format; many other programming languages use this family of regex languages. It includes capabilities like “**\d**” to represent digits.

 Here are some important things that vary:

* Sometimes there is an option or alternative method to match the entire input; if available, you can use that instead of the anchoring symbols. Make sure it matches the whole thing, though; some methods only check the beginning.

* Sometimes “**^**” matches the beginning of the whole data, while in others it represents the beginning of any line in the data. The same goes for “**$**”. This is often controlled by a *multiline* option.

* The “**.**” for representing *“any character”* doesn’t always match the newline character (**\n**); often there is an option to turn this on or off.

* Does it properly support Unicode and the encoding you are using?

* Can it handle data with the **NUL** character (byte value 0) within the data? If not, and your input data could have an embedded **NUL** character, you will need to validate the data first to make sure there are no **NUL** characters before passing the data to the regex implementation.

* Is matching case-sensitive? Usually it is case-sensitive by default, and there is a trivial way to make it case-insensitive. If it is case-insensitive, remember that exactly what characters have case-insensitive matches depends on the locale. For example, “**I**” and “**i**” match in the English (“**en**”) and the C locale (“**C**”), but not in the Turkish (“**tr**”). In the Turkish locale, the Unicode LATIN CAPITAL LETTER I matches the LATIN SMALL LETTER DOTLESS I - not a lowercase “**i**”.

In some languages, such as in Ruby, you normally use **\A** and **\z** instead of “**^**” and “**$**” to match string begin/end, because “**^**” and “**$**” match line begin/end instead.

#### Branch Priority

Almost all regex implementations support *branches* - that is, “**aa|bb|cc**” matches **aa**, **bb**, or **cc**. All ERE and PCRE implementations support branches, and even some BRE implementations support branches if they are written as “**&#92;|**” instead of “**|**”. The *priority* of the branch operation is standard, but it is not what some users expect. The regex “**^aa|bb$**” means *“either it begins with aa OR it ends with bb”*, not *“exactly aa or bb”*.  When you are using regexes for input validation, a sequence of branches that is not surrounded by parentheses is practically always a mistake. What you normally want is “**^(aa|bb)$**” which means *“exactly aa or bb”*.

** So, whenever you have a branch (“|”) in a regex, group the whole expression with branches using parentheses.**

#### Test Input Validators

Again, you should know what your software should not accept, and use some of those examples as automated test cases to ensure that your software will correctly reject them. This is especially important with regexes, because it is easy to write a regex that looks fine but allows inputs it wasn’t intended to. This can help you catch, for example, missing anchors or failures to surround branches with parentheses.