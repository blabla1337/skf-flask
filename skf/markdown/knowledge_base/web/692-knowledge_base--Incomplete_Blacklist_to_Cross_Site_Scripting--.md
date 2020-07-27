##Description:

The product uses a blacklist-based protection mechanism to defend against XSS attacks, but the blacklist is incomplete, allowing XSS variants to succeed.

While XSS might seem simple to prevent, web browsers vary so widely in how they parse web pages, that a blacklist cannot keep track of all the variations. The XSS Cheat Sheet [REF-564] contains a large number of attacks that are intended to bypass incomplete blacklists.

##Mitigation:
