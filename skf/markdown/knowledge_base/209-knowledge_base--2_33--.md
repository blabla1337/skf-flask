#Description

Browser autocomplete and password managers could be used by attackers to steal sensitive
information. Whenever an application is susceptible to XSS (Cross site scripting) attacks,
the attacker can inject forms into the application which are autocompleted by the browser.

The attacker can than use javascript to read the input fields and steal credentials or
other sensitive information.

#Solution

The browser should explicitly be told for al the input fields that the autocomplete function
should be turned of. The "autocomplete=off" HTML attribute should be added to al the input and
hidden input fields in the form you want to disable the autocomplete of.

