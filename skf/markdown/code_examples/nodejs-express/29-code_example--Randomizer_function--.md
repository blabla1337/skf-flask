# Randomizer function

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
Please see [documentation for randomizer function](https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback).

## Example
Asynchronous:
```js
const crypto = require('crypto');

crypto.randomBytes(256, (err, buf) => {
    //buf holds your bytes
    if (err) throw err;

    console.log(`${buf.length} bytes of random data: ${buf.toString('hex')}`);
});
```

Synchronous:
```js
const crypto = require('crypto');
const buf = crypto.randomBytes(256);

console.log(`${buf.length} bytes of random data: ${buf.toString('hex')}`);
```

## Considerations
TBA
