# Hashing

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
For this you can use [`bcrypt` module](https://www.npmjs.com/package/bcrypt):
```js
const bcrypt = require('bcrypt')
	
const hash = password => {
	const saltRounds = 10;
	return bcrypt.hash(myPlaintextPassword, saltRounds);
}
```

Asynchronous method:
```js
const validatePassword = (user, password) => {
	bcrypt.compare(myPlaintextPassword, hash, (err, res) => {
		if(res) {
			// Passwords match, handle success
		} else {
			// Passwords don't match, handle failure
		} 
	});
};
```

Synchronous method:
```js
const validatePassword = (user, password) => {
	if(bcrypt.compareSync('somePassword', hash)) {
		// Passwords match, handle success
		return true;
	} else {
		// Passwords don't match, handle failure
		return false;
	}
}
```

## Considerations
TBA
