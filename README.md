# OWASP Security Knowledge Framework
[![SKF Logo](https://github.com/blabla1337/skf-www/blob/master/images/site-skf/logo_github.png?raw=true)](https://www.securityknowledgeframework.org/) 

<br>Project status details:<br>
[![Build Travis CI Master](https://travis-ci.org/blabla1337/skf-flask.svg?branch=master)](https://travis-ci.org/blabla1337/skf-flask)
[![Join the chat at https://gitter.im/Security-Knowledge-Framework/Lobby](https://badges.gitter.im/Security-Knowledge-Framework/Lobby.svg)](https://gitter.im/Security-Knowledge-Framework/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Join the chat at https://owasp.slack.com/messages/C0F7L9X6V](https://img.shields.io/badge/chat-on%20slack-blueviolet)](https://owasp.slack.com/messages/C0F7L9X6V)
[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-orange.svg)](https://www.owasp.org/index.php/OWASP_Security_Knowledge_Framework)
[![OSSF Working group: Best Practices for Open Source Developers](https://img.shields.io/badge/openssf-Learning%20Platform%20Project-orange.svg)](https://openssf.org)

<br>Quality testing:<br>
[![Known Vulnerabilities](https://snyk.io/test/github/blabla1337/skf-flask/badge.svg)](https://snyk.io/test/github/blabla1337/skf-flask)
[![Coverage Status](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=master)
[![Black Duck Security Risk](https://copilot.blackducksoftware.com/github/repos/blabla1337/skf-flask/branches/master/badge-risk.svg)](https://copilot.blackducksoftware.com/github/repos/blabla1337/skf-flask/branches/master)
[![Requirements Status](https://requires.io/github/blabla1337/skf-flask/requirements.svg?branch=master)](https://requires.io/github/blabla1337/skf-flask/requirements/?branch=master)

The OWASP Security Knowledge Framework is an open source web application that explains secure coding principles in multiple programming languages. The goal of OWASP-SKF is to help you learn and integrate security by design in your software development and build applications that are secure by design. OWASP-SKF does this through manageable software development projects with checklists (using OWASP-ASVS/OWASP-MASVS  or custom security checklists) and labs to practice security verification (using SKF-Labs, OWASP Juice-shop, and best practice code examples from SKF and the OWASP-Cheatsheets).

## Table of Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Updating Database](#updating-db)
* [Updating Chatbot](#updating-dataset)
* [Usage](#usage)
* [CI-Pipeline](#ci-pipeline)
* [Development / Contributing](https://github.com/blabla1337/skf-flask/blob/master/CONTRIBUTING.md)
* [Scrum Board](#scrum-board)
* [License](#license)
* [Contributors](#contributors)

## <a name="introduction"></a>Introduction

Our experience taught us that the current level of security of web-applications is not sufficient enough to ensure security. This is mainly because web-developers simply aren't aware of the risks and dangers that are lurking, waiting to be exploited by hackers.

Because of this we decided to develop a framework in order to create a guide-system available for all developers so they can develop applications secure by design from the start.

[![SKF Features](https://raw.githubusercontent.com/blabla1337/skf-www/master/images/site-skf/skf_features.png)](https://www.securityknowledgeframework.org/) 

[![SKF Flow](https://raw.githubusercontent.com/blabla1337/skf-www/master/images/site-skf/skf_flow.gif)](https://www.securityknowledgeframework.org/) 

## <a name="installing"></a>Installing

### [Kubernetes installation how to](https://github.com/blabla1337/skf-flask/tree/master/installations/Kubernetes)  
### [Bare metal / on premise installation how to](https://github.com/blabla1337/skf-flask/tree/master/installations/local)  
### [Docker-compose local how to](https://github.com/blabla1337/skf-flask/tree/master/installations/docker)  
### [SKF K8s Raspberry pi cluster how to](https://github.com/blabla1337/skf-flask/tree/master/installations/pi-cluster)  
### [SKF Chatbot installation how to](https://github.com/blabla1337/skf-bot)  

## <a name="updating-db"></a>Updating Database

There is a method available to update the content of the SKF application.

When you have modified or created new Knowledge base items, code examples or checklist you need to run the following commands in the SKF root directory:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
flask updatedb
```

## <a name="updating-dataset"></a>Updating chatbot

There is a method available to update the dataset of the SKF chatbot application.

When you have modified or created new Knowledge base items, code examples or checklist you need to run the following commands in the SKF root directory:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
flask initdataset
```

## <a name="usage"></a>Usage

For more detailed information such as setting up an admin account and user guides please see the extended documentation that can be found below:

[Readme: extended documentation](https://skf.readme.io/)  

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


## <a name="license"></a>License
    Copyright (C) 2021  Glenn ten Cate, Riccardo ten Cate

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
- Lucas Luitjes
- [Mattijs van Ommeren](https://twitter.com/alcyonsecurity)
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
- [Wojciech Reguła](https://www.linkedin.com/in/wojciech-regula/) 
- Amadeusz Starzykiewicz
- Adam Zima
- Kacper Madej
- Rafał Fronczyk
- Chang Xu (Neo)
- Martin Marsicano
- [Priyanka Jain](https://www.linkedin.com/in/priyanka997/)
- Chandrasekar Karthickrajan
- Leena Bhegade
- Balazs Hambalko
- Rudy Truyens
- Giulio Comi
- Aniket Surwade
- Thiago Luiz Dimbarre
- Harshant Sharma
- Semen Rozhkov
- Mehtab Zafar 
- Daniel Spilsbury
- Akash M
- Tess Sluijter
- Xavier Rene-Corail
