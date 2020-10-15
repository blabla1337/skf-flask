##Description:

This is a mitigation of the risk that a password can leak by any means towards a possible attacker. Because of password reuse, this could happen not only due to a leak in your site. Changing the password to a new one minimizes the damage.

Also, users really don't like changing their passwords. So what users used to do when forced to change their password was to change it twice - once to some temporary password and then a second time back to the original password.

##Mitigation:

Keep a number of password hashes entries greater than the number of times that the change password functionality execution is permitted and validate that the new password hash is not one of those entries.
