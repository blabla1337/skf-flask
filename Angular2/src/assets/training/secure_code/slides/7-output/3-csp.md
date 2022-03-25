### Content Security Policy (CSP)

[Web application]

When creating web applications, a really important tool for limiting damage is a *Content Security Policy* (CSP). If it exists, the CSP tells the receiving web browser what is allowed and not allowed from a security perspective. CSP by itself does not prevent most attacks, but can make many vulnerabilities harder to exploit or greatly reduce their impact. That makes CSP an important *defense in depth measure* to reduce risk.

Normally a reference to the CSP is sent as an HTTP header (called **Content-Security-Policy**), and like all HTTP headers, the user receives it *before* the user receives the main content. You can also send CSP information as a **&lt;meta&gt;** HTML element with the **http-equiv** attribute set to **Content-Security-Policy**. However, using the **&lt;meta&gt;** element is not as good as using the HTTP header, because the system has already started processing the HTML by this point. So try to use the HTTP header instead. If you have to use CSP via an HTML element, include this **&lt;meta&gt;** element as soon as you can in your HTML, so that it will take effect as soon as possible.

Perhaps the most important CSP capability is that CSP can control which scripts are allowed to run. By default, a web browser runs all scripts sent to it. This is terrible if there is an XSS vulnerability, because the attack may be able to sneak code into the page and have the victim’s web browser run it. A better secure solution is to separate the code from the data and limit privilege. We can do this with CSP.

Here is a simple CSP that prevents a large number of attacks. This CSP says that resources (in particular scripts and styles) are only from the source site (**&#39;self&#39;**), and that **inline** or **evals** for scripts and styles are not allowed (because they have not been specifically permitted):

**Content-Security-Policy: default-src ‘self';**

The challenge with this CSP is that to use it to its full potential, we need to *stop* using inline styles and scripts. The HTML can request the *loading* of JavaScript files and CSS styles, but the JavaScript and CSS styles must be in separate files. The HTML may include lots of information important to scripts and styles (such as the **tag**, **class**, and **id**), but the HTML cannot embed scripts and styles directly.

Never using inline scripts and styles is widely considered good practice, but it is more than that; it dramatically improves security. If inline scripts and styles are ignored, then an XSS attack that subverts an HTML web page *cannot* easily cause an untrusted script or style to be used. This does not prevent all attacks, but it does prevent many, and it makes other attacks dramatically harder. If you can *stop* using all inline scripts and styles, and enforce that through your CSP, the system becomes more resistant to a range of attacks.

But what if this policy is too difficult to implement on a page, or does not meet your circumstance? That is not a problem; simply use a *different* CSP for that page. The CSP specification has a range of options that you can use to permit more operations and restrict others.

As always, your goal is least privilege: try to make the CSP as restrictive as you can. You will often get the most benefit if you modify your system so it can use a more restrictive CSP on all pages, but even a small restriction can have some benefits. Common ways to relax the limitations on scripts and styles are:

1. Have a restrictive CSP on as many web pages as you can, such as only allowing scripts and styles from specific locations on your website (never inline). Then relax the restrictions on pages where that is currently difficult.

2. Allow loading scripts and styles from specific other sites. You can set **default-src** (where script source files are loaded) to allow specific other websites you list. This tells the web browser that you fully trust those specific sites. Be careful; this can hurt user privacy. For example, each organization that manages those other sites will know at *least* whenever a user retrieves that information and their IP address.

3. Allow specific hashes. You can set **default-src** to allow a specific inline program by saying that its cryptographic hash can be executed using the format **‘&lt;hash-algorithm&gt;-&lt;base64-value&gt;’**. This can be a useful intermediate step if you have existing inline scripts, though in the long, term it would be better to move those scripts to a separate file.

CSP has various other mechanisms to limit privileges. Another CSP parameter that is especially important is **frame-ancestors**, which is a great tool for countering clickjacking attacks. A clickjacking attack is one where an attacker can “hijack” a click that the user intended for one purpose, but in fact the click was “hijacked” to do something else. Attackers typically do this by misusing HTML’s frame capabilities. If you don’t use frames - and most sites don’t - you can easily fix this by including “**frame-ancestors ‘none';**” in your policy. If you do use frames, then use “**frame-ancestors ‘self';**” instead.

When you are developing a site it might be wise to go through the CSP specification and try to maximally limit what you ask web browsers to allow. The less you allow, the less attackers can do if you make a mistake. There are other HTTP headers that can help harden a site against attack; in the next unit we will look at a few.