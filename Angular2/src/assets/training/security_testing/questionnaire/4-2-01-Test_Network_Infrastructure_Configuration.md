# Question

Decide if the given statmen is true or false.

"There is no need to review Administrative tools, since they require explicit privilege and usually only couple of people use the tools."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: All the elements of the infrastructure need to be reviewed in order to make sure that they don't contain any known vulnerabilities. It takes only a single vulnerability to undermine the security of the entire infrastructure. 


-----SPLIT-----


# Question

Which of the following steps needed to be taken to test configuration management infrastructure? Can choose multiple answers.

* ( ) The different elements that make up the infrastructure need to be determined in order to understand how they interact with a web application and how they affect its security.
* ( ) All the elements of the infrastructure need to be reviewed in order to make sure that they don't contain any known vulnerabilities.
* ( ) A review needs to be made of the administrative tools used to maintain all the different elements.
* ( ) The authentication systems, need to reviewed in order to assure that they serve the needs of the application and that they cannot be manipulated by external users to leverage access.
* ( ) A list of defined ports which are required for the application should be maintained and kept under change control.
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) The different elements that make up the infrastructure need to be determined in order to understand how they interact with a web application and how they affect its security.
* (x) All the elements of the infrastructure need to be reviewed in order to make sure that they don't contain any known vulnerabilities.
* (x) A review needs to be made of the administrative tools used to maintain all the different elements.
* (x) The authentication systems, need to reviewed in order to assure that they serve the needs of the application and that they cannot be manipulated by external users to leverage access.
* (x) A list of defined ports which are required for the application should be maintained and kept under change control.
* ( ) None of the above 

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"One of the objective of testing infrastructure configuration is validating used frameworks and systems are secure and not susceptible to known vulnerabilities due to unmaintained software or default settings and credentials."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Using server version to detect vulnerabilities provide reliable results."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: Some automated tools will flag vulnerabilities based on the web server version retrieved. This leads to both false positives and false negatives. On one hand, if the web server version has been removed or obscured by the local site administrator the scan tool will not flag the server as vulnerable even if it is. On the other hand, if the vendor providing the software does not update the web server version when vulnerabilities are fixed, the scan tool will flag vulnerabilities that do not exist.


