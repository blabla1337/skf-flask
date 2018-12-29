# HttpOnly flag
-------

## Example:


  //when setting sessions you can add the "cookie" part listed bellow
  var session = require("express-session");
  app.use(session({
    secret: "some random and long value ",
    key: "sessionId",
    cookie: {
      httpOnly: true,
      secure: true
    }
  }));