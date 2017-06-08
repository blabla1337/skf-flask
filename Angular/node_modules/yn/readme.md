# yn [![Build Status](https://travis-ci.org/sindresorhus/yn.svg?branch=master)](https://travis-ci.org/sindresorhus/yn)

> Parse yes/no like values

Useful for validating answers of a CLI prompt.

-

The following case-insensitive values are recognized:

```js
'y', 'yes', 'true', true, 1, 'n', 'no', 'false', false, 0
```

*Enable lenient mode to gracefully handle typos.*


## Install

```
$ npm install --save yn
```


## Usage

```js
var yn = require('yn');

yn('y');
//=> true

yn('NO');
//=> false

yn(true);
//=> true

yn('abomasum');
//=> null

// lenient mode will use a key distance-based score
// to leniently accept typos of "yes" and "no"
yn('mo', {lenient: true});
//=> false
```

Unrecognized values return `null`.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
