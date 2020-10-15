##Description:
A replay attack (also known as playback attack) is a form of attack in which
a valid data transmission is maliciously or fraudulently repeated or delayed. 
This is carried out either by the originator or by an adversary who intercepts the data and re-transmits it.
This is one of the lower tier versions of a "Man-in-the-middle attack".

##Mitigation:
Replay attacks can be prevented by tagging each encrypted component with a session ID and a component number.
Using this combination of solutions does not use anything that is interdependent on one another. 
Because there is no interdependency there are fewer vulnerabilities. This works because a unique, 
random session id is created for each run of the program thus a previous run becomes more difficult to replicate. 
In this case an attacker would be unable to perform the replay because on a new run the session ID would have changed
