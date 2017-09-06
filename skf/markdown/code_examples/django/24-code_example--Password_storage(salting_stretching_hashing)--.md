# Password storage(salting/stretching/hashing)
-------

## Example:

    """
    Django provides a flexible password storage system and uses PBKDF2 by default.

    Password is of the format: 
    <algorithm>$<iterations>$<salt>$<hash>
	"""


	# For the encryption of passwords with salt

	from django.contrib.auth.hashers import make_password

	pwd = make_password('some_password')
	

	
	#Validate your password

	from django.contrib.auth.hashers import check_password

	check_password(password, pwd_hash)