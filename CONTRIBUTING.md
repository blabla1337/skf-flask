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
2. pip3.6 install -r requirements.txt
3. export FLASK_APP=skf/app.py
4. export PYTHONPATH=.:$PYTHONPATH
5. export FLASK_DEBUG=1
6. python3.6 skf/app.py
7. Run the manual test first to verify if everything is good
``` 
coverage run tests/run.py test
``` 
7. Create your changes and write a unit test, commit and open a PR from your fork to the master repo. All CI test must pass before we accept pull requests.

## <a name="development-angular"></a>Development SKF-ANGULAR

1. Fork and clone https://github.com/blabla1337/skf-flask
2. cd Angular
3. npm install
4. ng serve --host=0.0.0.0 
4. OR edit the package.json in Angular folder and remove --env=prod example: "start": "ng serve --host=0.0.0.0"
5. npm start
6. Run the manual test in the Angular dir first to verify if everything is good
``` 
npm test
``` 
7. Create your changes and write a unit test, commit and open a PR from your fork to the master repo. All CI test must pass before we accept pull requests.


## <a name="testing"></a>Testing

TESTING SKF-API<br>
Go to the SKF root dir and run:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
export FLASK_DEBUG=1
coverage run tests/run.py test
```

TESTING SKF-ANGULAR<br>
Go to the Angular dir in the SKF root dir and run:
```
npm test
```

END 2 END TESTING SELENIUM<br>

Testing SKF App End to End with Selenium<br>
We need to start the SKF API first<br>
Go to the SKF root dir and run:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
export FLASK_DEBUG=1
python3 skf/app.py
```

Now we need to start the SKF Angular<br>
Go to the Angular dir in the SKF root dir and run:
```
npm start
```

First we need to download the ChromeDriver for our OS<br>
Always pick the last version available:<br>
http://chromedriver.chromium.org/downloads<br>
Then download your OS driver:<br>
https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/<br>
Unzip it and place it in a good location<br>
Now add it to the Path (Windows):<br>
```
set PATH=%PATH%;C:\WHERE_I_PUT_THEDRIVER
```
Or for Mac/Linux add it to the Path:<br>
```
export PATH=$PATH:/usr/local/bin/WHERE_I_PUT_THEDRIVER
```
Go to the SKF root dir and run:
```
export FLASK_APP=skf/app.py
export PYTHONPATH=.:$PYTHONPATH
export FLASK_DEBUG=1
python3 tests/selenium/run.py
```
