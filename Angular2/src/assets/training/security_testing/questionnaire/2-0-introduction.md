# Question

Choose the *wrong* statement about the OWASP Testing Project ?

* ( ) The aim is to make a web application vulnerability checklist.
* ( ) The project provides a testing guide that can be used as a template to build their own testing programs or qualify other people's processes.
* ( ) The framework does not simply highlight areas of weakness, although that is certainly a by-product of many of the OWASP guides and checklists.

-----SPLIT-----

# Answer

* (x) The aim is to make a web application vulnerability checklist.
* ( ) The project provides a testing guide that can be used as a template to build their own testing programs or qualify other people's processes.
* ( ) The framework does not simply highlight areas of weakness, although that is certainly a by-product of many of the OWASP guides and checklists.


Explanation: The aim of the project is to help people understand the what, why, when, where, and how of testing web applications.


-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"The testing guide allows organizations to compare themselves against industry peers, to understand the magnitude of resources required to test and maintain software, or to prepare for an audit."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"The application should only be to tested when the deployment phase is completed in the Software Development Life Cycle (SDLC)."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* ( ) True
* (x) False

Explanation: SDLCs should include security tests to ensure security is adequately covered and controls are effective throughout the development process, not only once at the end of the deployment.

-----SPLIT-----

# Question

What are the actors to be tested in a software?

* ( ) People
* ( ) Process
* ( ) Technology
* ( ) All of the above

-----SPLIT-----

# Answer

* ( ) People
* ( ) Process
* ( ) Technology
* (x) All of the above

Explanation: An effective testing program should have components that test the following:
	People – to ensure that there is adequate education and awareness;
	Process – to ensure that there are adequate policies and standards and that people know how to follow these policies;
	Technology – to ensure that the process has been effective in its implementation.


-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"A prescriptive SDLC framework can provide a menu of potential security controls that can be applied within the SDLC."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

Explanation: A prescriptive advice shows how the secure SDLC should work, and descriptive advice shows how it is used in the real world. Both have their place. For example, if you don't know where to start, a prescriptive framework can provide a menu of potential security controls that can be applied within the SDLC.

-----SPLIT-----


# Question

Choose the answer(s) which is/are a descriptive secure SDLC framework.

* ( ) BSIMM
* ( ) OpenSAMM
* ( ) ISO/IEC 27034 

-----SPLIT-----

# Answer

* (x) BSIMM
* ( ) OpenSAMM
* ( ) ISO/IEC 27034 

-----SPLIT-----


# Question

Please select the approaches that can be applied while developing a threat model.  Select multiple choice if needed.

* ( ) Decomposing the application
* ( ) Defining and classifying the assets
* ( ) Exploring potential vulnerabilities
* ( ) Exploring potential threats
* ( ) Creating mitigation strategies
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) Decomposing the application
* (x) Defining and classifying the assets
* (x) Exploring potential vulnerabilities
* (x) Exploring potential threats
* (x) Creating mitigation strategies
* ( ) None of the above 

Explanation: The all given approches are recommended and they follows the NIST 800-30 standard for risk assessment.

-----SPLIT-----

# Question

Which of the following(s) is/are threat modelling methodology? Select multiple choice if needed.

* ( ) DREAD
* ( ) PASTA
* ( ) STRIDE
* ( ) CVSS
* ( ) CAPTCHA
* ( ) OCTAVE
* ( ) PnG
* ( ) hTMM
* ( ) None of the above 

-----SPLIT-----

# Answer

* (x) DREAD
* (x) PASTA
* (x) STRIDE
* (x) CVSS
* ( ) CAPTCHA
* (x) OCTAVE
* (x) PnG
* (x) hTMM
* ( ) None of the above 

Explanation: There are lots of threat modelling methodologies, such as DREAD, Process for Attack Simulation and Threat Analysis (PASTA), STRIDE, Common Vulnerability Scoring System (CVSS), Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE), LINDDUN, Attack trees, Persona non Grata (PnG), Hybrid Threat Modeling Method (hTMM). However, CAPTCHA ("Completely Automated Public Turing test to tell Computers and Humans Apart") is a test for determine whether user user is human, so it is irrelevent from the context.


-----SPLIT-----

# Question

Which of the following is *NOT* a disadvantage for source code reviews?

* ( ) Requires highly skilled security aware developers
* ( ) Can miss issues in compiled libraries
* ( ) Completeness and effectiveness
* ( ) Cannot detect runtime errors easily

-----SPLIT-----

# Answer

* ( ) Requires highly skilled security aware developers
* ( ) Can miss issues in compiled libraries
* (x) Completeness and effectiveness
* ( ) Cannot detect runtime errors easily

-----SPLIT-----

# Question

Which of the following statement is *false* for 'Funcional Security Requirements'.

* ( ) It can be derived from best practises, policies, regulations.
* ( ) Authentication and authorization can be categorized in 'Funcional Security Requirements'.
* ( ) Architectural requirements, like "robusteness" or "minimal performance and scalability" are also part of 'Funcional Security Requirements'
* ( ) All of the above 

-----SPLIT-----

# Answer

* ( ) It can be derived from best practises, policies, regulations.
* ( ) Authentication and authorization can be categorized in 'Funcional Security Requirements'.
* (x) Architectural requirements, like "robusteness" or "minimal performance and scalability" are also part of 'Funcional Security Requirements'
* ( ) All of the above 

Explanation: Architectural requirements, like "robusteness" or "minimal performance and scalability" are considered as 'Non-Functional Security Requirements'

-----SPLIT-----

# Question

What are the security controls that a generic security test suite might include? Can choose multiple answers.

* ( ) Identity, authentication & access control
* ( ) Input validation & encoding
* ( ) Encryption
* ( ) User and session management
* ( ) Error and exception handling
* ( ) Auditing and logging
* ( ) Encryption 

-----SPLIT-----

# Answer

* (x) Identity, authentication & access control
* (x) Input validation & encoding
* (x) Encryption
* (x) User and session management
* (x) Error and exception handling
* (x) Auditing and logging
* (x) Encryption 


-----SPLIT-----

# Question

What are the best practices to include when reporting a security test result? Can choose multiple answers.

* ( ) A categorization of each vulnerability by type
* ( ) The security threat that each issue is exposed to
* ( ) The root cause of each security issue, such as the bug or flaw
* ( ) Each testing technique used to find the issues
* ( ) The remediation, or countermeasure, for each vulnerability
* ( ) The severity rating of each vulnerability (e.g., high, medium, low, or CVSS score)

-----SPLIT-----

# Answer

* (x) A categorization of each vulnerability by type
* (x) The security threat that each issue is exposed to
* (x) The root cause of each security issue, such as the bug or flaw
* (x) Each testing technique used to find the issues
* (x) The remediation, or countermeasure, for each vulnerability
* (x) The severity rating of each vulnerability (e.g., high, medium, low, or CVSS score)

