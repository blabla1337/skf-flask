# Secure Database Configuration
-------

## Example:

    
    // in order for the connection to be secure, it is best practice the credentials and all the relevant sensitive information about the database to be kept at the server configuration files. For this reason the following changes have been made at tomcat's server.xml configuration file. 

    <Resource auth="Container" driverClassName="com.mysql.cj.jdbc.Driver" maxActive="100" maxIdle="30" maxWait="10000" name="jdbc/myJdbc" password="javadude" type="javax.sql.DataSource" url="jdbc:mysql://localhost:3306/aggregate_control" username="user"/>

    <Resource auth="Container" driverClassName="com.mysql.cj.jdbc.Driver" maxActive="100" maxIdle="30" maxWait="10000" name="jdbc/auditlogs_Jdbc" password="javadude" type="javax.sql.DataSource" url="jdbc:mysql://localhost:3306/auditlogs" username="user"/>

    the above configuration example indicates that there are two different mysql connections to the database. One refers to the auditlog database and the other refers to the aggregate_control database using the jdbc mysql connector. As you can see the mysql username and password are residing in the web application server configuration file.

    As for the server side code, in order to be informed of the existence of the databases, the following code must be located in the file /META-INF/context.xml

    <?xml version="1.0" encoding="UTF-8"?>

    <Context path="/JServletSide" docBase="/JServletSide"
      crossContext="true" reloadable="true" debug="1">


    <Resource name="jdbc/myJdbc" auth="Container" type="javax.sql.DataSource"
              maxActive="100" maxIdle="30" maxWait="10000"
              username="user" password="javadude" 
              driverClassName="com.mysql.cj.jdbc.Driver"
              url="jdbc:mysql://localhost:3306/aggregate_control"/>

    <Resource name="jdbc/auditlogs_Jdbc" auth="Container" type="javax.sql.DataSource"
              maxActive="100" maxIdle="30" maxWait="10000"
              username="user" password="javadude" 
              driverClassName="com.mysql.cj.jdbc.Driver"
              url="jdbc:mysql://localhost:3306/auditlogs"/>
              </Context>

    The above snippet indicates the database  resource that will be use in the servlet in ordet to perform a succesfull connection to the database

    Afterwards the following servlet snippet will be used for the database connection. 

    Context initContext = new InitialContext();
    Context webContext  = (Context)initContext.lookup("java:/comp/env");
    DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
    Connection conn = ds.getConnection();

    the init context line refers to the database resource inside the context.xml file

    Also in order for the application to map the database reference we have to include the following lines inside the /WEB-INF/web.xml 
    
    <resource-ref>
        <description>DB Connection</description>
        <res-ref-name>jdbc/myJdbc</res-ref-name>
        <res-type>javax.sql.DataSource</res-type>
        <res-auth>Container</res-auth>
      </resource-ref>
      <resource-ref>
        <description>DB Connection</description>
        <res-ref-name>jdbc/auditlogs_Jdbc</res-ref-name>
        <res-type>javax.sql.DataSource</res-type>
        <res-auth>Container</res-auth>
      </resource-ref>

      