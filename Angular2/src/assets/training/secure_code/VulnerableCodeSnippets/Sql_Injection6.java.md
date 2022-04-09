# Question
 
What is the problem here?
 
```
public static void main(String []args){
    System.out.println("Your first name and last name:");
    String firstname = args[0];
    String lastname = args[1];
    String query = "SELECT id, firstname, lastname FROM authors WHERE firstname = "+ firstname +" and lastname = " + lastname;
    PreparedStatement pstmt = connection.prepareStatement( query );
    try
    {
        ResultSet results = pstmt.execute( );
    }
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. Program arguments are vulnerable for injection attacks. These parameters are being concatenated to build a SQL query without a proper sanitization. You may also notice 'PreparedStatement' is in use, however it is non-compliant and parameterization is missing.