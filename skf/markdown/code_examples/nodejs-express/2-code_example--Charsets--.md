# Charsets

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
Charset header should be set on the response your server sends back to the client. For example, in the case of `text/html` this can be achieved by the following code: 
```js
res.charset = 'utf-8'; //utf-8 is the default encoding for json
```

Or directly in your HTML markup:
```html
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
```

### Considerations
TBA
    		