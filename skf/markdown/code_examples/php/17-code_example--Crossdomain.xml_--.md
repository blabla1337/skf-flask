
Crossdomain.xml 
-------

**Example:**


A bad example of a crossdomain.xml would be:

	<?xml version="1.0" ?>
	<cross-domain-policy>
	  <site-control permitted-cross-domain-policies="master-only"/>
	  <allow-access-from domain="*"/>
	  <allow-http-request-headers-from domain="*" headers="*"/>
	</cross-domain-policy>

Because it allows acces from all other domains.

Instead of this approach you might want to use the following restrictions. 
Example by twitter's crossdomain.xml:

	<?xml version="1.0" encoding="UTF-8"?>
	<cross-domain-policy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.adobe.com/xml/schemas/PolicyFile.xsd">
	  <allow-access-from domain="twitter.com" />
		<allow-access-from domain="api.twitter.com" />
		<allow-access-from domain="search.twitter.com" />
		<allow-access-from domain="static.twitter.com" />
		<site-control permitted-cross-domain-policies="master-only"/>
	  <allow-http-request-headers-from domain="*.twitter.com" headers="*" secure="true"/>
	</cross-domain-policy>


	
