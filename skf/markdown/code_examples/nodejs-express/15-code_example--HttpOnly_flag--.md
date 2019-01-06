# HttpOnly flag
-------

## Example:


  //When setting sessions you can add the "cookie" part listed bellow. This will ensure cookie is sent only over HTTP(S) which will help to protect against cross-site scripting attacks.
  var session = require("express-session");
  app.use(session({
    secret: "some random and long value ",
    key: "sessionId",
    cookie: {
      httpOnly: true,
      secure: true
    }
  }));