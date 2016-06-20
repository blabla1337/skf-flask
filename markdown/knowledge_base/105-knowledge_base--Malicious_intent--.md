
Malicious intent
-------

**Description:**

Before pushing a code live you should check the software for malicious code in order to 
make sure no developers with evil intent made backdoors or deliberately put in exploits.
The same goes for whenever you are using third-part software and components.

Also verify, that third party components come from trusted repositories.


**Solution:**

Running your code through a static code analyser or auditing tools could give you a change 
to find malicious pieces of code which could be embedded into the software. 
Also if the new or adjusted functionality is critical then check manually it in the form 
of a code review for back doors, Easter eggs, and logic flaws.

This should also mean that authorised administrators must have the capability to verify the integrity of 
all security-relevant configurations to ensure that they have not been tampered with.
