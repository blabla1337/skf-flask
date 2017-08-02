# PHP Object Injection
-------

## Example:

	/*
	Vulnerability occur when unsanitized input is passed into the unserialize function
	*/

	<?php

		class foo{
			public $cmd;

			function __destruct()
			{
				system($cmd);
			}

		}

		$data = $_GET['data'];

		unserialize($data);

	?>

	/*
	In the above example  user can control the input to the unserialize function, which can lead to change in the $cmd variable which can even result in taking over the server.
	*/

	/*
	Do not use unserialize() function with user-supplied input, use JSON functions instead.
	We can use json_decode instead of unserialize.
	Otherwise userinput should not be able to control the unserialize function
	*/

	<?php

		class foo{
			public $cmd;

			function __destruct()
			{
				system($cmd);
			}

		}

		$data = $_GET['data'];

		json_decode($data);

	?>	
