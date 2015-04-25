[![SKF Logo](http://www.securityknowledgeframework.com/img/logos/logo-purple.png)](http://www.securityknowledgeframework.com)
<br>Project status details:<br>
[![Build Travis CI](https://travis-ci.org/blabla1337/skf-flask.svg)](https://travis-ci.org/blabla1337/skf-flask)
[![Coverage Status](https://img.shields.io/coveralls/blabla1337/skf-flask/master.svg)](https://coveralls.io/r/blabla1337/skf-flask)
[![Code Quality Status](https://scrutinizer-ci.com/g/blabla1337/skf-flask/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/blabla1337/skf-flask/)
[![Pypip DL Status](https://pypip.in/d/owasp-skf/badge.png)](https://pypi.python.org/pypi/owasp-skf)
[![Pypip Version](https://pypip.in/v/owasp-skf/badge.png)](https://pypi.python.org/pypi/owasp-skf)


#OWASP Security Knowledge Framework
Security Knowledge Framework is an expert system application that uses OWASP Application Security Verification Standard, code examples, helps developers in pre-development and post-development.

##Table of Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Usage](#usage)
* [Scrum Board](#scrum)
* [Testing](#testing)
* [License](#license)
* [Contributors](#contributors)

##<a name="introduction"></a>Introduction
Our experience taught us that the current level of security the current web-applications contain is not sufficient enough to ensure security. This is mainly because web-developers simply aren't aware of the risks and dangers which are lurking, waiting to be exploited by hackers.

Because of this we decided to develop a proof of concept framework in order to create a guide system available for all developers so they can develop applications secure by design.

The security knowledge framework is here to support developers create secure applications. By analysing processing techniques in which the developers use to edit their data the application can link these techniques to different known vulnerabilities and give the developer feedback regarding descriptions and solutions on how to properly implement these techniques in a safe manner.

The second stage of the application is validating if the developer properly implemented different types of defence mechanisms by means of checklists with among others the OWASP Application security verification standards.

By means of the answers supplied by the developer the application again generates documentation in which it gives feedback on what defence mechanisms the developer forgot to implement and give him feedback regarding descriptions and solutions on how to properly implement these techniques in a safe manner.

##<a name="installing"></a>Installing

####Ubuntu
----------
To run SKF you need Python pip and sqlite3 database support.
```bash
  sudo apt-get install python-pip sqlite3
```

After the prerequisites you can install the Python packages.
```bash
  sudo pip install https://github.com/mitsuhiko/flask/tarball/master
  sudo pip install owasp-skf
```

Now you can start the program by opening the folder (e.g. /opt/owasp-skf/) and run:
```bash
  python skf.py
```

####Windows
-----------
Download and install [Python 2.7.9](https://www.python.org/downloads/release/python-279/)

Run below commands in cmd (As Administrator):
```
  C:\Python27\Scripts\pip.exe install https://github.com/mitsuhiko/flask/tarball/master
  C:\Python27\Scripts\pip.exe install owasp-skf
```

Now you can start the program by opening the folder and run the skf.py file:
```
  cd C:\Python27\Lib\site-packages\skf
  C:\Python27\python.exe skf.py
```

##<a name="usage"></a>Usage

The application will greet you on `https://127.0.0.1:5443/`

Default the application will generate a certificate on the fly but what you really want to do is placing your own server.key and server.crt in the skf dir. Then the skf-flask application will use these instead.

Default username: `admin`
The password will be auto-generated every time the skf-application is launched. Check commandline output for the generated password.

##<a name="scrum"></a>Scrum Board
####Waffle.io:
https://waffle.io/blabla1337/skf-flask

##<a name="testing"></a>Testing
####Travis-ci.org:
-----------
```
Test and Deploy with Confidence. Easily sync your GitHub projects with Travis CI and you'll be testing your code in minutes!
SKF Build details:
```
https://travis-ci.org/blabla1337/skf-flask

####Coveralls.io:
------------
```
DELIVER BETTER CODE. We help developers deliver code confidently by showing which parts of your code aren't covered by your test suite.
SKF Coveralls details:
```
https://coveralls.io/r/blabla1337/skf-flask

####Scrutinizer-ci.com:
------------
```
Why to use Scrutinizer. Improve code quality and find bugs before they hit production with our continuous inspection platform. Improve Code Quality.
SKF Scrutinizer details:
```
https://scrutinizer-ci.com/g/blabla1337/skf-flask/

##<a name="license"></a>License
    Copyright (C) 2015  Glenn ten Cate, Riccardo ten Cate

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

####SKF includes the following software:
----------------------------------------

* [Owasp](http://owasp.com/index.php/Main_Page)  
Licensed under the [creative commons](http://creativecommons.org/licenses/by-nd/3.0/nl/) license

* [Python-Flask](http://flask.pocoo.org/)  
Licensed under the [BSD license](http://flask.pocoo.org/docs/0.10/license/) license

* [jQuery](http://jquery.org)  
Licensed under the [MIT license](http://jquery.org/license)

* [Certified secure](https://www.certifiedsecure.com/frontpage)  
Licensed under the [creative commons](http://creativecommons.org/licenses/by-nd/3.0/nl/) license

* [Flask](https://github.com/mitsuhiko/flask/)  
Copyright (c) 2015 by Armin Ronacher and contributors, Some rights reserved.

* [Markdown](https://pypi.python.org/pypi/Markdown)  
Licensed under the [BSD](http://www.linfo.org/bsdlicense.html) license

* [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4/4.3.2)  
Licensed under the [MIT](http://en.wikipedia.org/wiki/MIT_License) license

* [Python-docx](https://pypi.python.org/pypi/pyOpenSSL)  
Licensed under the [MIT](http://en.wikipedia.org/wiki/MIT_License) license

* [pyOpenSSL](https://pypi.python.org/pypi/python-docx)  
Licensed under the [APL2](https://www.apache.org/licenses/LICENSE-2.0) license

* Boostrap theme thanks to http://www.blacktie.com

##<a name="contributors"></a>Contributors
- Glenn ten Cate
- Riccardo ten Cate
- Alexander Kaasjager
- John Haley
- Daniel Paulus <d.paulus@gmail.com>
- Erik de Kuijper
