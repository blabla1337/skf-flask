# User registration SQL truncation prevention

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
In order to prevent Column truncation SQL injection we have to make sure that the applications structural logic does not mismatches with the database structural logic.

To achieve this imagine the follow example of a user model:

```
// models/user.js
// load the things we need
var database = require('my_favorite_database');


// define the schema for our user model
var userSchema = database.Schema({

    local            : {
        email        : String,
        password     : String,
        firstname    : String,
        lastname     : String,
    }
});
```

Then we need to define some methods to hash passwords and check password validity

```
var bcrypt   = require('bcrypt-nodejs');
// to hash
userSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// to validate
userSchema.methods.validPassword = function(password) {
    return bcrypt.compareSync(password, this.local.password);
};

// create the model for users and expose it to our app
module.exports = database.model('User', userSchema);

```
Then you can config the [Passport](http://www.passportjs.org/) middleware to handle your local authentication strategy

```
// authentication.js

// load all the things we need
var LocalStrategy   = require('passport-local').Strategy;

// load up the user model
var User = require('models/user');

// expose this function to our app using module.exports
module.exports = function(passport) {

    // passport needs ability to serialize and unserialize users out of session

    // used to serialize the user for the session
    passport.serializeUser(function(user, done) {
        done(null, user.id);
    });

    // used to deserialize the user
    passport.deserializeUser(function(id, done) {
        User.findById(id, function(err, user) {
            done(err, user);
        });
    });
    
    passport.use('local-signup', new LocalStrategy({
        usernameField : 'email',
        passwordField : 'password',
        passReqToCallback : true
    },
    function(req, email, password, firstname, lastname done) {
        process.nextTick(function() {
            User.findOne({ 'local.email' :  email }, function(err, user) {
                if (err)
                  return done(err);
      
                if (user) {
                    return done(null, false, req.flash('signupMessage', 'User exists'));
                } else {
                    var user             = new User();
                    user.local.email     = email;
                    user.local.password  = user.generateHash(password);
                    user.local.firstname = firstname;
                    user.local.lastname  = lastname

                // save the user
                newUser.save(function(err) {
                    if (err)
                        throw err;
                    return done(null, user);
                });
            }

        });    

        });

    }));

};

```

Then in the app routes

```
 // signup form processing
    app.post('/register', passport.authenticate('local-signup', {
        successRedirect : '/profile', // redirect to the secure profile section
        failureRedirect : '/register', // redirect back to the signup page if there is an error
        failureFlash : true // allow flash messages
    }));


```


## Considerations
TBA
