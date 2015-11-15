
WYSIWYG editors
-------

**Description:**

WYSIWYG editors can be a great risk to your web application since it allows direct
HTML as input to make the user perform styling on their submissions. This is why the
editor should be put under a strict sanitation protocol to prevent injections. 

The first thing to take into consideration whenever you want to use WYSIWYG editors on 
your web application is to use as limited options as possible. Only the options which
are necessary for your applications intended operation should be applied. This decreases
the attackers attack vector drastically and leaves less room for error in your WYSIWYG
editor in terms of your HTML sanitation. 

When providing your web application with an WYSIWYG editor you should also take note that
most people just want to use bullets, make text bold or underline some text. They mostly
do not understand half the functionalities the editors are providing.

**Solution:**

You should start of with a whitelisting of different type of attributes and tags
you want your WYSIWYG editor to allow. i.e:

for tags:
<h1></h1>
<ul></ul>
etc

or for attributes:
class
id
etc

Everything not matching your filter should be rejected and stripped by your sanitizer.

For protection against JavaScript execution via common attributes there are basically 
three entry points for code/javscript injection which you should controll in order to 
prevent injection. These entry points take form as: Single quotes, Double quotes, and 
back-ticks. Whenever you monitor your application for these inputs and you properly encode 
them on injection than you have developed a good filter for your attributes.

What about encoding? 
Unless your ops are doing explicit decoding on the server side you should not worry about 
encoding. Encoded attacks will not help the attacker to break the context and execute 
malicious code.

<div class="AttackersInjection">Double quotes</div>
<div class='AttackersInjection'>Single quotes</div>

For protection against JavaScript execution via 'style' attribute there are basically 
six entry points for code/javscript injection which you should controll in order to 
prevent injection. These entry points take form as: Single quotes, Double quotes, small
parenthesis, backslash, smaller than sign, and ampersand. Whenever you monitor your 
application for these inputs and you properly encode them on injection than you have 
developed a good filter for your style.

The angular bracket(smaller than sign) is used for whenever the editor puts the 
styling in a <style>  tag attacker break a style tag with the bracket

Added value about this method is leaves al other style options in tact.

It is also optional to download a HTML sanitizer specialy designed to do this work for you if available.

Note: whenever using an of the shelf HTML sanitizer this sanitizer should be thoroughly tested/audited by
professionals in order to verify if it does not leave holes for attack.





