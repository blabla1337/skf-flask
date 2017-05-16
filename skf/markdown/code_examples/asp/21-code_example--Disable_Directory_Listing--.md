Disable Directory Listing
-------

**Example:**

	<configuration>
	  <location path="Secured">
		<system.webServer>
		  <directoryBrowse enabled="false" />
		</system.webServer>
	  </location>
	</configuration>

NOTE: This example applies to IIS 7+, for IIS 6 you'll have to do it from IIS Manager
