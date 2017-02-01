Include anti clickjacking headers
-------

**Description:**

Clickjacking, also known as a "UI redress attack", is when an attacker uses multiple
transparent or opaque layers to trick a user into clicking on a button or link on another
page when they were intending to click on the top level page. Thus, the attacker is
"hijacking" clicks meant for their page and routing them to another page, most likely
owned by another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted
combination of stylesheets, iframes, and text boxes, a user can be led to believe they
are typing in the password to their email or bank account, but are instead typing into an
invisible frame controlled by the attacker.


**Solution:**

To avoid your application from being clickjacked you can add the X-frame-Options header
to your application. These headers can be configured as:

    X-frame-Options: deny

The page cannot be displayed in a frame, regardless of the site attempting to do so.

    X-Frame-Options: sameorign  

The page can only be displayed in a frame on the same origin as the page itself.

    X-Frame-Options: ALLOW-FROM uri

The page can only be displayed in a frame on the specified origin.

You may also want to consider to include "Framebreaking/Framebusting" defense for legacy
browsers that do not support X-Frame-Option headers.

Source:
https://www.codemagi.com/blog/post/194
