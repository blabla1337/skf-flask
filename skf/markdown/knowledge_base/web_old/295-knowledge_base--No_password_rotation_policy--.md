##Description:
Some policies require users to change passwords periodically, often every 90 or 180 days. 
The benefit of password expiration, however, is debatable. Systems that implement such 
policies sometimes prevent users from picking a password too close to a previous selection.

This policy can often backfire. Some users find it hard to devise "good" passwords that are 
also easy to remember, so if people are required to choose many passwords because they have 
to change them often, they end up using much weaker passwords; the policy also encourages 
users to write passwords down. Also, if the policy prevents a user from repeating a recent password, 
this requires that there is a database in existence of everyone's recent passwords (or their hashes) 
instead of having the old ones erased from memory. Finally, users may change their password repeatedly
within a few minutes, and then change back to the one they really want to use, circumventing the 
password change policy altogether.

##Mitigation:
Only force users to update their passwords when the password strength that is enforced by the application
is no longer sufficient to withstand brute force attacks due to increase of computing power.
