### Sidequest: Text, Unicode, and Locales

Often you receive text as input (either directly or as part of some larger structure). We will describe text as simply a sequence of characters. If the text input is untrusted, you then need to validate that text. To understand this, we must understand what text *is*. A remarkably large number of developers have never learned much about text - even though it is one of the most common data types - so let’s make sure you understand that first. If you are already confident you are familiar with text issues such as Unicode, encoding, and locales, feel free to skip on.

#### Code Points and Encoding

Digital computers do not directly handle characters; we instead need to assign a number to each character. Different character sets with different assignments were created for different languages, and this created interoperability nightmares. In the vast majority of cases today you will use the character assignments specified by Unicode and ISO/IEC 10646, which define a Universal Character Set (UCS) that assigns a unique number (*code point*) for every character. For example, they assign the Latin character capital “A” the decimal number 65.

Historically, it was thought that 16 bits would be enough to identify all characters, but this was mistaken and was changed in 1996 (they now use 21 bits to encode any character). As a result of this mistake, some programming languages have a “character” type (e.g., Java’s **char**) that is only 16 bits long. A 16-bit data type cannot, by itself, store any arbitrary 21-bit character, so in programming languages and APIs with a 16-bit “character”, a “character” is sometimes only half of an actual character.

Text that uses these assignments need to be exchanged using an *encoding*. There are five standard encodings for Unicode: UTF-32 (big-endian and little-endian), UTF-16 (big-endian and little-endian), and UTF-8. Generally, you should use UTF-8 unless you have a reason to do otherwise. UTF-16 and UTF-32 both have two forms: “little endian” and “big endian”. If you don’t know if the recipient expects big-endian or little-endian, you should add a *byte order marker* at the beginning of the text to make sure that the receiver interprets it correctly, and when receiving UTF-16 or UTF-32, your application needs to pay attention to that. A critical issue is that some sequences of bytes are *not* valid, so when we do input validation, we will need to ensure that the data we receive is valid for the encoding we expect.

#### Locales

Interpreting characters is more complicated than you might think. Much depends on the “locale”, which defines the user’s language, country/region, user interface preferences, and probably character encoding. For example, on Unix/Linux systems, Australian English with UTF-8 encoding is represented as the locale **en_AU.UTF-8**. Locale is important, because it affects how characters are interpreted. For example, it affects:

* Collation (sorting) order

* Character classification (what is a “letter"?). Ranges like “A-Za-z” do not list *all the alphabetic characters* in arbitrary locales. If you use the C or POSIX locale and are only processing ASCII characters, then that range is the complete list of alphabetic characters, but that is not true in general.

* Case conversion (what is upper/lower case of a character, if it exists?). Note that even if there is a conversion, it might not convert to a single character in a given locale.

If you want to interpret text in the same way regardless of locale, the usual solution is to use the “C” aka “POSIX” locale - however, be careful, because that is not always what the user wanted.

Case conversion is especially fraught. Some languages don’t have upper and lower case letters. Even if they do, the mapping between them is different between different locales. So the uppercase version of a letter is *not* fixed - it is based on the locale!

A great example of this are the Turkic languages that use the Turkish alphabet. In this alphabet dotted and dotless “I” are distinct letters with upper and lower case forms. For example, lowercase dotted “i” when capitalized becomes capital dotted “İ” (not uppercase dotless “I” as it does in an English locale), and uppercase dotless “I” when lowercased becomes lowercase dotless “ı”. Note that “i” and “I” are *not* equal in a case-insensitive match in a correctly-implemented system for such locales. This has resulted in several security vulnerabilities, and we will occasionally mention this in the course because it is a great example of the kinds of mistakes that can happen if you are not aware of it.

If you want to know if “two sequences of characters are equivalent” ignoring case, then in the general case you need to call a routine to do this *and* provide it the locale to use. This raises the issues about equivalence in general, which we will discuss next.

#### Unicode Equivalence

Many programmers assume that if a sequence of text “code points” are different, they are different strings. While that is fine for some purposes, that is the wrong mental model for others, even if you assume that you want a “case sensitive” match. Unicode had to be developed in a way that was compatible with pre-existing standards, and that led to some complications.

In some cases you should use library routines to test for Unicode canonical equivalence. That is because there are some code points, or sequences of code points, that in many circumstances should be considered *equivalent* in the sense that they should always appear identical, even if they have different underlying values. For example, the code point U+006E (the Latin lowercase “n”) followed by U+0303 (the combining tilde “◌̃”) is canonically equivalent to code point U+00F1 (“ñ”).  Another example is the character “Å” that can be represented as U+00C5 (the letter “LATIN CAPITAL LETTER A WITH RING ABOVE”) or as U+212B (“ANGSTROM SIGN”): these two values should be considered equivalent.

In some other cases, you should use routines to test for Unicode compatibility. That is because there are some sequences that might appear different but would have the same underlying meaning. For example, the code point U+FB00 (typographic “ﬀ”) is compatible, but not equivalent, to U+0066 U+0066 (two Latin “f” letters). Equivalent strings are always compatible, but compatible strings are not always equivalent.

This is a pain, so the Unicode standard defines text normalization procedures, called Unicode normalization. Unicode normalization turns equivalent or compatible sequences into the exact same sequence of characters. There are 4 normalization forms:

* NFD (Normalization Form Canonical Decomposition)
Characters are decomposed by canonical equivalence, and multiple combining characters are arranged in a specific order.

* NFC (Normalization Form Canonical Composition)
Characters are decomposed and then recomposed by canonical equivalence.

* NFKD (Normalization Form Compatibility Decomposition)
Characters are decomposed by compatibility, and multiple combining characters are arranged in a specific order.

* NFKC (Normalization Form Compatibility Composition)
Characters are decomposed by compatibility, then recomposed by canonical equivalence.

From a security point-of-view it normally does not matter *which* Unicode normalization you use, but if you want to determine if two strings are equal, you need to be *consistent* about the normalization you use when comparing them. Also note that once you normalize a sequence of characters, you cannot in general regenerate exactly the original sequence.

#### Visual Spoofing

*Visual spoofing* happens when two different strings are mistaken as being the *same* by the user. Attackers will sometimes use visual spoofing as part of an attack.

Visual spoofing can even happen in the ASCII subset of Unicode. The digit “0” looks like the uppercase letter “O”, and the digit “1” looks like the lowercase letter “l”. For example, an attacker might try to create a malicious **paypa1.com** domain instead of **paypal.com**. The sequence “rn” is sometimes misread as the letter “m”! That said, most users of Latin alphabets are aware of these problems, and many fonts take care to make them more distinguishable.

But once we move beyond the ASCII subset, many other tricks exist:

* Decomposition
“ƶ” may be expressed as U+007A U+0335 (z + combining short stroke overlay) or as U+01B6. This means that different sequences of bytes may still indicate the same letter (and thus look identical). Normalization solves this problem.

* Mixed-script
Greek omicron & Latin “o” typically look the same, even though they are in different sections of Unicode.

* Same-script
Some characters simply look similar. E.g., “-” Hyphen-minus U+002D vs. hyphen “‐” U+2010.

* Bidirectional Text Spoofing
Some languages are mostly right-to-left, but switch in certain situations to left-to-right. Thus, Unicode includes mechanisms to indicate direction. But this means that the string “olleh”, surrounded by “use right-to-left”, will visually look the same as “hello”.

Visual spoofing can be very challenging to counter in general. Normalization and using distinctive fonts is not always enough, but it can sometimes be very helpful.
