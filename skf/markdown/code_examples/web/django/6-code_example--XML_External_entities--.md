# XML External entities
-------

## Example:

    
	"""
	Django’s serialization framework provides a mechanism for “translating” Django models into other formats. By which we can avoid XXE while using XML. 
	
	Models can be easily translated to other formats such as XML, Json, YAML
	"""

	//Serialization of SomeModel defined in Models.py
	from django.core import serializers 
	data = serializers.serialize("xml", SomeModel.objects.all())

	//Save serialized data to file file.xml	
	XMLSerializer = serializers.get_serializer("xml")
	xml_serializer = XMLSerializer()
	with open("file.xml", "w") as out:
		xml_serializer.serialize(Question.objects.all(), stream=out)
	data = xml_serializer.getvalue()

	//Deserialize the XML
	for obj in serializers.deserialize("xml", data):
		//Accessing object
		obj.object


	






