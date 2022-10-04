# OWASP Security Knowledge Framework
[![SKF Logo](https://github.com/blabla1337/skf-www/blob/master/images/site-skf/logo_github.png?raw=true)](https://www.securityknowledgeframework.org/) 

<br>Project status details:<br>
[![Build Travis CI main](https://travis-ci.org/blabla1337/skf-flask.svg?branch=main)](https://travis-ci.org/blabla1337/skf-flask)
[![Join the chat at https://gitter.im/Security-Knowledge-Framework/Lobby](https://badges.gitter.im/Security-Knowledge-Framework/Lobby.svg)](https://gitter.im/Security-Knowledge-Framework/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Join the chat at https://owasp.slack.com/messages/C0F7L9X6V](https://img.shields.io/badge/chat-on%20slack-blueviolet)](https://owasp.slack.com/messages/C0F7L9X6V)
[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-orange.svg)](https://www.owasp.org/index.php/OWASP_Security_Knowledge_Framework)
[![OSSF Working group: Best Practices for Open Source Developers](https://img.shields.io/badge/openssf-Learning%20Platform%20Project-orange.svg)](https://openssf.org)

<br>Quality testing:<br>
[![Known Vulnerabilities](https://snyk.io/test/github/blabla1337/skf-flask/badge.svg)](https://snyk.io/test/github/blabla1337/skf-flask)
[![Coverage Status](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=main)](https://coveralls.io/repos/blabla1337/skf-flask/badge.svg?branch=main)
[![Requirements Status](https://requires.io/github/blabla1337/skf-flask/requirements.svg?branch=main)](https://requires.io/github/blabla1337/skf-flask/requirements/?branch=main)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/133/badge)](https://bestpractices.coreinfrastructure.org/projects/133)

The OWASP Security Knowledge Framework is an open source web application that explains secure coding principles in multiple programming languages. The goal of OWASP-SKF is to help you learn and integrate security by design in your software development and build applications that are secure by design. OWASP-SKF does this through manageable software development projects with checklists (using OWASP-ASVS/OWASP-MASVS  or custom security checklists) and labs to practice security verification (using SKF-Labs, OWASP Juice-shop, and best practice code examples from SKF and the OWASP-Cheatsheets).

Currently we are making plans to make SKF fully SaaS so that you don't need to perform your own installation to
be able to benifit fully from whatever the SKF has to offer you. We made this step because we realised that with all the
additional features we are providing SKF becomes harder and harder to deploy and maintain yourself.

Ofcourse, if you want to have your own instance running feel free to follow all the installation steps provided in either the 
[Kubernetes installation how to](installations/Kubernetes) or the [Docker-compose local how to](installations/docker).


## Table of Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Usage](#usage)
* [CI-Pipeline](#ci-pipeline)
* [Development / Contributing](CONTRIBUTING.md)
* [Scrum Board](#scrum-board)
* [License](#license)
* [Contributors](#contributors-main)

## <a name="introduction"></a>Introduction

Our experience taught us that the current level of security of web-applications is not sufficient enough to ensure security. This is mainly because web-developers simply aren't aware of the risks and dangers that are lurking, waiting to be exploited by hackers.

Because of this we decided to develop a framework in order to create a guide-system available for all developers so they can develop applications secure by design from the start.

[![SKF Features](https://raw.githubusercontent.com/blabla1337/skf-www/master/images/site-skf/skf_features.png)](https://www.securityknowledgeframework.org/) 

[![SKF Flow](https://raw.githubusercontent.com/blabla1337/skf-www/master/images/site-skf/skf_flow.gif)](https://www.securityknowledgeframework.org/) 

## <a name="installing"></a>Installing

### **Types of installation**

### [Kubernetes installation how to](installations/Kubernetes)

In order to make the SKF more ready to be used inside enterprise environments, we knew we had to do something with our
existing authentication/authorization model. We decided to change the SKF architecture and get rid of authentication/
authorization decisions within the API itself and delegate this to the API gateway and IDP. When choosing the full deployment of the SKF the user management can be done directly in Keycloak. You can also decide if you want to use Keycloak’s federation or social login features.


![full](https://user-images.githubusercontent.com/8506705/193818570-ff027ef1-acd1-461b-a9d1-53faac979a32.png)


---

### [Docker-compose local how to](installations/docker)

This deployment method is for testing and local development only. When deploying the SKF with the Docker
compose you are provisioned with the following environment:

![minimal](https://user-images.githubusercontent.com/8506705/193818616-d2ca5d02-aff5-48e7-bcb5-f4100742d0d4.png)

This setup makes the SKF directly accessible for everybody who wants to use it. Keep in mind that this also allows everybody to make changes to the SKF knowledgebase, code examples, questionnaires, etc. because after all, there are no authentication/authorization mechanisms in place remember?

---


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

### Requires.io pip packages:
```
Stay Up-to-date! Stay secure! Requires.io monitors your Python projects dependencies, and notify you whenever any of your dependency is out-of-date.
SKF Requires details:
```
https://requires.io/github/blabla1337/skf-flask/requirements/

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
    Copyright (C) 2022  Glenn ten Cate, Riccardo ten Cate

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

## <a name="contributors-main"></a>Main Contributors
- [Glenn ten Cate](https://twitter.com/FooBar_testing_)
- [Riccardo ten Cate](https://twitter.com/RiieCco)
- [Erik de Kuijper](https://twitter.com/edkpr)
- Martin Knobloch
- Rudy Truyens
- Thiago Luiz Dimbarre
- Volkan Dindar
- Bruno Cortes Rodrigues
- Sezer Toprak
- Jacob O'Toole (on behalf of MeVitae)
- Heeraj Nair
- [Priyanka Jain](https://www.linkedin.com/in/priyanka997/)
- Akash M
- [Ionut Marius Breaz](https://www.linkedin.com/in/ionut-breaz-52b847a2/)
- [Alexandru Stanciu](https://www.linkedin.com/in/alexandrustanciu)


## <a name="contributors"></a>Contributors
- [Imanuel Febie](https://github.com/tuffgniuz)
- Lucas Luitjes
- [Mattijs van Ommeren](https://twitter.com/alcyonsecurity)
- [Alexander Kaasjager](https://twitter.com/akaasjager)
- John Haley
- Daniel Paulus
- Roderick Schaefer
- [Jim Manico](https://twitter.com/manicode)
- Martijn Gijsberti Hodenpijl
- Bithin Alangot
- Adam Fisher
- Tom Wirschell
- Joerg Stephan
- Simon Brakhane
- Gerco Grandia
- [Ross Nanopoulos](https://www.linkedin.com/in/rnanopoulos/)
- Bob van den Heuvel
- Mariano Jose Abdala
- Ilguiz Latypov
- Laurence Keijmel
- Rick Mitchell (Kingthorin)
- Xenofon Vassilakopoulos
- Alpha Kitonga
- [Wojciech Reguła](https://www.linkedin.com/in/wojciech-regula/) 
- Amadeusz Starzykiewicz
- Adam Zima
- Kacper Madej
- Rafał Fronczyk
- Chang Xu (Neo)
- Martin Marsicano
- Chandrasekar Karthickrajan
- Leena Bhegade
- Balazs Hambalko
- Giulio Comi
- Aniket Surwade
- Harshant Sharma
- Semen Rozhkov
- Mehtab Zafar 
- Daniel Spilsbury
- Tess Sluijter
- Xavier Rene-Corail
- Luca Famà
