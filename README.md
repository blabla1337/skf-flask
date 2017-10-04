# OWASP Security Knowledge Framework
[![SKF Logo](https://www.securityknowledgeframework.org/img/banner-wiki-owasp.jpg)](https://www.securityknowledgeframework.org/)

<br>Project status details:<br>
[![Build Travis CI Master](https://travis-ci.org/blabla1337/skf-flask.svg?branch=master)](https://travis-ci.org/blabla1337/skf-flask)
[![Join the chat at https://gitter.im/Security-Knowledge-Framework/Lobby](https://badges.gitter.im/Security-Knowledge-Framework/Lobby.svg)](https://gitter.im/Security-Knowledge-Framework/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


<br>Quality testing SKF-Angular:<br>
[![codecov](https://codecov.io/gh/blabla1337/skf-flask/branch/master/graph/badge.svg)](https://codecov.io/gh/blabla1337/skf-flask)
[![bitHound Overall Score](https://www.bithound.io/github/blabla1337/skf-flask/badges/score.svg)](https://www.bithound.io/github/blabla1337/skf-flask)
[![bitHound Code](https://www.bithound.io/github/blabla1337/skf-flask/badges/code.svg)](https://www.bithound.io/github/blabla1337/skf-flask)
[![bitHound Dependencies](https://www.bithound.io/github/blabla1337/skf-flask/badges/dependencies.svg)](https://www.bithound.io/github/blabla1337/skf-flask/master/dependencies/npm)

<br>Quality testing SKF-API:<br>
[![Coverage Status](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)
[![Black Duck Security Risk](https://copilot.blackducksoftware.com/github/groups/blabla1337/locations/skf-flask/public/results/branches/master/badge-risk.svg)](https://copilot.blackducksoftware.com/github/groups/blabla1337/locations/skf-flask/public/results/branches/master)
[![Code Quality Status](https://scrutinizer-ci.com/g/blabla1337/skf-flask/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/blabla1337/skf-flask/)
[![Requirements Status](https://requires.io/github/blabla1337/skf-flask/requirements.svg?branch=master)](https://requires.io/github/blabla1337/skf-flask/requirements/?branch=master)

Security Knowledge Framework is an expert system application that uses the OWASP Application Security Verification Standard with detailed code examples (secure coding principles) to help developers in pre-development and post-development phases and create applications that are secure by design.

## Table of Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Usage](#usage)
* [CI-Pipeline](#ci-pipeline)
* [Development-API](#development-api)
* [Development-Angular](#development-angular)
* [Testing](#testing)
* [Scrum Board](#scrum-board)
* [License](#license)
* [Contributors](#contributors)

## <a name="introduction"></a>Introduction

Our experience taught us that the current level of security of web-applications is not sufficient enough to ensure security. This is mainly because web-developers simply aren't aware of the risks and dangers that are lurking, waiting to be exploited by hackers.

Because of this we decided to develop a framework in order to create a guide-system available for all developers so they can develop applications secure by design from the start.

The OWASP Security Knowledge Framework is here to support developers create secure applications. By using the [OWASP Application Security Verification Standards.](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project) as a security requirement and give the developer feedback regarding descriptions and solutions on how to properly implement these security controls in a safe manner.

The second stage is validating if the developer properly implemented different security controls and the belonging defence mechanisms by means of checklists created with the [OWASP Application Security Verification Standards.](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project) By means of the answers supplied by the developer the application again generates documentation in which it gives feedback on what defence mechanisms the developer forgot to implement and give him feedback regarding descriptions and solutions on how to properly implement these techniques in a safe manner.

## <a name="installing"></a>Installing

### Docker

The fastest way to start using the SKF project is using the pre-built container hosted at Docker hub. This container always has the very latest version from the master repository. Change the JWT_SECRET value to a new random secret string before starting the docker image.

First run the docker pull command to get the latest image
```
docker pull blabla1337/skf-flask
```
Then start the docker image 
```
docker run -e "ORIGIN=localhost" -e "JWT_SECRET=change_this_super_secret_random_string" -ti -p 127.0.0.1:443:443 blabla1337/skf-flask
```

The application will greet you on:
https://localhost

## <a name="usage"></a>Usage

For more detailed information such as setting up an admin account and user guides please see the extended documentation that can be found below:

[Readme: extended documentation](https://skf.readme.io/)  

## <a name="development-api"></a>Development SKF-API

1. Fork and clone https://github.com/blabla1337/skf-flask
2. pip install -r requirements.txt
3. export FLASK_APP=skf/app.py
4. export PYTHONPATH=.:$PYTHONPATH
5. python3.6 skf/app.py
6. Run the manual test first to verify if everything is good
``` 
coverage run tests/run.py test
``` 
7. Create your changes and write a unit test, commit and open a PR from your fork to the master repo. All CI test must pass before we accept pull requests.

## <a name="development-angular"></a>Development SKF-ANGULAR

1. Fork and clone https://github.com/blabla1337/skf-flask
2. cd Angular
3. npm install
4. ng serve --host=0.0.0.0 
5. Run the manual test in the Angular dir first to verify if everything is good
``` 
npm test
``` 
6. Create your changes and write a unit test, commit and open a PR from your fork to the master repo. All CI test must pass before we accept pull requests.


## <a name="scrum-board"></a>Scrum Board

### Waffle.io:

https://waffle.io/blabla1337/skf-flask

[![Throughput Graph](https://graphs.waffle.io/blabla1337/skf-flask/throughput.svg)](https://waffle.io/blabla1337/skf-flask/metrics)

## <a name="CI-Pipeline"></a>CI-Pipeline

### Travis-ci.org:
```
Test and Deploy with Confidence. Easily sync your GitHub projects with Travis CI and you'll be testing your code in minutes!
SKF Build details:
```
https://travis-ci.org/blabla1337/skf-flask

### Coveralls.io Python:
```
DELIVER BETTER CODE. We help developers deliver code confidently by showing which parts of your code aren't covered by your test suite.
SKF Coveralls details:
```
https://coveralls.io/r/blabla1337/skf-flask

### codecov.io for Angular:
```
Code coverage done right. Highly integrated with GitHub, Bitbucket and GitLab.
SKF codecov details:
```
https://codecov.io/gh/blabla1337/skf-flask

### Scrutinizer-ci.com:
```
Why to use Scrutinizer. Improve code quality and find bugs before they hit production with our continuous inspection platform. Improve Code Quality.
SKF Scrutinizer details:
```
https://scrutinizer-ci.com/g/blabla1337/skf-flask/

### Bithound.io NPM packages:
```
BitHound provides your Node team with comprehensive and prioritized issues in your code and npm packages.
SKF Bithound details:
```
https://www.bithound.io/github/blabla1337/skf-flask

### Requires.io pip packages:
```
Stay Up-to-date! Stay secure! Requires.io monitors your Python projects dependencies, and notify you whenever any of your dependency is out-of-date.
SKF Requires details:
```
https://requires.io/github/blabla1337/skf-flask/requirements/

### Black Duck Security Risk:
```
Announcing Black Duck CoPilot, a new service helping open source project teams catalog and report on their project's dependencies.
SKF Requires details:
```
https://copilot.blackducksoftware.com/github/groups/blabla1337/locations/skf-flask/public/results

### uptimerobot.com:
```
Monitor HTTP(s), Ping, Port and check Keywords. Get alerted via e-mail, SMS, Twitter, web-hooks or push. View uptime, downtime and response times.
```

### ssllabs.com & sslbadge.org:
```
ssllabs.org:
Bringing you the best SSL/TLS and PKI testing tools and documentation.

sslbadge.org:
Creates a nice badge for your website SSL/TLS security settings based on the Qualys SSL Labs testing.
```
[![SSL Rating](http://sslbadge.org/?domain=securityknowledgeframework.org)](https://www.ssllabs.com/ssltest/analyze.html?d=securityknowledgeframework.org)

## <a name="testing"></a>Testing

TESTING SKF-API<br>
Go to the SKF root dir and run:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
coverage run tests/run.py test
```

TESTING SKF-ANGULAR<br>
Go to the Angular dir in the SKF root dir and run:
```
npm test
```

## <a name="license"></a>License
    Copyright (C) 2017  Glenn ten Cate, Riccardo ten Cate

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

### OWASP:

* [Owasp](http://owasp.com/index.php/Main_Page)  
Licensed under the [creative commons](http://creativecommons.org/licenses/by-nd/3.0/nl/) license

## <a name="contributors"></a>Contributors

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
- Simon Brakhane
- Gerco Grandia
- [Ross Nanopoulos](https://twitter.com/rossnanop)
- Bob van den Heuvel
- Mariano Jose Abdala
- Ilguiz Latypov
- Laurence Keijmel
- Rick Mitchell (Kingthorin)
- Xenofon Vassilakopoulos
- Heeraj Nair
- Alpha Kitonga

