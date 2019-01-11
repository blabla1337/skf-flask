# XSS filtering

- [General](#general)
- [Example](#example)
- [Considerations](#Considerations)

## General
TBA

## Example:
If you're creating server - side pages you can use [`dompurify`](https://www.npmjs.com/package/dompurify) to sanitize strings as shown below:
```js
const dompurify = require('dompurify');
...
const clean = DOMPurify.sanitize(dirty);
```
Then you can use sanitized string as normal.

### Dangerous methods in frameworks
If you're using a template engine or a framework, then **AVOID** using the following methods:

#### {{ mustache }} and Handlebars
```hbs
{{{ raw html }}}
```

#### EJS
```
<%- raw html %>
```

#### Nunjucks
```
{% raw html %}
```

#### Angular
```
<div ng-bind-html="raw html" />
```

#### React
```
<div dangerouslySetInnerHTML={raw html} />
```

#### Vue.js
```
<div v-html="raw html" />
```

## Considerations
TBA
