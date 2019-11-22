# Open Forwards and Redirects 

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
When using forwards and redirects you should make sure the URL is being explicitly declared in the code and cannot be manipulated by an attacker like in the case of `redirectTo` being dynamically set based on user input:
```js
app.get('/offers', (req, res, next) => {
    const redirectTo = req.query.redirect;
    res.redirect(redirectTo);
});
```

Generally you should avoid getting parameters which could contain user input into the redirect by any means. If for any reason this is not feasible, then you should make a whitelist input validation for the redirect as shown below:
```js
const validRedirectURLs = [...]; // list of URLs permitted for redirection

app.get('/offers', (req, res, next) => {
    const redirectTo = req.query.redirect;

    if(validRedirectURLs.includes(redirectTo)) {
        res.redirect(redirectTo);
    } else {
        return res.status(500).send({ error: 'Invalid redirection URL' });
    }
});
```

## Considerations
TBA
