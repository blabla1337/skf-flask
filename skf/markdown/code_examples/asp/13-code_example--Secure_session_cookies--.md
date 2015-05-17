
Secure session cookies
-------

**Example:**

	Whenever  a cookie is sent over a secured connection, the cookie should be set
	with the secure flag, in order to guarantee the integrity of the data it contains.

	in the <system.web> element, add the following element:

	<httpCookies requireSSL="true" />

	whenever you have a <forms> element in your system.web block, this setting will 
	override the setting in httpCookies, changing it's value back to false.

	In that case, you need to add the requireSSL="true" attribute to the forms element as well.

	<system.web>
		<authentication mode="Forms">
			<forms requireSSL="true"> <-- secure flag
				/* forms content */
			</forms>
		</authentication>
	</system.web>



	
