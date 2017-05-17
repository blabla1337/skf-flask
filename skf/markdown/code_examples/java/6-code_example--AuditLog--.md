AuditLogs
-----------

***Example:***

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

package com.edw;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDateTime;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import org.apache.log4j.Logger;

public class AuditLog {

	
	public int countID;
	public int userID; 
	public int count; 
	public int blocker; 
	public static String validation = "pass"; 
	
	final static Logger logger = Logger.getLogger(AuditLog.class);
	
	
	public void SetLog(String userid, String message, String state, LocalDateTime localDateTime, String ThreatLevel, String remote_address)
    {
		
	
		try(FileWriter fw = new FileWriter("C:\\log.txt", true);
			    BufferedWriter bw = new BufferedWriter(fw);
			    PrintWriter out = new PrintWriter(bw))
			{
			    out.println(userid + " - " + message + " - " + remote_address /*REMOTE_ADDR from servlet*/ + " - " + state + " - " + LocalDateTime.now()
			    + " - " +  localDateTime);

			} catch (IOException e) {
			    logger.error("cannot write to file : "  + e.toString());
			}		
    }
	
	public void SetLog(String userid, String message, String state, LocalDateTime localDateTime, String ThreatLevel)
    {
		
	
		try(FileWriter fw = new FileWriter("C:\\log.txt", true);
			    BufferedWriter bw = new BufferedWriter(fw);
			    PrintWriter out = new PrintWriter(bw))
			{
			    out.println(userid + " - " + message + " - " + state + " - " + LocalDateTime.now()
			    + " - " +  localDateTime);

			} catch (IOException e) {
			    logger.error("cannot write to file : "  + e.toString());
			}		
    }
	
	public String counter(int counting)
    {
		
		
		Connection connect = null;
	    try {
		
		
		Context initContext = new InitialContext();
		Context webContext  = (Context)initContext.lookup("java:/comp/env");
		DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
		connect = ds.getConnection();			
		
			/*
	        First we select the counts from the count table in order to verify if the user session should be terminated
	        or that the user should be locked out.
	        */
	      String sqlquery = "SELECT * from counter";
	   
	      //We bind the parameter in order to prevent sql injections
	      PreparedStatement state = connect.prepareStatement(sqlquery);
	      
	      // execute the query, and get a java resultset
	      ResultSet res = state.executeQuery();
	      
	      //Next we read the value from the database and put it into a variable
	      while (res.next())
	      {
	    	userID = res.getInt("userID");
	        count  = res.getInt("count");
	        blocker = res.getInt("blocker");
	
	      }
	      
	      state.close();
	      connect.close();
		
		
		
	    } catch (SQLException | NamingException e) {
			 logger.error("cannot search database. check query" + e.toString() );
			 return "cannot search database. check query"; 
		}
		
		
		Connection conn = null;
	    try {
		
		
		Context initContext = new InitialContext();
		Context webContext  = (Context)initContext.lookup("java:/comp/env");
		DataSource ds = (DataSource)webContext.lookup("jdbc/myJdbc");
		conn = ds.getConnection();			
		
			/*
	        First we select the counts from the count table in order to verify if the user session should be terminated
	        or that the user should be locked out.
	        */
	      String query = "SELECT * from counter WHERE userID = ?";
	   
	      //We bind the parameter in order to prevent sql injections
	      PreparedStatement st = conn.prepareStatement(query);
	      st.setInt(1, userID);
	      
	      // execute the query, and get a java resultset
	      ResultSet rs = st.executeQuery();
	      
	      //Next we read the value from the database and put it into a variable
	      while (rs.next())
	      {
	        count  = rs.getInt("count");
	        blocker = rs.getInt("blocker");
	
	      }
	      
	      st.close();
	      conn.close();
		
		
		
	    } catch (SQLException | NamingException e) {
			 logger.error("cannot search database. check query" + e.toString() );
			 return "cannot search database. check query"; 
		}
	    
	    
	     //We add the counting to the database results for the final value
	    count  = count + counting; 
        int finalCount = count;
        blocker = blocker + counting;
        int finalBlock = blocker;
	    
        
        //Here we connect to the database  
        Connection conn2 = null;
        try {
        Context initContext2 = new InitialContext();
		Context webContext2  = (Context)initContext2.lookup("java:/comp/env");
		DataSource ds2 = (DataSource)webContext2.lookup("jdbc/myJdbc");
		conn2 = ds2.getConnection();	
         
	      // create the java mysql update preparedstatement
	      String query2 = "UPDATE counter SET count = ?, blocker = ? WHERE userID = ?";
	      PreparedStatement preparedStmt2 = conn2.prepareStatement(query2);
	      preparedStmt2.setInt(1, count);
	      preparedStmt2.setInt(2, blocker);
	      preparedStmt2.setInt(3, userID);

	      // execute the java preparedstatement
	      preparedStmt2.executeUpdate();
	      
	      
	      conn2.close();
		} catch (SQLException | NamingException e) {
			 logger.error("SQL insert query error in update counter" + e.toString() );
			 return "SQL insert query error in update counter";  // this can be used to dispatch the response back to the client showing a corresponding message
			} 
        
        
        if (finalCount == 3)
        {
        	validation = "terminate";        	
        }

        if (finalBlock > 3)
        {        	
        	int access = 0; //0 is considered as FALSE in MySQL
        	
        	//Here we connect to the database  
            Connection conn3 = null;
            try {
            Context initContext3 = new InitialContext();
    		Context webContext3  = (Context)initContext3.lookup("java:/comp/env");
    		DataSource ds3 = (DataSource)webContext3.lookup("jdbc/myJdbc");
    		conn3 = ds3.getConnection();	
             
    	      // create the java mysql update prepared statement
    	      String query3 = "UPDATE users set access = ? WHERE userID = ?";
    	      PreparedStatement preparedStmt3 = conn3.prepareStatement(query3);
    	      preparedStmt3.setInt(1, access);
    	      preparedStmt3.setInt(3, userID);

    	      // execute the java preparedstatement
    	      preparedStmt3.executeUpdate();
    	      
    	      validation = "block";
    	      
    	      conn3.close();
    		} catch (SQLException | NamingException e) {    					    			
    			logger.error("SQL insert query error in update access" + e.toString() );
    			return "SQL insert query error in update access" ;  // this can be used to dispatch the response back to the client showing a corresponding message    		    		
    		}	
        }
        
		return validation;    		
    }
	
	
}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
