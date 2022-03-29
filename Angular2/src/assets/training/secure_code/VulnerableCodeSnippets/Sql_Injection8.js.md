# Question
 
What is the problem here?
 
```
var express = require('express')

var app = express()
const Sequelize = require('sequelize');

const sequelize = new Sequelize('localhost', 'root', 'secPass1907', {
  dialect: 'sqlite',
  storage: 'data/database.sqlite'
});

app.post('/users', function (req, res) {
    sequelize.query('SELECT * FROM users WHERE username = ' +  req.body.username);
  })
```
 
-----SPLIT-----
 
# Answer

It is an SQL Injection issue. 'username' parameter is vulnerable part. The code retrieves the data from the request, however there is no any input control exists and the code concatenates words for query building. No SQL parameterization.
