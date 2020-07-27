##Description:

If an application allows the user to attempt for out-of-band authentication using an old out-of-band authentication key, it increases the likelihood of replay attacks and can assist in comprising a user session.


## Solution:

The most effective solution is to reject out of band authentication attempts after 10 minutes and also ensure the out-of-band authentication key can be used only once. The system providing out-of-band authentication keying material should discard the key once it used.
