### Countering Cross-Site Scripting (XSS)

[Web application]

#### The XSS Problem

One of the most common vulnerabilities in web applications is a Cross-Site Scripting (XSS) vulnerability. In an XSS attack, the attacker tries to fool a web browser to do something malicious (usually to run malicious code) by inserting information into a valid web page or web application that will be misinterpreted by the receiving browser as some sort of malicious action. It is always abbreviated as XSS, because CSS already has another meaning (Cascading Style Sheets). XSS is an especially common problem in pages or sites that allow user comments, because user comments are an easy vector for attackers to insert their malicious information.

The fundamental problem is that web browsers (which operate as clients) must presume that if they were sent some data, the sender intended to send it. After all, what else could the web browser presume? However, if the sender creates that data by combining constant data it controls with attacker-provided data, and the attacker-provided data is not properly sanitized, then the combination could become malicious. The mishmash of this combination would then be interpreted by the web browser as a request to do something malicious, which it then dutifully does.

For example, if the web server sends HTML embedded with a string from an untrusted user, and an attacker arranges for that string to contain **&lt;script&gt; do_something_malicious(); </script>**, the user might end up running the JavaScript program **do_something_malicious()**.

In XSS, the system that is eventually attacked is the *web browser*. However, the *cause* of the attack is improper code written in the *sender* of the data to the web browser. There are three common patterns for XSS:

* **Persistent Store**
The malicious data is stored in a database for later retrieval. For example, an attacker submits a comment with an embedded malicious script; when someone else uses their web browser to view the comments, the web browser runs the malicious script.

* **Reflection**
The malicious data is sent by the victim’s web browser to the server (typically inside a URL) and immediately reflected back to the browser.

* **DOM-based**
The web client sends the attack data to itself, typically using data provided from an attack and then sent via the DOM using JavaScript.

🔔 XSS is such a common mistake in web applications that it is 2017 OWASP Top 10 #7. It is also 2019 CWE Top 25 #2. In CWE it is [CWE-79](https://cwe.mitre.org/data/definitions/79.html), *Improper Neutralization of Input During Web Page Generation (‘Cross-site Scripting’)*.

#### The XSS Solution: Escape Output

The standard way to counter XSS is to escape all output that might be from an attacker and is not specifically approved. In many ways, this is the best countermeasure. Done right, it completely counters the attack and is very flexible. For example, if you have untrusted HTML data from an attacker, apply the standard HTML escapes unless you have a good reason to do otherwise:

**Standard HTML Escapes**

<table>
  <tr>
    <td>Original</td>
    <td>Escaped HTML</td>
  </tr>
  <tr>
    <td>&amp;</td>
    <td>&amp;amp;</td>
  </tr>
  <tr>
    <td>&lt;</td>
    <td>&amp;lt;</td>
  </tr>
  <tr>
    <td>&gt;</td>
    <td>&amp;gt;</td>
  </tr>
  <tr>
    <td>"</td>
    <td>&amp;quot;</td>
  </tr>
  <tr>
    <td>‘</td>
    <td>&amp;#39; or &amp;apos;</td>
  </tr>
</table>


In output sanitizing, just like input validation, it is often best to identify an allowlist and escape the rest. However, sometimes required output escapes are a well-defined list that you can directly apply, because sometimes you *can* safely enumerate the categories as we have done here for HTML. There are technically cases where you don’t have to apply the escapes to untrusted data, but in HTML it is often simpler and faster to just automatically apply them all unless you have a specific need to permit something else. Of course, these are only the escapes for HTML itself; these are not enough by themselves for other data formats (such as embedded URLs and HTTP headers).

Here is the problem: You have to be *perfect*. If you escape output correctly 99.9% of the time, and you generate output in 1,000 places, your program is *vulnerable*. You may be a genius, but that is not relevant; even geniuses make mistakes. Even if the software was *originally* perfect, a later change can easily introduce a vulnerability. We need a better solution than “*never make a mistake that is easy to make*” - especially when something happens over and over again.

In most cases, the best solution for XSS is to **_choose a framework or library that automatically escapes HTML output for you_**. That way, the output escaping is done, but you don’t have to constantly think about it. Instead, the output system automatically escapes the output for you (this is sometimes called *auto escaping*). This escaping is typically done using one of the many templating systems available that let you specify the constant template (which is trusted and therefore goes through unescaped) and the data (where untrusted data is escaped by default).

There are lots of options that do this. The JavaScript library React, for example, escapes by default any values embedded in its JSX language before rendering it. Ruby on Rails escapes HTML values by default when using its ERB templates. The Python web framework Flask uses the Jinja template library to render templates, and Jinja autoescapes data rendered in an HTML template. This is absolutely not a complete list; auto escaping is a very common capability in web frameworks. We strongly recommend that you only choose web frameworks and output libraries that will escape HTML by default; there are many good ones to choose from.

#### When You Need to Allow Unescaped Untrusted Data

Occasionally you *do* need to allow unescaped data through. One reason you might *want* to omit some escapes is that you want untrusted data to have some action that escaping would prevent. For example, let’s say that you want untrusted users to provide HTML that will italicize some of their text. In that case, you will want to let **&lt;i&gt;** and **&lt;/i&gt;** (italics) through, even though you would normally escape the **&lt;** and **&gt;** characters.

The problem is that once you allow anything additional through, the code necessary to properly escape output is much more complicated. For example, you need to make sure that every opening tag (**&lt;i>**) has a matching tag, that they nest properly, that they either don’t have attributes or those attributes are themselves allowed, and that only the tags and attributes that you allow are let through. There are many cases where this becomes a vulnerability. After all, many frameworks escape data by default, but when developers need to let something through, they sometimes allow *too much* through.

In that case, where possible, use libraries *already designed* to allow only what you want, and escape everything else. Most widely-used programming languages and frameworks already have libraries that let you state what to let through, and then escape, strip, or forbid the rest.

#### URLs

We have focused on escaping HTML, because that is the biggest problem in web applications. But HTML can embed other kinds of data, and of those, perhaps the most common are URLs.

Embedded URLs must also be escaped, and the rules for escaping URLs are different. The URL syntax is generally **scheme:[//authority]path[?query][#fragment]**. For example, in the URL **&lt;https://www.linuxfoundation.org/about/&gt;**, the scheme is “**https**”, authority “<b>www.linuxfoundation.org</b>”, path is “**/about/**”, and this example has no query or fragment part. Sometimes you need special characters in the path, query, or fragment. The conventional way to escape those parts of the URLs is to first ensure the data is encoded with UTF-8, and escape as “**%hh**” (where **hh** is the hexadecimal representation) all bytes except for “safe” bytes, which are typically **A-Z**, **a-z**, **0-9**, “**.**”, “**-**”, “**&#42;**”, and “**&#95;**”. The Java routine **java.net.URLEncoder.encode()** turns all spaces into “**+**” instead of “**%20**”; both the “**+**” and “**%20**” conventions are in wide use.

#### XSS Alternatives

You should normally use a framework that automatically escapes HTML by default.

If for some reason you can’t, you can build a wrapper that does the escaping for you and sends the output. A wrapper is riskier if it is easy to not call the wrapper. If you do use a wrapper, the wrapper should also perform the output. If you separately call an escape routine and then call to produce output, then it is especially easy to forget to call the wrapper. E.g., if you do **SendOutput(EscapeHTML(data))**, it will be far too easy to use the vulnerable **SendOutput(data)** instead.

An alternative sometimes suggested is to use very harsh input filtering that prevents all HTML metacharacters (**&amp; &lt; &gt; &quot; &#39;**). In theory, this prevents XSS in HTML. If you *can* limit your input like this, you should do so, since you should always limit your untrusted inputs as much as possible. In practice, while harsh input filtering can help counter other attacks, it is usually *not* enough to counter XSS. The problem is that usually some inputs eventually have to allow some HTML metacharacters. For example, an O’Malley would be unhappy with a system that did not allow single quotes in a name. Even a system that starts with this limitation often outgrows it, so you cannot count on harsh input validation *by itself* to counter XSS. Yes, use harsh input validation where you can as a hardening measure - but it’s not enough to counter XSS.

A very mild hardening measure is to set the attribute **HttpOnly** on cookies. That way, if a malicious script is run, it cannot see the cookie value. You *should* set this limitation when you can, because it limits privilege, but this is a very mild hardening measure that is only useful if you apply *other* measures as well.

XSS is usually best countered by choosing a framework or library that automatically escapes output for you. However, programs often have many outputs. It would be best if we paired this solution with something else that limited the damage when a mistake *is* made. On the web there is a solution: the Content Security Policy (CSP). The next unit will discuss this.
