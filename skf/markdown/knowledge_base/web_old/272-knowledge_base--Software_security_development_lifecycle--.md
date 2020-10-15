##Description:

In software engineering, a software development process is the process of dividing software development
work into distinct phases to improve design, product management, and project management. 
It is also known as a software development life cycle. The methodology may include the 
pre-definition of specific deliverables and artifacts that are created and completed by a 
project team to develop or maintain an application

In this software security development lifecycle we can also integrate security test automation and
other quality pilars for security.

##Mitigation:

The secure software development lifecycle ideally consists out of 5 different stages namely:

* Training and awareness
* Security requirements
* Test automation (unit testing, sonarqube, e2e testing, etc)
* Security test automation (SAST, DAST, IAST, RASP, ETC)
* Secure code review, penetration test

There are a lot of ways to achieve a good (S)SDLC, the most important thing to keep into
consideration is that you need to have a scalable solution that works over different CI
envorinments. Also keep in mind that your CI/CD pipeline is a production environment that
delivers production environments. So your CI/CD pipelines should be hardened as well as any other 
application.  Keep into consideration things like

- Monitoring on your pipeline
- Secret management
- Hardening of containers
- Hardening of your CI environment
- etc
