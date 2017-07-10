XML External entities
-------

## Example:


	/*
	The overall prevention method for loading external entities is adding the following line of code:
	This line of code function tells the underlying libxml parsing to not try to interpret the values 
	of the entities in the incoming XML and leave the entity references intact.
	*/

	/*
	In .NET Framework versions 3.5 and earlier, DTD parsing behavior is controlled by the 
	Boolean ProhibitDtd property found in the System.Xml.XmlTextReader and System.Xml.XmlReaderSettings
	classes. Set this value to true to disable inline DTDs completely:
	*/
	
	XmlTextReader reader = new XmlTextReader(stream);
	reader.ProhibitDtd = true;

	//or

	XmlReaderSettings settings = new XmlReaderSettings();
	settings.ProhibitDtd = true;
	XmlReader reader = XmlReader.Create(stream, settings);

	/*
	The default value of ProhibitDtd in XmlReaderSettings is true, but the default value 
	of ProhibitDtd in XmlTextReader is false, which means that you have to explicitly set 
	it to true to disable inline DTDs (NOT RECOMMENDED).
	*/
	
	/*
	In .NET Framework version 4.0, DTD parsing 
	behavior has been changed. The ProhibitDtd property has been deprecated in favor of 
	the new DtdProcessing property. You can set this property to Prohibit (the default value) 
	to cause the runtime to throw an exception if a <!DOCTYPE> element is present in the XML:
	
	At this point, we have hardened this code so that it is much less vulnerable to XML bombs, 
	but we haven't yet addressed the dangers posed by malicious external entities. 
	You can improve your resilience against these attacks if you customize the behavior 
	of XmlReader by changing its XmlResolver. XmlResolver objects are used to resolve external 
	references, including external entities. XmlTextReader instances, as well as XmlReader 
	instances returned from calls to XmlReader.Create, are prepopulated with default 
	XmlResolvers (actually XmlUrlResolvers). You can prevent XmlReader from resolving 
	external entities while still allowing it to resolve inline entities by setting the 
	XmlResolver property of XmlReaderSettings to null. This is attack surface reduction 
	at work again; if you don't need the capability, turn it off:
	*/
	
	XmlReaderSettings settings = new XmlReaderSettings();
	settings.ProhibitDtd = false;
	settings.MaxCharactersFromEntities = 1024;
	settings.XmlResolver = null;
	XmlReader reader = XmlReader.Create(stream, settings);

	/*
	Alternatively, you can set the DtdProcessing property to Ignore, which will not throw 
	an exception on encountering a <!DOCTYPE> element but will simply skip over it and not 
	process it. Finally, you can set DtdProcessing to Parse if you do want to allow and process inline DTDs.
	
	For extra detailed information please visit:
	
	https://msdn.microsoft.com/en-us/magazine/ee335713.aspx 

	*/
	



	