##Description:

Whenever a user browses a section of a web-based application that contains sensitive information the user should be challenged authenticate again using a higher assurance credential to be granted access to this information.
This is to prevent attackers from reading sensitive information after they successfully hijacked a user account.


##Mitigation:

Verify the application has additional authorization (such as step up or adaptive authentication) so the user is challenged before being granted access to sensitive information. This rule also applies for making critical changes to an account or action.
Segregation of duties should be applied for high-value applications to enforce anti-fraud controls as per the risk of application and past fraud.

