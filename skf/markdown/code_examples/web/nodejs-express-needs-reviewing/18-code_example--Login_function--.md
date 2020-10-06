# Login Functionality 

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
Using the [Passport middleware](http://www.passportjs.org/)

The following example assumes username/password authentication.

First, configure the middleware:
```
 var auth_manager = require('passport')
  , LocalStrategy = require('passport-local').Strategy;

auth_manager.use(new LocalStrategy(
  function(username, password, done) {
    User.findOne({ username: username }, function(err, user) {
      if (err) { return done(err); }
      if (!user) {
        return done(null, false, { message: 'Incorrect username.' });
      }
      if (!user.validPassword(password)) {
        return done(null, false, { message: 'Incorrect password.' });
      }
      return done(null, user);
    });
  }
));
```

Then, register the route handling authentication can be:
```
app.post('/login',
  auth_manager.authenticate('local', { successRedirect: '/',
                                   failureRedirect: '/login'
				   })
);
```

## Considerations
TBA
