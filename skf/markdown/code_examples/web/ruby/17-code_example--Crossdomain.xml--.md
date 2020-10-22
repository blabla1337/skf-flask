# Crossdomain.xml
-------

## Example:


		// A bad example of a crossdomain.xml would be:

			<?xml version="1.0" ?>
			<crossdomainpolicy>
				<sitecontrol permittedcrossdomainpolicies="masteronly"/>
				<allowaccessfrom domain="*"/>
				<allowhttprequestheadersfrom domain="*" headers="*"/>
			</crossdomainpolicy>

		//	Because it allows acces from all other domains.

		//	Instead of this approach you might want to use the following restrictions. 
		//	Example by twitter's crossdomain.xml:

			<?xml version="1.0" encoding="UTF8"?>
			<crossdomainpolicy xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance" 
			xsi:noNamespaceSchemaLocation="http://www.adobe.com/xml/schemas/PolicyFile.xsd">
				<allowaccessfrom domain="twitter.com" />
				<allowaccessfrom domain="api.twitter.com" />
				<allowaccessfrom domain="search.twitter.com" />
				<allowaccessfrom domain="static.twitter.com" />
				<sitecontrol permittedcrossdomainpolicies="masteronly"/>
				<allowhttprequestheadersfrom domain="*.twitter.com" headers="*" secure="true"/>
			</crossdomainpolicy>