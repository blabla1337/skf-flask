
XML External entities
-------

**Example:**



	    <?php

		/*
		The overall prevention method for loading external entities is adding the following line of code:
		This line of code function tells the underlying libxml parsing to not try to interpret the values 
		of the entities in the incoming XML and leave the entity references intact.
		*/

		libxml_disable_entity_loader(true);

		?>





	