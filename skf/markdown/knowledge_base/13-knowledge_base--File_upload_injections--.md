File upload injections
-------

**Description:**

Uploaded files represent a significant risk to applications.
The first step in many attacks is to get some code to the system to be attacked.
Then the attack only needs to find a way to get the code executed. Using a file upload
helps the attacker accomplish the first step.

The consequences of unrestricted file upload can vary, including complete system takeover,
an overloaded file system or database, forwarding attacks to back-end systems, and simple
defacement.

There are really two classes of problems here.
The first is with the file metadata, like the path and file name.
These are generally provided by the transport, such as HTTP multi-part encoding.
This data may trick the application into overwriting a critical file or storing the file
in a bad location. You must validate the metadata extremely carefully before using it.

The other class of problem is with the file size or content.
An attacker can easily craft a valid image file with php code inside.


**Solution:**

Uploaded files always needs to be placed outside the document root of the web-server.

You should also check the user-input(filename) for having the right
allowed extensions such as .jpg, .png etc.

Note: when checking these extensions always make sure your application validates the last
possible extension so an attacker could not simply inject ".jpg.php" and bypass your
validation

After this validation you must also check the user-input(filename) for containing possible
path traversal patterns in order to prevent him from uploading outside of
the intended directory.

Most developers also do a mime-type check. This is a good protection however not
whenever you are checking this mime-type through the post request. This header can not be
trusted since it can be easily manipulated by an attacker.

The best way to check the mime-type
is to extract the file from the server after uploading and check it from the file itself.
Deleting it whenever it does not comply with expected values.

You may also want to check if the filenames do already exist before uploading in order to
prevent the overwriting of files.

Also for serving the files back there needs to be a file handler function that can select
the file based on an identifier that will serve the file back towards the user.
