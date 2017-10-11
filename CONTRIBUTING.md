# OWASP Security Knowledge Framework
[![SKF Logo](https://www.securityknowledgeframework.org/img/banner-wiki-owasp.jpg)](https://www.securityknowledgeframework.org/)

## Table of Contents
* [Development-API](#development-api)
* [Development-Angular](#development-angular)
* [Testing](#testing)

Wow you landed on the contribution page how awesome you must be to help out and add value to his project! We thank you very much for this and we really appricate your help. We will reward contributors with recongnision on the contributors list of SKF and for people who add new feutures or fix / report security issues we will give you a free OWASP-SKF t-shirt! If you are really bad ass and you add major improvements then you will receive a hoodie of OWASP-SKF with your name on it!

Below are the 2 different parts of SKF and how you can contribute to it, please always make sure that the quality we try to achieve remains intact. Also when you have questions or want to discuss your implementation / contribution please locate us on Gitter.im chat: [![Join the chat at https://gitter.im/Security-Knowledge-Framework/Lobby](https://badges.gitter.im/Security-Knowledge-Framework/Lobby.svg)](https://gitter.im/Security-Knowledge-Framework/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Again thank you for your help, you rock!

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