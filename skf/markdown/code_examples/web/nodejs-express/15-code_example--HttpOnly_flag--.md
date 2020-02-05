# `httpOnly` flag

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
`httpOnly` flag can be added to the `Set-Cookie` response header in order to dissalow client-side scripts from accessing or modifying the cookie in question. This can help to mitigate most common XSS attacks by protecting the cookie data.

## Example
When setting sessions with [`express-session` module](https://www.npmjs.com/package/express-session) you can add the `cookie` portion of the configuration as shown below in order to protect session ID cookie:
```js
const session = require('express-session');

app.use(session({
  secret: 'some random and long value',
  key: 'sessionId',
  cookie: {
    httpOnly: true,
    secure: true
  }
}));
```

## Considerations
TBA
