# SQL query
-------

## Example:


    """
    Django supports almost most of the database backends.  

    A model contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table.

    CREATE TABLE myapp_person (
    	"id" serial NOT NULL PRIMARY KEY,
    	"first_name" varchar(30) NOT NULL,
    	"last_name" varchar(30) NOT NULL
	);

	Model for the above SQL query
	"""

	from django.db import models

	class Publisher(models.Model):

   		name = models.CharField(max_length=30)
   		address = models.CharField(max_length=50)

		def __str__(self):

    		return ' '.join([
        		self.name,
        		self.address,
    		])

    //In order to add your model to django, you have to add the app in INSTALLED_APP
    INSTALLED_APPS = [
    	//...
    	'myapp',
    	//...
	]

	"""
	After adding the application, inorder to make the changes we need to make migrations
	and migrate - For creating tables 
	"""

	$ python manage.py makemigrations
	$ python manage.py migrate
	//Needs to be added

	"""
	Inserting data into the database - create, add and commit
	"""
	
	book = Publisher(name=p1, address=p2)
	book.save()

	"""
	Delete entries from the table
	"""
	
	instance = Publisher.objects.get(name=name)
	instance.delete()

	"""
	Querying Records
	"""
	
	//Retrieve the user with username
	instance = Publisher.objects.filter(name=name).all()
	instance.address

	"""
	SQL raw string approach
	"""
	
	if inputValidation(inputParameter, 'alphanumeric') == False:
		people = Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [inputParameter])
	
		for p in people:
			print("%s is %s." % (p.first_name, p.age))