# Randomizer function
-------

## Example:
//Documentation at: https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback

// Asynchronous
const crypto = require('crypto');
crypto.randomBytes(256, (err, buf) => {
  //buf holds your bytes
  if (err) throw err;
      console.log(`${buf.length} bytes of random data: ${buf.toString('hex')}`);
});

// Synchronous
const buf = crypto.randomBytes(256);
console.log(
  `${buf.length} bytes of random data: ${buf.toString('hex')}`);
