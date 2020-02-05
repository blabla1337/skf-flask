# Session hijacking and fixation 

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
First you need to implement the strict transport security header. This is done in order to prevent users from accessing your application over an unprotected connection.

Strict transport security header can be set as shown below:
```js
response.setHeader('Strict-Transport-Security', 'max-age=31536000');
```

If all present and future subdomains will be `HTTPS`:
```js
response.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubdomains;');
```

We recoomend to have your domain included in the `HSTS` preload list maintained by Chrome (and used by Firefox and Safari). To achieve this you need to do the following: 
```js
response.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubdomains; preload');
```

The `preload` flag indicates the site owner's consent to have their domain preloaded. The preload list
enforces the browser to always present your application on HTTPS even on the first time the user hits your application.

Then you should set the `httpOnly` flag (please see "HttpOnly" in the code examples for more details about implementation).

Then set the flag for session timeout (please see "Timeout" in the code examples for more details about implementation).

Then set the session `secure` flag (see "Secure flag" in the code examples for more details about implementation).

On login we also need to add another cookie with a random value to the application in order to prevent an attacker to fixate an `JSSESSION` id on your users and hijack their sessions (This code example can be found in the "Login functionality" for more detailed information).

Now imagine the scenario after the login of the user (see the "Login functionality" in the code examples for more details). Whenever the user is logged in, the users IP address, user agent string and session id are also stored in the database these values are used in order to verify if there are multiple users active on the same session. 

If so, we can let the user decide to terminate the session and terminate theother assigned sessions.
```js
const login = (**args**) => {
		/* Passport prevents session fixation but doesn't track concurrent long lived sessions, this is custom code on top of passport
		*/
}
```

## Considerations
TBA
