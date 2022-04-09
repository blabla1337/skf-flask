# Question
 
What is the problem here?
 
```
def player_stats(full_name, season, week_number):
    conn = mysql.connector.connect(user='admin', password='mysuperscreetpassword', host='localhost', database='sportDB')
    cursor = conn.cursor()
    statement = "SELECT * FROM game WHERE playerName = (\'{}\') AND season = {} AND weekNumber < {};".format(full_name, season, week_number)
    cursor.execute(statement)
    rows = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    if rows:        
        return True
    else:
        msg = "No such user exists!"
        return False
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. The function parameters are vulnerable for malicious injection and no input sanitization or parameterized query takes place.