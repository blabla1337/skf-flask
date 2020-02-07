# Logout Functionality

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General

## Example
Using [Passport](http://www.passportjs.org/docs/logout/) as a middleware call logOut() or logout() on your req object.
```
app.get('/logout', function(req, res){
  req.logout();
  res.redirect('/');
});

```

## Considerations
TBA
