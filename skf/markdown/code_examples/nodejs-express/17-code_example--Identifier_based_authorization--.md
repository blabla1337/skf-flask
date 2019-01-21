# Identifier-based authorization

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
Based off this post on [Medium](https://medium.com/@evangow/server-authentication-basics-express-sessions-passport-and-curl-359b7456003d);

Database expected is MS SQL server making use of [mssql](https://www.npmjs.com/package/mssql).
`file_access` is formatted as so:
| user_id | file_id |
|---------|---------|
| 1       | 2       |
Where both ids are foreign keys and the primary key is made of a composite of the two.

## Example
```js
const express = require('express');
const session = require('express-session')
const FileStore = require('session-file-store')(session);
const bodyParser = require('body-parser');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const sql = require('mssql')

//Made up external files
const validator = require('./validator'); //Handles validating logins
const files = require('./files'); //Gets files from DB or store



// configure passport.js to use the local strategy
passport.use(new LocalStrategy(
	{ usernameField: 'email' }, (email, password, done) => {
		const user = validator.login(email, password); //Validator returns false if invalid
		return done(null, user)
	}
));

// tell passport how to serialize the user
passport.serializeUser((user, done) => {
  	done(null, user.id);
});

passport.deserializeUser((id, done) => {
	const user = users.getUserById(id);
  	done(null, user);
});

// create the server
const app = express();

// add & configure middleware
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(session({
  store: new FileStore(),
  secret: process.env.sessionKey, //always use environment variables to pass in keys.
  resave: false,
  saveUninitialized: true
}))
app.use(passport.initialize());
app.use(passport.session());

//Login excluded

app.get('/post',  passport.authenticate('local', { failureRedirect: '/login' }), //authenticates the user using session
   async function(req, res) {
	  	const data = req.body;
	  	let pool = await sql.connect(config)
		let result = await pool.request()
			.input('user_id', sql.Int, req.user.id) //sql.Int validates that only a integer value can be in the variable
			.input('file_id', sql.Int, data.id)
            .query('select * from file_access where user_id = @user_id and file_id = @file_id'); //variables inlined into sql query

		if(result.recordsets.length === 1) { //If the result exists the user has access
			res.send(files.getFile(data.id)) //sends file
		} else {
			res.redirect('/invalidFile'); //redirects to a generic invalid file
		}
  });
```

## Considerations
TBA
