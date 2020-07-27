##Description:

Applications frequently use the actual name or key of an object when generating web pages. 
Applications don’t always verify the user is authorized for the target object. 
This results in an insecure direct object reference flaw. Testers can easily manipulate parameter 
values to detect such flaws and code analysis quickly shows whether authorization is properly verified.

The most classic example:
The application uses unverified data in a SQL call that is accessing account information:

String query = "SELECT * FROM accts WHERE account = ?";
PreparedStatement pstmt = connection.prepareStatement(query , ... );
pstmt.setString( 1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery();

The attacker simply modifies the ‘acct’ parameter in their browser to send whatever 
account number they want. If not verified, the attacker can access any user’s account, instead of 
only the intended customer’s account.

http://example.com/app/accountInfo?acct=notmyacct

## Solution:

Preventing insecure direct object references requires selecting an approach 
for protecting each user accessible object (e.g., object number, filename):

Use per user or session indirect object references. This prevents attackers from directly 
targeting unauthorized resources. For example, instead of using the resource’s database key, 
a drop down list of six resources authorized for the current user could use the numbers 1 to 6 to 
indicate which value the user selected. The application has to map the per-user indirect reference 
back to the actual database key on the server.

Check access. Each use of a direct object reference from an untrusted source must include an access control 
check to ensure the user is authorized for the requested object.
