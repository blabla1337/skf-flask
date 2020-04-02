# Anti-clickjacking

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
One way to defend against clickjacking is to include a `frame-breaker` script in each page that should not be framed. The following methodology will prevent a webpage from being framed even in legacy browsers, that do not support the `X-Frame-Options-Header`.

In the document `HEAD` element please add the following code:
1. Apply an ID to the style element itself:
```html
<style id="antiClickjack">
    body {
        display:none !important;
    }
</style>
```
2. And then delete that style by its ID immediately after in the script:
```html
 <script type="text/javascript">
    if(self === top) {
        const antiClickjack = document.getElementById("antiClickjack");
        antiClickjack.parentNode.removeChild(antiClickjack);
    } else {
        top.location = self.location;
    }
</script>
```

The second option is to use security headers. There are two options for setting the `anti-clickjacking` headers in your application:.

This will completely prevent your page from being displayed in an iframe:
```js
response.addHeader('X-Frame-Options', 'deny');
```

This will completely prevent your page from being displayed in an iframe on other sites:
```js
response.addHeader('X-Frame-Options', 'SAMEORIGIN');
```

Alternatively you can use [`helmet` module]( https://www.npmjs.com/package/helmet) which sets `X-FRAME` headers along with a host of other security headers.

If you only want `X-FRAME-OPTIONS` please use [`frameguard`](https://github.com/helmetjs/frameguard).
```js
const frameguard = require('frameguard');

// Don't allow me to be in ANY frames:
app.use(frameguard({ action: 'deny' }));

// Only let me be framed by people of the same origin:
app.use(frameguard({ action: 'sameorigin' }));
app.use(frameguard());  // defaults to sameorigin

// Allow from a specific host:
app.use(frameguard({
    action: 'allow-from',
    domain: 'http://example.com'
}));
```

## Considerations
TBA
