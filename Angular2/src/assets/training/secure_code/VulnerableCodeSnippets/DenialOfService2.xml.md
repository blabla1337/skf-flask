# Question
 
What is the problem here?
 
```
<?xml version="1.0" encoding="UTF-8"?>
<Context path="/products">
  <Resource name="jdbc/prodDataBase"
      auth="Container"
      type="javax.sql.DataSource"
      description="prodDataBase"
      removeAbandoned="true"
      removeAbandonedTimeout="30"
      maxActive="5"
      maxIdle="5"
      maxWait="60000"
      username="root"
      password="p@$$w0rd"
      driverClassName="com.mysql.jdbc.Driver"
      url="jdbc:mysql://127.0.0.1:3306/prodDataBase"/>
</Context>
```
 
-----SPLIT-----
 
# Answer

It is a Denial Of Service issue. The application will only accept 'maxActive="5"' connections. The attacker can consume all connection pool and then the service will be inaccessible for other users.