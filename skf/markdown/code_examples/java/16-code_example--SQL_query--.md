
SQL query
-------

**Example:**

[source,java]
      /*
      This example uses a prepared statement in order to insert data into the database.
      Because this method enforces the user to prepare all user input  passed into the query, it always escapes SQL
      injections so none could be accidentally forgotten.
      */

      /*
      For detecting a possible attack on your application simply escaping the userinput is obviously not enough.
      Therefore, you'll want to verify the input as submitted by the user does not contain malicous code.
      In this example the expexted input is a-z/0-9:
      */
        String employeeId = request.getParameter('userId');
        String salary = request.getParameter('salary');
        Pattern numeric = Pattern.compile(".*[^0-9].*");
        if(!numeric.matcher(employeeId).find() && !numeric.matcher(salary).find()){

            //Set a log for whenever there is unexpected userinput with a threat level:
            log(userId, "Invalid expected input", "FAIL", Calendar.getInstance(), "privilege", "HIGH" );

            /*
		          Set counter; if counter hits 3 the user's session must terminated.
		          After 3 session terminations, the user's acount must be blocked
		        */
            counter++;
            if(counter > 2 ){
                blockUser(userId);
            }

            String updateQuery = "UPDATE EMPLOYEES SET SALARY = ? WHERE ID = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(updateQuery);
            preparedStatement.setInt(1, salary);
            preparedStatement.setInt(2, employeeId);
        }

        //Always use parametrized queries with prepared statements.
        //For example, with Hibernate (HQL) named parameters
        Query query = session.createQuery("UPDATE EMPLOYEES SET SALARY = :salary WHERE ID = :employeeId");
        query.setParameter("salary", salary);
        query.setParameter("employeeId", employeeId);

        //or with JPA
        Query query = entityManager.createQuery("UPDATE EMPLOYEES SET SALARY = :salary WHERE ID = :employeeId");
        query.setParameter("salary", salary);
        query.setParameter("employeeId", employeeId);

        //The important thing to remember:
        //Never construct SQL statements using string concatenation of unchecked input values
        PreparedStatement preparedStatement = connection.prepareStatement("UPDATE EMPLOYEES SET SALARY = " + request.getParameter('salary') + " WHERE ID = " + request.getParameter('userId'));
