## Description:

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

## Solution:

Download a HTML sanitizer and configure it to your specific needs. When configuring the sanitizer make sure
you disable all unused components. The less options an attacker has to insert into your application the less
his attack surface becomes. Also before implementing this HTML sanitizer on a production environment have
it first thoroughly examined by security testers since it is a very delicate function.
