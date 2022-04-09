# Question
 
What is the problem here?
 
```
[HttpGet("{user_ID}")]
public string checkUser(string user_ID)
{
    user_ID = user_ID.Replace("select", ""); 
    string conString = "Server=localhost;Database=companyDB;Trusted_Connection=True;";
    using (SqlCommand cmd = new SqlCommand("SELECT userName,userEmail FROM users WHERE userId = '" + user_ID + "'"))
    {
        using (SqlConnection con = new SqlConnection(conString))
        {
            con.Open();
            cmd.Connection = con;
            SqlDataReader reader = cmd.ExecuteReader();
            string _result = "";
            while (reader.Read())
            {
                _result += reader[0].ToString() + ":" + reader[1].ToString();;
            }
            return _result;
        }
    }
}
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'user_ID' parameter is vulnerable. The input is not being checked properly and the code concatenates words for query building. You may also notice, it replaces 'select' key words with nothing, however it can be easily bypassed with 'selselectect'.