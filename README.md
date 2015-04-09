About Security Knowledge Framework
------------------------------------
Our experience taught us that the current level of security the current 
web-applications contain is not sufficient enough to ensure security. 
This is mainly because web-developers simpy aren't aware of the risks and dangers 
which are lurking, waiting to be exploited by hackers. 

Because of this we decided to develop a proof of concept framework in order 
to create a guide system available for all developers so they can develop 
applications secure by design.

The security knowledge framework is here to support developers create secure applications. 
By analysing proccessing techniques in which the developers use to edit their 
data the application can link these techniques to different known vulnerabilities and 
give the developer feedback regarding descriptions and solutions on how to properly 
implement these techniques in a safe manner. 

The seccond stage of the application is validating if the developer 
properly implemented different types of defense mechanisms 
by means of checklistswith among others the 
OWASP Application security verification standards.

By means of the answers supplied by the developer the application again generates
documentation in which it gives feedback on what defense 
mechanisms the developer forgot to implement and give him feedback 
regarding descriptions and solutions on how to properly implement
these techniques in a safe manner.

Installing Ubuntu
----------
sudo apt-get install python-pip <br>
sudo apt-get install sqlite3 <br>

pip install owasp-skf <br>
pip install https://github.com/mitsuhiko/flask/tarball/master <br>

Now you can start the program by opening the folder (e.g. /opt/owasp-skf/) and run:
python skf.py

Installing Windows
----------
Download and install Python2.7.9<br>
https://www.python.org/downloads/release/python-279/

Run below commands in cmd:<br>
C:\Python27\Scripts\pip.exe install owasp-skf<br>
C:\Python27\Scripts\pip.exe install https://github.com/mitsuhiko/flask/tarball/master

Now you can start the program by opening the folder and run the skf.py file:<br>
cd C:\Python27\Lib\site-packages\skf<br>
C:\Python27\python.exe skf.py<br>

1. The SKF web-application:
     
     The application will greet you on
     https://127.0.0.1:5443/

     Default the application will generate a certificate on the fly but what you 
     really want to do is placing your own server.key and server.crt in the skf dir. 
     Then the skf-flask application will use these instead.

     default username: admin
     The password will be auto-generated every time the skf-application is launched. 
     Check commandline output for the the generated password.
	 
3. If you want to use test_skf.py as well, you will need to<br>
     Ubuntu:<br>
     pip install pytest<br>
     Windows:<br>
     C:\Python27\Scripts\pip.exe --install pytest
     
