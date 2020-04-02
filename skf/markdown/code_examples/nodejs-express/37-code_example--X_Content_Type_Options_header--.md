# `X-Content-Type-Options` header

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
In order to set the `X-Content-Type-Options` header you'll have to add the following code to the head of your application:
```js
res.set('X-Content-Type-Options', 'nosniff');
```

Alternatively you can use [`dont-sniff-mimetype` module](https://www.npmjs.com/package/dont-sniff-mimetype):
```js
const nosniff = require('dont-sniff-mimetype');

app.use(nosniff());
```

The same can be achieved by using [`helmet` module]( https://www.npmjs.com/package/helmet) which sets X-FRAME headers along with a host of other security headers.

## Considerations
TBA
