# Question
 
What is the problem here?
 
```
`public void runQuery(String firstColValue, int secColValue) throws SQLException {
    String sql = "update TABLE_X set COLUMN_X = '" + firstColValue + "' where USER = " + secColValue;
    try (PreparedStatement pStmt = wrappedConnection.prepareStatement(sql)) {
        pStmt.executeUpdate();
        }
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'firstColValue' parameter is vulnerable for malicious injection. It is also same for 'secColValue' parameter as well but the data type is integer which does not leave any attack surface. And additionally, the code shows a wrong implementation of 'PreparedStatement'.