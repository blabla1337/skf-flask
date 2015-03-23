
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

It depends on what the application does with the uploaded file and especially where it is stored.

There are really two classes of problems here. 
The first is with the file metadata, like the path and file name. 
These are generally provided by the transport, such as HTTP multi-part encoding. 
This data may trick the application into overwriting a critical file or storing the file 
in a bad location. You must validate the metadata extremely carefully before using it.

The other class of problem is with the file size or content. 
An attacker can easily craft a valid image file with php code inside. 


**Solution:**

Uploaded files always needs to be placed outside the document root of the web-server. 
Also for serving the files back there needs to be a file handler function that can select 
the file based on an identifier and the file will be served to the user.

	