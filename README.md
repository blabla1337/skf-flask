#OWASP Security Knowledge Framework
[![SKF Logo](https://www.securityknowledgeframework.org/img/banner-wiki-owasp.jpg)](https://www.securityknowledgeframework.org/)
<br>Project status details:<br>
[![Build Travis CI Master](https://travis-ci.org/blabla1337/skf-flask.svg?branch=master)](https://travis-ci.org/blabla1337/skf-flask)
[![Coverage Status](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)
[![Code Quality Status](https://scrutinizer-ci.com/g/blabla1337/skf-flask/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/blabla1337/skf-flask/)

<br/>
Security Knowledge Framework is an expert system application that uses OWASP Application Security Verification Standard, code examples, helps developers in pre-development and post-development.  
 
##Table of Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Usage](#usage)
* [Development](#development)
* [Scrum Board](#scrum)
* [Testing](#testing)
* [License](#license)
* [Pebble OWASP-SKF](#pebble)
* [Contributors](#contributors)

##<a name="introduction"></a>Introduction

Our experience taught us that the current level of security the current web-applications contain is not sufficient enough to ensure security. This is mainly because web-developers simply aren't aware of the risks and dangers which are lurking, waiting to be exploited by hackers.

Because of this we decided to develop a proof of concept framework in order to create a guide system available for all developers so they can develop applications secure by design.

The security knowledge framework is here to support developers create secure applications. By analysing processing techniques in which the developers use to edit their data the application can link these techniques to different known vulnerabilities and give the developer feedback regarding descriptions and solutions on how to properly implement these techniques in a safe manner.

The second stage of the application is validating if the developer properly implemented different types of defence mechanisms by means of checklists with among others the OWASP Application security verification standards.

By means of the answers supplied by the developer the application again generates documentation in which it gives feedback on what defence mechanisms the developer forgot to implement and give him feedback regarding descriptions and solutions on how to properly implement these techniques in a safe manner.

##<a name="installing"></a>Installing

####Automated installation with Chef
----------

The easiest way to use the SKF project is using the Chef cookbook that we created.

What is Chef?

*Chef is a configuration management and automation platform from Opscode. Chef helps you describe your infrastructure with code. Because your infrastructure is managed with code, it can be automated, tested and reproduced with ease. Check out [https://www.chef.io](https://www.chef.io) for more information about Chef*  

For using the SKF chef cookbook you will need to install the 3 software products on your machine/laptop. Those are all free to use.

**VirtualBox**
* VirtualBox is a free to use Virtual Machine that can load images.
* [https://www.virtualbox.org/wiki/Downloads ](https://www.virtualbox.org/wiki/Downloads )

**Chef Development Kit**
* Chef Development Kit is a free to use tooling for testing and running cookbooks created with chef.
* [https://downloads.chef.io/chef-dk/](https://downloads.chef.io/chef-dk/)

**Vagrant**
* Vagrant is has pre-build images ready to use for stable and fast development
* [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html) 

When you have installed the above software you are now able to create a VirtualBox image with Vagrant configuration and using Chef to configure the SKF application. The SKF chef cookbook will do this all for you and you only need to follow the steps below on your machine/laptop.

````bash
cd ~/
wget https://github.com/blabla1337/owasp-skf-chef/archive/master.zip
unzip master.zip
cd owasp-skf-chef-master
kitchen converge default 
```

Now you have to wait a few minutes and watch the magic happen! ^^
When the Chef run has completed (-----> Kitchen is finished!) the application is ready to use. When you will start the VirtualBox GUI you can see the cookbook created a new VB image that is running and holding the SKF application.

The application will greet you on:
https://192.168.33.118

Below are some useful Kitchen 101 commands.
```bash
# All the below commands should be run in the SKF chef directory

# Command for creating the VM with the SKF project
kitchen converge default 

# Command for login to the VM with the SKF project
kitchen login default 

# Command for detroying the VM with the SKF project
kitchen destroy
```

#### AWS installation

A CloudFormation template is provided to make it easy to set up the
Security Knowledge Framework in AWS. For more information consult
[the README in the `cloudformation` directory](cloudformation/README.md).

####Ubuntu manual installation
----------
To run SKF you need Python pip and sqlite3 database support.
```bash
  On 64-bit platform:
  sudo apt-get install python-pip sqlite3 lib32z1-dev python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev
  
  On 32-bit platform:
  sudo apt-get install python-pip sqlite3 zlib1g-dev python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev
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

####Windows manual installation
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
####Mac OSX manual installation
----------
The first step is to install brew
```bash
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

After installing brew you can now install sqllite3
```bash
  brew install python-pip sqlite3
```

Now we install python pip
```bash
  sudo easy_install pip
```

After the prerequisites you can install the Python packages.
```bash
  sudo pip install https://github.com/mitsuhiko/flask/tarball/master
  sudo pip install owasp-skf
```

Now you can start the program by opening the folder (e.g. /opt/owasp-skf/) and run:
```bash
  sudo python skf.py
```

####Ubuntu Apache WSGI Setup (manual installation)
----------
To run the OWASP-SKF as a service (SaaS) you can hook it up to your existing webservers using the WSGI module.

First do the normal owasp-skf installation.
User that is installing this software is foobar, change foobar for your own user
```bash
  apt-get install git apache2 libapache2-mod-wsgi
  sudo a2enmod wsgi
  cd /home/foobar
  git clone https://github.com/blabla1337/skf-flask.git
```

Now disable SSL settings, we want Apache to do this

Edit the file file:
/home/foobar/skf-flask/skf/skf.py
```bash
  Change line:
       app.run(host=bindaddr, port=5443, ssl_context='adhoc')
  to:
       app.run(host=bindaddr, port=5443)
```

Now we can edit the configuration file of Apache

Edit the following file and add this below the virtualHost config for port 80
/etc/apache2/sites-enabled/000-default.conf
```bash
  WSGIRestrictStdout Off
  Listen 5443
  <VirtualHost *:5443>

    WSGIDaemonProcess skf user=www-data group=www-data threads=5
    WSGIScriptAlias / /home/foobar/skf-flask/skf/skf.wsgi

    <Directory /home/foobar/skf-flask/skf>
        WSGIProcessGroup skf
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
        Require all granted
    </Directory>

  </VirtualHost>
```

Now edit the configuration file of WSGI

Edit the following file:
/etc/apache2/mods-enabled/wsgi.conf
Add below inside the if_module of mod_wsgi:
```bash
  <FilesMatch ".+\.py$">
    SetHandler wsgi-script
  </FilesMatch>

  # Deny access to compiled binaries
  # You should not serve these to anyone
  <FilesMatch ".+\.py(c|o)$">
    Order Deny,Allow
    Deny from all
  </FilesMatch>
```
Create the WSGI file so it can be loaded by Apache

Create new skf.py file:
/home/foobar/skf-flask/skf/skf.wsgi
```bash
  import sys, os
  sys.path.insert (0,'/home/foobar/skf-flask/skf')
  os.chdir("/home/foobar/skf-flask/skf")
  from skf import app as application
```

The final step:
```bash
  chmod +x /home/foobar/skf-flask/skf/skf.py
  chown -R www-data:www-data /home/foobar/skf-flask
  sudo service apache2 restart
```

The application can be visited at port http://the_ip_/:5443
Also now you can apply your favourite Apache SSL/TLS settings.

##<a name="usage"></a>Usage

For more detailed information such as user guides and other documentation see:
<br/>
* [Readme: extended documentation](http://skf.readme.io/)  
<br/>

##<a name="development"></a>Development

1. Fork and clone https://github.com/blabla1337/skf-flask
2. pip install -r requirements.txt
3. cd skf && python ./skf.py
4. Create your changes commit and open a PR from your fork to the master repo

##<a name="scrum"></a>Scrum Board
####Waffle.io:
https://waffle.io/blabla1337/skf-flask

[![Throughput Graph](https://graphs.waffle.io/blabla1337/skf-flask/throughput.svg)](https://waffle.io/blabla1337/skf-flask/metrics) 

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

####uptimerobot.com:
------------
```
Monitor HTTP(s), Ping, Port and check Keywords. Get alerted via e-mail, SMS, Twitter, web-hooks or push. View uptime, downtime and response times.
```

####ssllabs.com & sslbadge.org:
------------
```
ssllabs.org:
Bringing you the best SSL/TLS and PKI testing tools and documentation.

sslbadge.org:
Creates a nice badge for your website SSL/TLS security settings based on the Qualys SSL Labs testing.
```
[![SSL Rating](http://sslbadge.org/?domain=securityknowledgeframework.org)](https://www.ssllabs.com/ssltest/analyze.html?d=securityknowledgeframework.org)

##<a name="license"></a>License
    Copyright (C) 2016  Glenn ten Cate, Riccardo ten Cate

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

##<a name="pebble"></a>Pebble OWASP-SKF
We have also created a Pebble application called: OWASP-SKF Pebble, check it out:
http://apps.getpebble.com/en_US/application/556b65b8389795176b000042

##<a name="contributors"></a>Contributors
- [Glenn ten Cate](https://twitter.com/FooBar_testing_)
- [Riccardo ten Cate](https://twitter.com/RiieCco)
- [Alexander Kaasjager](https://twitter.com/akaasjager)
- John Haley
- Daniel Paulus
- [Erik de Kuijper](https://twitter.com/edkpr)
- Roderick Schaefer
- [Jim Manico](https://twitter.com/manicode)
- Martijn Gijsberti Hodenpijl
- Bithin Alangot
- Martin Knobloch
- Adam Fisher
- Tom Wirschell
- Joerg Stephan
