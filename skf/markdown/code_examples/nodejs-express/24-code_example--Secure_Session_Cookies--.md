# Secure flag for session cookies

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
In [`express-session` module](https://www.npmjs.com/package/express-session) it is possible to supply `secure` flag as a part of `cookie` configuration.

This flag instructs the browser to never send cookies over an `HTTP` request. The cookie will only be sent over `HTTPS` even if the user manually types in a request for `HTTP`. The HTTP request itself will be sent, but the browser will not send any cookies.

## Example
A session with secured cookies can be created in the following way:
```js
app.use(session({
    name: 'session',
    keys: ['key1', 'key2'],
    cokkie: {
        secure: true
        httpOnly: true,
        domain: 'complete.subdomain.example.com',
        path: 'foo/bar',
        expires: expiryDate
    } 
}));
```

## Considerations
The `HTTP` request is still sent and thus could be manipulated by a man in the middle to perform convincing phishing attacks (please see Strict Transport Security for a recommended solution).

Setting the `domain` attribute to a too permissive value, such as `example.com`, allows an attacker to launch attacks on the session IDs between different hosts and web applications belonging to the same domain, known as cross-subdomain cookies. For example, vulnerabilities in `example.com` might allow an attacker to get access to the session IDs from `secure.example.com`.
