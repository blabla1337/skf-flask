# Anti-cashing headers 

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
Add the following headers to your response head in order to prevent the browser from caching:

### HTTP 1.1
```js
resp.set('Cache-Control', 'no-cache, no-store, must-revalidate');
```

### HTTP 1.0
```js
res.set('Pragma', 'no-cache');
```

### Proxies
```js
res.set('Expires', '0');
```

## Considerations
TBA
