Timeout a Session
-------

**Example:**

Within your web.config you can configure your session idle timeout.
The default time is set to 20 minutes.
		
	<configuration>
	   <system.web>
		  <sessionState mode="InProc"
						cookieless="true"
						timeout="20"/> <-- Here is where we set the timeout by minutes
		  </sessionState>
	   </system.web>
	</configuration>
